from random import *

class NoiseProcesses:
    """ comment here """

    def __init__(self, seed):
        self.seed = seed

    def addNoise(value, low, high):
        return randrange(value-low, value+high)

    
