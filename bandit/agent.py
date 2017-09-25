import random


class Agent(object):

    def __init__(self, slots, greedy=0.9):
        self.slots = slots
        self.greedy = greedy

        self.estimates = {}

        for slot in slots:
            self.estimates[slot] = {
                'chosen': 0,
                'value': 0
            }

    def set_value(self, slot, value):
        self.estimates[slot]['value'] = value

    def get_value(self, slot):
        return self.estimates[slot]['value']

    def inc_steps(self, slot):
        self.estimates[slot]['chosen'] += 1

    def get_steps(self, slot):
        return self.estimates[slot]['chosen']

    def draw(self):
        if random.random() < self.greedy:
            slot = max(self.slots, key=self.get_value)
        else:
            slot = random.choice(self.slots)

        self.inc_steps(slot)

        reward = slot.draw()

        old_value = self.get_value(slot)
        new_value = old_value + (1 / self.get_steps(slot)) * (reward - old_value)

        self.set_value(slot, new_value)

        return reward

