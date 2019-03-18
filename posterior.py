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
class Posterior:

    """
    Parameters: prior is a distribution object, conditionalProbs is a list
    """
    def __init__(self, prior, conditionalProbs):
        self.prior = prior
        self.conditionalProbs = conditionalProbs

    """
    Parameters: SAT score
    Returns: a list of tuples of the type and the SAT score ex. [(x_1, s_1), ..., (x_n, s_n)]

    to get [(x_1, s_1), ..., (x_n, s_n)]:

    [(x, f(x)) for x in myList] where myList = [x_1, x_2, ...]
    """
    def askPosterior(score):

        return

    """
    Parameters: takes in a list of tuples of the type and the SAT score ex. [(x_1, s_1), ..., (x_n, s_n)]
    Returns: a plot of type (x-axis) and probability that a type has a certain SAT score
    """
    def plotting():

        return
