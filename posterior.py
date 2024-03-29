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
import pdb

class Posterior:

    """
    Parameters: prior is a distribution object, conditionalProbs is a list
    """
    def __init__(self, threshold, threshold_2):
        #self.prior = prior
        self.threshold = threshold
        self.threshold_2 = threshold_2
        #self.conditionalProbs = conditionalProbs

    """
    Parameters: a list of tuples of the type and the SAT score ex. [(x_1, s_1), ..., (x_n, s_n)]
    Returns: list of the true types accepted by the college

    to get [(x_1, s_1), ..., (x_n, s_n)]:

    [(x, f(x)) for x in myList] where myList = [x_1, x_2, ...]
    """
    def askPosterior(self, type_and_scores):
        filtered_type_and_scores = filter(lambda x: x[1] > self.threshold, type_and_scores)

        return sorted(filtered_type_and_scores, key=lambda x: x[0])

    """
    Parameters: a hashtable with key = type, value = percentage of people who have those types
    Returns:
    """
    def plotting(self, type_list, old_list):

        # for type_list
        hist, bins = np.histogram(type_list)
        width = 0.7 * (bins[1] - bins[0])
        #center = (bins[:-1] + bins[1:]) / 2
        numBins = (type_list[len(type_list)-1] - type_list[0]) + 1

        # for old_list
        hist2, bins2 = np.histogram(old_list)
        #center = (bins[:-1] + bins[1:]) / 2
        numBins2 = (old_list[len(old_list)-1] - old_list[0]) + 1

        plt.hist(type_list, bins=range(1, 101), alpha = .5, label="x") #align='center', width=width
        plt.hist(old_list, bins=range(1, 101), alpha = .5, label="y")
        plt.xticks(np.arange(0, 101, 2.0))
        plt.axvline(self.threshold, color='k', linestyle='solid', linewidth=1)
        plt.xlabel('True Types')
        plt.ylabel('Number of Applicants')
        plt.show()


    def plotTwoPopulationsAcceptedTrueTypes(self, accepted_types_1, accepted_types_2):
        fig,axes = plt.subplots(nrows = 1, ncols = 2)
        ax1, ax2 = axes.flatten()
        ax1.hist(accepted_types_1, bins=range(1, 101))
        ax1.set_title('population 1')
        ax2.hist(accepted_types_2, bins=range(1, 101))
        ax2.set_title('population 2')
        #ax1.xticks(np.arange(0, 101, 2.0))
        ax1.axvline(self.threshold, color='k', linestyle='solid', linewidth=1)
        plt.xticks(np.arange(0, 101, 2.0))
        ax2.axvline(self.threshold_2, color='k', linestyle='solid', linewidth=1)
        plt.show()


    def plotTwoPopulations(self, accepted_types_1, accepted_types_2, original_true_types, original_true_types_2):
        fig,axes = plt.subplots(nrows = 1, ncols = 2)
        ax1, ax2 = axes.flatten()
        ax1.hist(accepted_types_1, bins=range(1, 101), alpha = .5)
        ax1.hist(original_true_types, bins=range(1, 101), alpha = .5)
        ax1.set_title('population 1')
        ax2.hist(accepted_types_2, bins=range(1, 101), alpha = .5)
        ax2.hist(original_true_types_2, bins=range(1, 101), alpha = .5)
        ax2.set_title('population 2')

        ax1.axvline(50,color='k', linestyle='dotted', linewidth=1)
        ax2.axvline(50,color='k', linestyle='dotted', linewidth=1)
        ax1.axvline(self.threshold, color='k', linestyle='solid', linewidth=1)
        #ax2.xticks(np.arange(0, 101, 2.0))
        ax2.axvline(self.threshold_2, color='k', linestyle='solid', linewidth=1)
        ax1.set_xticks(np.arange(0, 101, 5.0))
        ax2.set_xticks(np.arange(0, 101, 5.0))
        plt.show()
