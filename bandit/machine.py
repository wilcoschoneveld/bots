import random


class Machine(object):

    def __init__(self, mu=0, sigma=1):
        self.mu = mu
        self.sigma = sigma

    def update(self):
        self.mu += random.gauss(0, 0.01)

    def draw(self):
        return random.gauss(self.mu, self.sigma)

    @classmethod
    def random(cls):
        mu = random.gauss(0, 1)
        sigma = 1

        machine = cls(mu, sigma)

        return machine
