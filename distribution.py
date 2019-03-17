from random import *

#TODO: make this an ABSTRACT class
class Distribution:

    # QUESTION: Is it supposed to be the prob for one value? or a
    # list of values and their associated probabilites

    """TODO:
    1. make this an ABSTRACT method?
    2. no return? because it's actually defined in uniform
    """
    def getProb(value):
        return randrange(0, 1)
