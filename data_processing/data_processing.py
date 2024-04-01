import pandas
import numpy
import copy
import msgpack
from types import SimpleNamespace
from deepazul.game_controller import AzulGameController, TITLE_COLORS


class DataProcessor:
    def __init__(self):
        self.support_game_controller = AzulGameController()

    def process_multiple_game_logs(self, game_logs):
        return pandas.concat([self.process_game_log(game_log) for game_log in game_logs], ignore_index=True)

    def process_game_log(self, game_log):
        game_log = msgpack.unpackb(game_log)
        game_winner = game_log[-1]['winner']
        features = [self.get_features_from_game_log(status) for status in game_log]
        result = pandas.DataFrame(features).astype(numpy.int8)
        result['game_winner'] = game_winner
        return result

    def get_features_from_game_log(self, status):
        status = SimpleNamespace(**status)
        features = {}
        title_colors = TITLE_COLORS

        for color in title_colors:
            features[f'total_factories_and_center_color{color}'] = status.center[color] + sum(
                [factory.count(color) for factory in status.factories])

        # This hack is to make the factories appear always in the same order based on their content
        factories = [''.join([f"{factory.count(color)}{color}" for color in title_colors]) for factory in
                     status.factories]
        factories.sort()
        for index, factory in enumerate(factories):
            for color in title_colors:
                features[f'factory{index}_{color}'] = factory[factory.find(color) - 1]

        for attribute in ['center', 'title_bag', 'discarded_titles']:
            for index, value in getattr(status, attribute).items():
                features[f'{attribute}_{index}'] = value

        features['player_turn'] = status.player_turn
        features[f'difference_score'] = status.scores[0] - status.scores[1]
        expected_points = self.get_expected_points(status)
        features[f'expected_difference_score_round_end'] = expected_points[0] - expected_points[1]
        expected_points_all_pattern = self.get_expected_points_all_pattern_lines_completed(status)
        features[f'expected_difference_score_all_pattern_lines_completed'] = expected_points_all_pattern[0] - \
                                                                             expected_points_all_pattern[1]

        for player in range(2):
            for index, pattern_line in enumerate(status.pattern_lines[player]):
                features[f'pattern_line{index}_player{player}_used'] = pattern_line['used']
                for color in title_colors:
                    features[f'pattern_line{index}_player{player}_color{color}'] = pattern_line['color'] == color

            for row in range(5):
                for col in range(5):
                    features[f'board_player{player}_row{row}_col{col}'] = int(status.boards[player][row][col]['filled'])

            features[f'floor_line_player{player}_len'] = len(status.floor_lines[player])

            for color in title_colors:
                features[f'floor_line_player{player}_color{color}'] = status.floor_lines[player].count(color)

            features[f'floor_line_player{player}_first_player_token'] = 'first_player_token' in status.floor_lines[
                player]

            board = status.boards[player]
            pattern_line = status.pattern_lines[player]

            for row_index in range(5):
                for column_index in range(5):
                    features[
                        f'board_player{player}_row{row_index}_col{column_index}_point_prediction'] = self.get_predicted_points_per_title_placement(
                        board=board,
                        row_index=row_index,
                        column_index=column_index
                    )

            for color in title_colors:
                features[f'avaiable_space_player{player}_color{color}'] = self.get_avaiable_space_color(
                    board=board,
                    pattern_line=pattern_line,
                    color=color
                )
                features[f'excess_titles_player{player}_color{color}'] = features[
                                                                             f'avaiable_space_player{player}_color{color}'] - \
                                                                         features[
                                                                             f'total_factories_and_center_color{color}']

            for n in range(5):
                features[f'titles_to_complete_player{player}_row{n}'] = self.get_titles_to_complete_row(board=board,
                                                                                                        pattern_line=pattern_line,
                                                                                                        row=n)
                features[f'titles_to_complete_player{player}_column{n}'] = self.get_titles_to_complete_column(
                    board=board, pattern_line=pattern_line, col=n)

            for color in title_colors:
                features[f'titles_to_complete_player{player}_color{color}'] = self.get_titles_to_complete_color(
                    board=board, pattern_line=pattern_line, color=color)

            features[f'completed_rows_player{player}'] = sum(
                [all([square['filled'] for square in board[row]]) for row in range(5)])
            features[f'completed_columns_player{player}'] = sum(
                [all([board[row][col]['filled'] for row in range(5)]) for col in range(5)])
            features[f'completed_colors_player{player}'] = sum([all([board[row][col]['filled'] for row in range(5) for
                                                                     col in range(5) if
                                                                     board[row][col]['color'] == color]) for color in
                                                                title_colors])

        return features

    def get_titles_to_complete_row(self, board, pattern_line, row):
        titles_to_complete = (row + 1) * 5
        for col in range(5):
            if board[row][col]['filled']:
                titles_to_complete -= (row + 1)
            elif pattern_line[row]['color'] == board[row][col]['color']:
                titles_to_complete -= (pattern_line[row]['used'])

        return titles_to_complete

    def get_titles_to_complete_column(self, board, pattern_line, col):
        titles_to_complete = 15
        for row in range(5):
            if board[row][col]['filled']:
                titles_to_complete -= (row + 1)
            elif pattern_line[row]['color'] == board[row][col]['color']:
                titles_to_complete -= (pattern_line[row]['used'])

        return titles_to_complete

    def get_titles_to_complete_color(self, board, pattern_line, color):
        titles_to_complete = 15
        for row in range(5):
            if pattern_line[row]['color'] == color:
                titles_to_complete -= (pattern_line[row]['used'])
            else:
                for col in range(5):
                    if board[row][col]['color'] == color:
                        if board[row][col]['filled']:
                            titles_to_complete -= (row + 1)
        return titles_to_complete

    def get_predicted_points_per_title_placement(self, board, row_index, column_index):
        if board[row_index][column_index]['filled']:
            return 0

        points = 1
        row_connection_found = False
        col_connection_found = False
        for r in [range(column_index + 1, 5), range(column_index - 1, -1, -1)]:
            for col in r:
                if board[row_index][col]['filled']:
                    points += 1
                    row_connection_found = True
                else:
                    break

        for r in [range(row_index + 1, 5), range(row_index - 1, -1, -1)]:
            for row in r:
                if board[row][column_index]['filled']:
                    points += 1
                    col_connection_found = True
                else:
                    break

        if row_connection_found and col_connection_found:
            points += 1

        completed_row = True
        for col in range(5):
            if (not board[row_index][col]['filled']) and (col != column_index):
                completed_row = False
        if completed_row:
            points += 2

        completed_column = True
        for row in range(5):
            if (not board[row][column_index]['filled']) and (row != row_index):
                completed_column = False
        if completed_column:
            points += 7

        completed_color = True
        color = board[row_index][column_index]['color']
        for row in range(5):
            for col in range(5):
                if (board[row][col]['color'] == color) and (not board[row][col]['filled']) and (row != row_index):
                    completed_color = False
        if completed_color:
            points += 10

        return points

    def get_expected_points_all_pattern_lines_completed(self, status):
        status_copy = copy.deepcopy(status)
        for player in range(2):
            for row in range(5):
                if status_copy.pattern_lines[player][row]['color'] is not None:
                    status_copy.pattern_lines[player][row]['used'] = row + 1
        return self.get_expected_points(status_copy)

    def get_expected_points(self, status):
        self.support_game_controller.set_status(status)
        self.support_game_controller.end_of_round()
        self.support_game_controller.game_end()
        return self.support_game_controller.status.scores

    def get_avaiable_space_color(self, board, pattern_line, color):
        avaiable_space = 0
        for row in range(5):
            for col in range(5):
                if board[row][col]['color'] == color:
                    already_filled = board[row][col]['filled']
            if (not already_filled) and pattern_line[row]['color'] in (None, color):
                avaiable_space += row + 1 - pattern_line[row]['used']
        return avaiable_space