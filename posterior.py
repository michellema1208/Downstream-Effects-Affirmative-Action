"""
QUESTIONS:
1. Why do we take in conditionalProbs?
2. What does askPosterior do again?

NOTES:
1. Posterior and Conditional Probabilities are roughly the same thing
2. Helpful libraries:
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
    Returns: a distribution object?
    """
    def askPosterior(score):

        return
