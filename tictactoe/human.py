from tictactoe.player import Player


class Human(Player):

    def __init__(self, name):
        self.name = name

    def decide_move(self):
        move = int(input("{}, enter a move: ".format(self.name)))

        return move

    def win(self):
        print('{} WINS!!!!!!!!! *CONFETTI*'.format(self.name))

