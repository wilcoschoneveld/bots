from tictactoe.player import Player


class Human(Player):

    def decide_move(self, state):
        move = int(input("{}, enter a move: ".format(self.name)))

        return move


