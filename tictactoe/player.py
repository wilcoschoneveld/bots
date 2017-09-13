

class Player(object):

    def __init__(self, name):
        self.name = name

    def decide_move(self, state):
        raise NotImplementedError()

    def win(self):
        print('{} WINS!!!!!!!!! *CONFETTI*'.format(self.name))
