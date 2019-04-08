
import numpy as np
from numpy import random
import posterior  #get rid of this soon

class NoiseProcesses:
    """ comment here """

    def __init__(self, seed):
        self.seed = np.random.seed(seed=seed)
        self.min = 0
        self.max = 100

    def addUniformNoise(self, value, low, high):

        rand = np.random.randint(value-low, value+high+1)


        if (rand < self.min):
            return self.min
        elif (rand > self.max):
            return self.max

        return rand

    def addBinomialNoise(self, value, p, trials):
        rand = value + (2 * np.random.binomial(trials, p, 1) - trials)

        if (rand < self.min):
            return self.min
        elif (rand > self.max):
            return self.max

        return rand
