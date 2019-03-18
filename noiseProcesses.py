from random import *
"""
TODO:
1. For init, find Numpy function that will set random seed
"""

class NoiseProcesses:
    """ comment here """

    def __init__(self, seed):
        self.seed = seed

    def addNoise(value, low, high):
        return randrange(value-low, value+high)
