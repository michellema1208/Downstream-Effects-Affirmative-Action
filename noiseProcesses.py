
import numpy as np
from numpy import random
import posterior  #get rid of this soon

class NoiseProcesses:
    """ comment here """

    def __init__(self, seed):
        self.seed = np.random.seed(seed=seed)
        self.min = 0
        self.max = 100

    def addNoise(self, value, low, high):

        rand = np.random.randint(value-low, value+high+1)

        if (rand < self.min):
            return self.min
        elif (rand > self.max):
            return self.max

        return rand
