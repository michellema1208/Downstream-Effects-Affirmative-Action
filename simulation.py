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
        #if (list[i] < min):
            #truncated_true_types.append(min)
        #elif (list[i] > max):
            #truncated_true_types.append(max)
        #else:
        if (list[i] > min and list[i] < max):
            truncated_true_types.append(list[i])

    return truncated_true_types




def main():

    # from NoiseProcesses
    # my_types = list(range(0, 100))
    #original_true_types = np.random.binomial(100, .5, 10000) #
    #original_true_types = np.random.randint(0, 100, 10000)
    original_true_types = np.random.normal(50, 30, 500000)
    #TODO truncate true types
    original_true_types = [int(x) for x in original_true_types]
    original_true_types = truncateTrueTypes(original_true_types, 0, 100)
    myNoiseProcess = NoiseProcesses(2)
    true_types_and_noisy_scores = [(x, myNoiseProcess.addUniformNoise(x, 2, 15)) for x in original_true_types]
    #true_types_and_noisy_scores = [(x, myNoiseProcess.addBinomialNoise(x, .8, 10)) for x in original_true_types]
    #print(types_and_scores)
    myPosterior = posterior.Posterior(58.5, 41.5)
    accepted_types_and_score = myPosterior.askPosterior(true_types_and_noisy_scores)
    #print(new_list)
    accepted_types = [x[0] for x in accepted_types_and_score]

    #POPULATION 2

    original_true_types_2 = np.random.normal(50, 30, 500000)
    #TODO truncate true types
    original_true_types_2 = [int(x) for x in original_true_types_2]
    original_true_types_2 = truncateTrueTypes(original_true_types_2, 0, 100)
    myNoiseProcess_2 = NoiseProcesses(2)
    true_types_and_noisy_scores_2 = [(x, myNoiseProcess_2.addUniformNoise(x, 15, 2)) for x in original_true_types_2]
    #true_types_and_noisy_scores = [(x, myNoiseProcess.addBinomialNoise(x, .8, 10)) for x in original_true_types]
    #print(types_and_scores)
    myPosterior_2 = posterior.Posterior(41.5, 58.5)
    accepted_types_and_score_2 = myPosterior_2.askPosterior(true_types_and_noisy_scores_2)
    #print(new_list)
    accepted_types_2 = [x[0] for x in accepted_types_and_score_2]

    myPosterior.plotTwoPopulations(accepted_types, accepted_types_2, original_true_types, original_true_types_2)



    #myPosterior.plotting(accepted_types, original_true_types)
    #val = myNoiseProcess.addNoise(20, 10, 10)
    #print(val)

    #Grades
    #gradesNoiseProcess = NoiseProcesses(2)
    #types_after_grades =  [(x, gradesNoiseProcess.addBinomialNoise(x, .8, 10)) for x in type_list]
    #grades_list = [x[0] for x in types_after_grades]
    #myPosterior.plotting(type_list, grades_list)

    # from Posterior
    type_list = [1, 2, 3, 4, 5]
    type_and_score = [(1,1), (2,2), (3,3)]
    myPosterior = Posterior(2)
    new_list = myPosterior.askPosterior(type_and_score)
    #print(new_list)
    #myPosterior.plotting(type_list)

main()
