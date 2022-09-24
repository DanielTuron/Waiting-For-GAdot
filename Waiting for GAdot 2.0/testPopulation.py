import sys
import time
sys.path.append(r"C:\Users\dturo\Documents\Projects\Waiting for GAdot 2.0")
from Population import Population
import geneticFunctions.mutationFunction as mf
import geneticFunctions.breedingFunction as bf
import geneticFunctions.selectionFunction as sf
import geneticFunctions.fitnessFunction as ff

start_time = time.time()
P = Population("CityLights.png",mf.myMutate,bf.breed,sf.tournamentSelection,ff.labDistance,'run1.obj')
print("gen 0")
print("fitness: ",P.population[0].fitness)
print("--- %s seconds ---" % (time.time() - start_time))


P.continueInterface()