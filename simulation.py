"""
simulation file
"""

from posterior import *
from noiseProcesses import *
import numpy as np


#def generateTrueTypes(num_people, low, hi, probabilityDistributionFunction):
    #true_types = probabilityDistributionFunction()

def truncateTrueTypes(list, min, max):
    truncated_true_types = []
    for i in range(len(list)):
        if (list[i] < min):
            truncated_true_types.append(min)
        elif (list[i] > max):
            truncated_true_types.append(max)
        else:
            truncated_true_types.append(list[i])

    return truncated_true_types

def main():

    # from NoiseProcesses
    # my_types = list(range(0, 100))
    #my_types = np.random.binomial(100, .5, 10000) #
    #my_types = np.random.randint(0, 100, 10000)
    my_types = np.random.normal(50, 30, 10000)
    #TODO truncate true types
    my_types = [int(x) for x in my_types]
    my_types = truncateTrueTypes(my_types, 0, 100)
    myNoiseProcess = NoiseProcesses(2)
    types_and_scores = [(x, myNoiseProcess.addNoise(x, 5, 20)) for x in my_types]
    #print(types_and_scores)
    myPosterior = posterior.Posterior(50)
    new_list = myPosterior.askPosterior(types_and_scores)
    print(new_list)
    type_list = [x[0] for x in new_list]
    myPosterior.plotting(type_list, my_types)
    #val = myNoiseProcess.addNoise(20, 10, 10)
    #print(val)

    # from Posterior
    type_list = [1, 2, 3, 4, 5]
    type_and_score = [(1,1), (2,2), (3,3)]
    myPosterior = Posterior(2)
    new_list = myPosterior.askPosterior(type_and_score)
    #print(new_list)
    #myPosterior.plotting(type_list)

main()
