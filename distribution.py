"""
QUESTIONS:
0. make Distribution class an Abstract class
1. make getProb an ABSTRACT method?
2. make getProb return nothing? because it's actually defined in uniform
"""
from random import *

class Distribution:

    # QUESTION: Is it supposed to be the prob for one value? or a
    # list of values and their associated probabilites

    def getProb(value):
        return randrange(0, 1)
