

class Player(object):

    def __init__(self, name):
        self.name = name
        self.symbol = 'X'

    def set_symbol(self, symbol):
        self.symbol = symbol

    def decide_move(self, state):
        raise NotImplementedError()

    def end(self, winner):
        pass
