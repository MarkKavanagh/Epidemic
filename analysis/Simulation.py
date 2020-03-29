import time

import numpy as np


class Simulation(object):
    def __init__(self, entities):
        self.entities = entities

    def run(self):
        time.sleep(0.025)
        for entity in self.entities:
            dx = np.random.randint(-10, 11)
            dy = np.random.randint(-10, 11)
            entity.moveByAmount(dx, dy)
