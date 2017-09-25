import random


class Agent(object):

    def __init__(self, slots, greedy=0.9):
        self.slots = slots
        self.greedy = greedy

        self.history = {
            'actions': [],
            'rewards': []
        }

    def draw(self):
        if random.random() < self.greedy:
            slot = max(self.slots, key=lambda s: self.estimated_value(s))
        else:
            slot = random.choice(self.slots)

        value = slot.draw()

        self.history['actions'].append(slot)
        self.history['rewards'].append(value)

        return value

    def estimated_value(self, slot):
        values = []

        for action, reward in zip(self.history['actions'], self.history['rewards']):
            if action == slot:
                values.append(reward)

        if not values:
            return 0

        return sum(values) / len(values)
