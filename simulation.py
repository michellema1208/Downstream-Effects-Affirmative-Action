"""
simulation file
"""

from posterior import *
from noiseProcesses import *
import numpy as np

def main():

    # from NoiseProcesses
    # my_types = list(range(0, 100))
    my_types = np.random.binomial(100, .5, 100) #
    myNoiseProcess = NoiseProcesses(2)
    types_and_scores = [(x, myNoiseProcess.addNoise(x, 5, 5)) for x in my_types]
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
