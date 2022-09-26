import time
from Population import Population
import geneticFunctions.mutationFunction as mf
import geneticFunctions.breedingFunction as bf
import geneticFunctions.selectionFunction as sf
import geneticFunctions.fitnessFunction as ff

# Adjust these to use wanted genetic functions
fitnessFunction = ff.labDistance
mutationFunction = mf.myMutate
breedingFunction = bf.breed
selectionFunction = sf.tournamentSelection

# Create your project folder, and move the image into the folder
projectFolderName = 'MoonLight'
refrenceImageName = 'MoonLight.jpg'
pickleName = "pop2.obj"

start_time = time.time()
P = Population(refrenceImageName,mutationFunction,breedingFunction,selectionFunction,fitnessFunction,projectFolderName,pickleName=pickleName)
print("gen 0")
print("fitness: ",P.population[0].fitness)
print("--- %s seconds ---" % (time.time() - start_time))


P.continueInterface()
