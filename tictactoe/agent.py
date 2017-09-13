import random
from collections import OrderedDict

from tictactoe.player import Player


class Agent(Player):

    def __init__(self, name):
        super().__init__(name)

        self.states = OrderedDict()
        self.init_values()

    def init_values(self):
        from tictactoe.game import TicTacToe

        for line in TicTacToe.win_with:
            state = ['*'] * 9
            for i in line:
                state[i - 1] = 'X'
            self.set_value(state, 1)

    def set_value(self, state, value):
        self.states[''.join(state)] = value

    def get_value(self, state):
        convert = {
            '-': '-',
            self.symbol or 'X': 'X'
        }

        converted_state = [convert.get(s, 'O') for s in state]

        for stored_state, value in self.states.items():
            match = all(i == '*' or i == j for i, j in zip(stored_state, converted_state))

            if match:
                return value

        return 0.5

    def decide_move(self, state):
        possible_moves = [i + 1 for i in range(9) if state[i] == '-']

        expected_values = {}

        for move in possible_moves:
            new_state = state[:]
            new_state[move - 1] = self.symbol

            expected_values[move] = self.get_value(new_state)

        max_value = max(expected_values.values())

        greedy_moves = [move for move, value in expected_values.items() if value >= max_value]

        chosen_move = random.choice(greedy_moves)

        return chosen_move

    def _repr_html_(self):
        html = "<table><tr><td>State</td><td>Value</td></tr>"

        for state, value in self.states.items():
            html += "<tr><td>{}</td><td>{}</td></tr>".format(state, value)

        html += "</table>"

        return html
