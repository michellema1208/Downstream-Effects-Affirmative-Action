"""
TODO:
* NOTE: Posterior and Conditional Probabilities are roughly the same thing

1. Look into helpful libraries:
    2.1 Numpy
    2.2 Scipy --> has a way of coming up with your own distribution

    Link: https://scicomp.stackexchange.com/questions/1658/define-custom-probability-density-function-in-python
    def myDistr:
        def probabilityDistributionFunction(x, ):

            return _____

    2.3 matplotlib --> mpl has function for plotting histograms
    2.4 Python notebook
"""

import matplotlib.pyplot as plt
import numpy as np

class Posterior:

    """
    Parameters: prior is a distribution object, conditionalProbs is a list
    """
    def __init__(self, prior, threshold):
        self.prior = prior
        self.threshold = threshold
        #self.conditionalProbs = conditionalProbs

    """
    Parameters: a list of tuples of the type and the SAT score ex. [(x_1, s_1), ..., (x_n, s_n)]
    Returns: list of the true types accepted by the college

    to get [(x_1, s_1), ..., (x_n, s_n)]:

    [(x, f(x)) for x in myList] where myList = [x_1, x_2, ...]
    """
    def askPosterior(typeAndScores):
        maxIndex = 0
        sorted_list = sorted(typeAndScores, key=lambda x: x[1])
        for i in range(len(sorted_list)):
            if sorted_list[i].second >= self.threshold:
                maxIndex = i
                break

        final_list = typesAndScores[maxIndex:]
        type_list = []
        for i in range(len(final_list)):
            type_list.append(final_list[i].first)

        return type_list

    """
    Parameters: takes in a list of the true types accepted by the college
    Returns: a hashtable with key = type, value = percentage of people who have those types
    """
    def trueTypePercentages(type_list):

        type_map = {}
        total_people = len(type_list)
        for type in type_list:
            if !type_map[type]:   #TODO: fix this syntax
                type_map[type] = 0
            type_map[type] += 1

        for type in type_map:
            type_map[type] = float(type_map[type])/total_people

        return type_map

    def trueType(type_list):

        for i in range(len(type_list)):
            type_list[i] = float(type_list[i])/len(type_list)

        return type_list

    """
    Parameters: a hashtable with key = type, value = percentage of people who have those types
    Returns:
    """
    def plotting(type_list):

        hist, bins = np.histogram(type_list, bins=range(type_list[0], type_list[len(type_list)-1]))
        width = 0.7 * (bins[1] - bins[0])
        center = (bins[:-1] + bins[1:]) / 2
        plt.bar(center, hist, align='center', width=width)
        plt.show()
