import sys
import time
from Population import Population
import geneticFunctions.mutationFunction as mf
import geneticFunctions.breedingFunction as bf
import geneticFunctions.selectionFunction as sf
import geneticFunctions.fitnessFunction as ff
import os



start_time = time.time()
P = Population("MoonLight.jpg",mf.myMutate,bf.breed,sf.tournamentSelection,ff.labDistance,'MoonLight')
print("gen 0")
print("fitness: ",P.population[0].fitness)
print("--- %s seconds ---" % (time.time() - start_time))


P.continueInterface()