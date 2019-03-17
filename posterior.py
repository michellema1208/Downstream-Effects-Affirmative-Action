"""
QUESTIONS:
1. Why do we take in conditionalProbs?
2. What does askPosterior do again?
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
