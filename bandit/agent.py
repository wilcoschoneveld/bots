import random


class Agent(object):

    def __init__(self, slots, greedy=0.9, step_size='average', initial_value=0):
        self.slots = slots
        self.greedy = greedy
        self.step_size = step_size
        self.initial_value = initial_value

        self.estimates = {}
        self.reset()

    def reset(self):
        for slot in self.slots:
            self.estimates[slot] = {
                'chosen': 0,    
                'value': self.initial_value
            }

    def get_step_size(self, slot):
        if self.step_size == 'average':
            return 1 / self.get_steps(slot)

        return self.step_size

    def set_value(self, slot, value):
        self.estimates[slot]['value'] = value

    def get_value(self, slot):
        return self.estimates[slot]['value']

    def inc_steps(self, slot):
        self.estimates[slot]['chosen'] += 1

    def get_steps(self, slot):
        return self.estimates[slot]['chosen']

    def draw(self):
        for slot in self.slots:
            slot.update()

        if random.random() < self.greedy:
            slot = max(self.slots, key=self.get_value)
        else:
            slot = random.choice(self.slots)

        self.inc_steps(slot)

        reward = slot.draw()

        step_size = self.get_step_size(slot)
        old_value = self.get_value(slot)
        new_value = old_value + step_size * (reward - old_value)

        self.set_value(slot, new_value)

        return slot, reward

