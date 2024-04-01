import copy
import random
import json
import msgpack
from types import SimpleNamespace
from game_controller.title_colors import TITLE_COLORS

FLOOR_LINE_PENALIZATION = (0, 1, 2, 4, 6, 8, 11, 14)
INITIAL_STATUS = SimpleNamespace(**{
    'factories': [[] for _ in range(5)],
    'center': {color: 0 for color in TITLE_COLORS} | {'first_player_token': True},
    'player_turn': 0,
    'pattern_lines': [
        [{'color': None, 'used': 0} for _ in range(5)],
        [{'color': None, 'used': 0} for _ in range(5)]
    ],
    'floor_lines': [[], []],
    'boards': [
        [[{'color': TITLE_COLORS[(-row + col) % len(TITLE_COLORS)], 'filled': False} for col in
          range(5)] for row in range(5)],
        [[{'color': TITLE_COLORS[(-row + col) % len(TITLE_COLORS)], 'filled': False} for col in
          range(5)] for row in range(5)]
    ],
    'scores': [0, 0],
    'game_end': False,
    'title_bag': {color: 20 for color in TITLE_COLORS},
    'discarded_titles': {color: 0 for color in TITLE_COLORS},
    'winner': None
})


class AzulGameController:
    def __init__(self, factories_strategy=None, manual_factories=None, track_game_log=True):
        self.status = copy.deepcopy(INITIAL_STATUS)
        self.manual_factories = manual_factories
        self.track_game_log = track_game_log
        if factories_strategy == 'all_at_start':
            self.fill_factories_strategy = self.fill_factories_manually
        elif factories_strategy == 'ask':
            self.fill_factories_strategy = self.ask_for_factories_each_fill
        else:
            self.fill_factories_strategy = self.fill_factories_random
        self.fill_factories_strategy()
        self.game_log = []

    def make_move(self, move):
        move = SimpleNamespace(**move)

        # Calculate the number of picked titles and deals with moving titles between factories and center
        if move.local == 0:
            if self.status.center['first_player_token']:
                self.status.floor_lines[self.status.player_turn].extend(['first_player_token'])
                self.status.center['first_player_token'] = False
            picked_titles = self.status.center[move.color]
            self.status.center[move.color] = 0
        else:
            factory = self.status.factories[move.local - 1]
            picked_titles = factory.count(move.color)
            for title in factory:
                if title != move.color:
                    self.status.center[title] += 1
            factory.clear()

        # Place the titles in the pattern lines and floor lines
        if move.pattern_line < 5:
            pattern_line = self.status.pattern_lines[self.status.player_turn][move.pattern_line]
            pattern_line['color'] = move.color
            excess_titles = picked_titles + pattern_line['used'] - move.pattern_line - 1
            pattern_line['used'] = min(move.pattern_line + 1, picked_titles + pattern_line['used'])
        else:
            excess_titles = picked_titles

        self.status.floor_lines[self.status.player_turn].extend([move.color for _ in range(excess_titles)])

        # Check if factories are empty and center is empty for end of turn
        titles_left = sum([len(factory) for factory in self.status.factories]) + sum(
            [self.status.center[color] for color in TITLE_COLORS])
        if titles_left == 0:
            self.end_of_round()

        self.status.player_turn = (self.status.player_turn + 1) % 2

        if self.status.game_end:
            self.game_end()

        if self.track_game_log:
            self.game_log.append(vars(self.status))

    def end_of_round(self):
        for player in range(2):
            for index, pattern_line in enumerate(self.status.pattern_lines[player]):
                if pattern_line['used'] == (index + 1):
                    self.add_to_board(row_index=index, player=player)

            floor_line = self.status.floor_lines[player]
            self.status.scores[player] = max(
                0,
                self.status.scores[player] - FLOOR_LINE_PENALIZATION[min(7, len(floor_line))]
            )
            if 'first_player_token' in floor_line:
                self.status.player_turn = (player + 1) % 2

            for title in floor_line:
                if title != 'first_player_token':
                    self.status.discarded_titles[title] += 1
            floor_line.clear()

        self.fill_factories_strategy()
        self.status.center['first_player_token'] = True

    def add_to_board(self, row_index, player):
        pattern_line = self.status.pattern_lines[player][row_index]
        board = self.status.boards[player]
        col_connection_found = False
        row_connection_found = False

        for index, square in enumerate(board[row_index]):
            if square['color'] == pattern_line['color']:
                square['filled'] = True
                self.status.scores[player] += 1
                column_index = index

        for r in (range(column_index + 1, 5), range(column_index - 1, -1, -1)):
            for col in r:
                if board[row_index][col]['filled']:
                    self.status.scores[player] += 1
                    row_connection_found = True
                else:
                    break

        for r in (range(row_index + 1, 5), range(row_index - 1, -1, -1)):
            for row in r:
                if board[row][column_index]['filled']:
                    self.status.scores[player] += 1
                    col_connection_found = True
                else:
                    break

        if row_connection_found and col_connection_found:
            self.status.scores[player] += 1

        self.status.discarded_titles[pattern_line['color']] += row_index
        pattern_line['color'] = None
        pattern_line['used'] = 0

        if all([square['filled'] for square in board[row_index]]):
            self.status.game_end = True

    def game_end(self):
        for player in range(2):
            board = self.status.boards[player]
            for row in range(5):
                if all([square['filled'] for square in board[row]]):
                    self.status.scores[player] += 2

            for col in range(5):
                if all([board[row][col]['filled'] for row in range(5)]):
                    self.status.scores[player] += 7

            for color in TITLE_COLORS:
                if all([square['filled'] for row in board for square in row if square['color'] == color]):
                    self.status.scores[player] += 10
        self.check_game_winner()

    def fill_factories_random(self):
        bag = [color for color, count in self.status.title_bag.items() for _ in range(count)]
        random.shuffle(bag)

        for factory in self.status.factories:
            while len(factory) < 4:
                if len(bag) == 0:
                    bag = [color for color, count in self.status.discarded_titles.items() for _ in range(count)]
                    random.shuffle(bag)
                    self.status.discarded_titles = {color: 0 for color in TITLE_COLORS}
                factory.append(bag.pop())

        for color in TITLE_COLORS:
            self.status.title_bag[color] = bag.count(color)

    def fill_factories_manually(self):
        """
        This function permits the user to control how factories are build each round passing a list.
        It is useful for tests or simulating recommended moves in a game that was already played.
        It is necessary to add an empty factories list in the end to not break the game.
        """
        self.status.factories = self.manual_factories.pop(0)
        self.get_titles_from_bag()

    def ask_for_factories_each_fill(self):
        self.status.factories = json.loads(input("Enter factories: "))
        self.get_titles_from_bag()

    def get_titles_from_bag(self):
        for factory in self.status.factories:
            for title in factory:
                self.status.title_bag[title] -= 1

                if (self.status.title_bag[title] < 0) or (sum([self.status.title_bag[color] for color in TITLE_COLORS]) == 0):
                    for color, value in self.status.discarded_titles.items():
                        self.status.title_bag[title] += value

    def check_valid_moves(self):
        valid_moves = []
        player = self.status.player_turn

        # Check all colors available in each pattern line
        valid_colors_pattern_lines = [set() for _ in range(5)]
        for index, pattern_line in enumerate(self.status.pattern_lines[player]):
            if not pattern_line['used'] == (index + 1):
                if pattern_line['color'] is not None:
                    valid_colors_pattern_lines[index].add(pattern_line['color'])
                else:
                    for color in TITLE_COLORS:
                        if not next((square['filled'] for square in self.status.boards[player][index] if square['color'] == color), False):
                            valid_colors_pattern_lines[index].add(color)

        # Combine the valid colors of the pattern lines and floor line with the center titles
        for color in TITLE_COLORS:
            value = self.status.center[color]
            if (value > 0):
                valid_moves.append({
                    'local': 0,
                    'color': color,
                    'pattern_line': 5
                })
                for pattern_line in range(5):
                    if color in valid_colors_pattern_lines[pattern_line]:
                        valid_moves.append({
                            'local': 0,
                            'color': color,
                            'pattern_line': pattern_line
                        })

        # Combine the valid colors of the pattern lines and floor line with the factory titles
        for index, factory in enumerate(self.status.factories):
            factory = set(factory)
            for color in factory:
                valid_moves.append({
                    'local': index + 1,
                    'color': color,
                    'pattern_line': 5
                })
                for pattern_line in range(5):
                    if color in valid_colors_pattern_lines[pattern_line]:
                        valid_moves.append({
                            'local': index + 1,
                            'color': color,
                            'pattern_line': pattern_line
                        })

        return valid_moves

    def play_game(self, agents):
        while not self.status.game_end:
            move = agents[self.status.player_turn].choose_move(status=self.status, move_list=self.check_valid_moves())
            self.make_move(move)

        game_logs = msgpack.packb(self.game_log)
        self.reset_game()

        return game_logs

    def check_game_winner(self):
        score = self.status.scores
        rows = [0, 0]
        for player in range(2):
            board = self.status.boards[player]
            for row in range(5):
                if all([square['filled'] for square in board[row]]):
                    rows[player] += 1

        if score[0] > score[1]:
            self.status.winner = 0
        elif score[1] > score[0]:
            self.status.winner = 1
        elif rows[0] > rows[1]:
            self.status.winner = 0
        elif rows[1] > rows[0]:
            self.status.winner = 1
        else:
            self.status.winner = 2

    def reset_game(self):
        self.game_log = []
        self.status = copy.deepcopy(INITIAL_STATUS)
        self.fill_factories_strategy()

    def set_status(self, status):
        self.status = copy.deepcopy(status)
