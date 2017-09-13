import random
from collections import OrderedDict

from tictactoe.player import Player


class Agent(Player):

    def __init__(self, name):
        super().__init__(name)

        self.states = OrderedDict()
        self.explore = 0.1
        self.learning_rate = 0.1
        self.prev_state = None

    def convert_state(self, state):
        convert = {
            '-': '-',
            '*': '*',
            self.symbol: 'X'
        }

        return [convert.get(s, 'O') for s in state]

    def set_value(self, state, value):
        converted_state = self.convert_state(state)

        self.states[''.join(converted_state)] = value

    def get_value(self, state):
        converted_state = self.convert_state(state)

        for stored_state, value in self.states.items():
            match = all(i == '*' or i == j for i, j in zip(stored_state, converted_state))

            if match:
                return value

        return 0.5

    def update_value(self, new_value):
        if self.learning_rate and self.prev_state:
            old_value = self.get_value(self.prev_state)
            upd_value = old_value + self.learning_rate * (new_value - old_value)
            self.set_value(self.prev_state, upd_value)

    def end(self, winner):
        if winner and winner is self:
            self.update_value(1)
        if winner and winner is not self:
            self.update_value(0)

    def decide_move(self, state):
        possible_moves = [i + 1 for i in range(9) if state[i] == '-']

        if random.random() <= self.explore:
            move = random.choice(possible_moves)

            self.prev_state = state[:]
            self.prev_state[move - 1] = self.symbol

            return move

        move_to_state = {}
        move_to_values = {}

        for move in possible_moves:
            new_state = state[:]
            new_state[move - 1] = self.symbol

            move_to_state[move] = new_state
            move_to_values[move] = self.get_value(new_state)

        max_value = max(move_to_values.values())

        greedy_moves = [move for move, value in move_to_values.items() if value >= max_value]

        chosen_move = random.choice(greedy_moves)

        self.update_value(max_value)

        self.prev_state = move_to_state[chosen_move]

        return chosen_move

    def _repr_html_(self):
        html = "<table><tr><td>State</td><td>Value</td></tr>"

        for state, value in self.states.items():
            html += "<tr><td>{}</td><td>{}</td></tr>".format(state, value)

        html += "</table>"

        return html
