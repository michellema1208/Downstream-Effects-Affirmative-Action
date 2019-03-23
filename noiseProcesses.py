import numpy as np
from numpy import random

class NoiseProcesses:
    """ comment here """

    def __init__(self, seed):
        self.seed = np.random.seed(seed=seed)

    def addNoise(value, low, high):
        return np.random.randint(value-low, value+high+1)
