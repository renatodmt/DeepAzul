from deepazul.game_controller import AzulGameController
import random
import pandas
import numpy
import copy
from types import SimpleNamespace

class RandomAgent:
    def choose_move(self, move_list, status=None):
        return move_list.pop(random.randint(0, len(move_list)-1))


class NeuralNetworkAgent:
    def __init__(self, temperature, model, print_probabilities=False):
        self.temperature = temperature
        self.model = model
        self.print_probabilities = print_probabilities

    def choose_move(self, move_list, status):
        current_player = status.player_turn
        support_game_controller = AzulGameController(track_game_log=False)
        future_status = []
        winners = []
        for move in move_list:
            support_game_controller.set_status(status)
            support_game_controller.make_move(move)
            future_status.append(SimpleNamespace(**vars(support_game_controller.status)))
            winners.append(support_game_controller.status.winner)

        predict = self.model.predict(future_status)
        predict = pandas.DataFrame(predict, columns=['player_0', 'player_1', 'draw'])
        predict['move'] = move_list
        predict['winner'] = numpy.select(
            condlist=[
                winners == current_player,
                winners == 2,
                winners == (current_player + 1) % 2
            ],
            choicelist=[1, 0.01, 0],
            default=None
        )

        predict['prediction'] = numpy.where(
            predict.winner.isna(),
            predict[f'player_{current_player}'],
            predict['winner']
        )
        predict['pick_probability'] = numpy.exp((predict.prediction / self.temperature).astype(float))
        pick_probability_sum = predict['pick_probability'].sum()
        predict['pick_probability'] = predict['pick_probability'] / pick_probability_sum

        if self.print_probabilities:
            print(f'Winning probabilities: {predict.prediction.max()}')
        return predict.loc[numpy.random.choice(predict.index, p=predict.pick_probability), 'move']
