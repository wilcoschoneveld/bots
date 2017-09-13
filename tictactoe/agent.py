import random

from tictactoe.player import Player


class Agent(Player):

    def decide_move(self, state):
        possible_moves = [i + 1 for i in range(9) if state[i] == '-']

        move = random.choice(possible_moves)

        print("{} chooses move {}".format(self.name, move))

        return move
