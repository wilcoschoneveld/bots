import random
from collections import OrderedDict

from tictactoe.player import Player

invariants = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [7, 4, 1, 8, 5, 2, 9, 6, 3],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [3, 6, 9, 2, 5, 8, 1, 4, 7],
    [7, 8, 9, 4, 5, 6, 1, 2, 3],
    [9, 6, 3, 8, 5, 2, 7, 4, 1],
    [3, 2, 1, 6, 5, 4, 9, 8, 7],
    [1, 4, 7, 2, 5, 8, 3, 6, 9]
]


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
            self.symbol: 'X'
        }

        hashes = []

        for i in invariants:
            _hash = ''.join(convert.get(state[j - 1], '0') for j in i)
            hashes.append(_hash)

        return hashes

    def set_value(self, state, value):
        hashes = self.convert_state(state)

        for h in hashes:
            if h in self.states:
                self.states[h] = value
                return

        self.states[hashes[0]] = value

    def get_value(self, state):
        hashes = self.convert_state(state)

        for h in hashes:
            if h in self.states:
                return self.states[h]

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
