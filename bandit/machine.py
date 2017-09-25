import random


class Machine(object):

    def __init__(self, mu=100, sigma=20):
        self.mu = mu
        self.sigma = sigma

    def draw(self):
        return max(0, random.gauss(self.mu, self.sigma))

    @classmethod
    def random(cls):
        mu = random.randint(100, 1000)
        sigma = random.randint(20, 100)

        machine = cls(mu, sigma)

        return machine
