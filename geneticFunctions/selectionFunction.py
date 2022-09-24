##############################################
## This file contains all mutation functions
## Pass the one you want to use as a parameter
## to population.
##
## Mutation functions expect a Population
## object as only parameter
############################################


import random

# This is the selection function used and reccomended for project
# This selection function process goes as...
# Place a certain number of organisms in population into a habitat
# Now, the strongest 2 Organisms in the habitat will breed,
# and the weakest Organism will die.
# Repeat this process for any certain number of times
# The babies/offsprings get added after all repetitions
def tournamentSelection(Population):
    #IMPORTANT POPULATION NEEDS TO BE SORTED BEFORE COMING HERE

    # Note REPLACE_RATE + TOURNAMENT_PORTION < 1
    REPLACE_RATE = 0.8  #Portion of population to perish
    TOURNAMENT_PORTION = 0.1    #Size of tournaments as ratio of population size
    popSz = len(Population.population)
    replaceNum = round(REPLACE_RATE*popSz)
    TOURNAMENT_SIZE = round(TOURNAMENT_PORTION*popSz)

    babies = []
    for i in range(replaceNum):
        habitat = sorted(random.sample(range(popSz),TOURNAMENT_SIZE))   #Random indices of population
        goingToDie = max(habitat)   #Last indici has lowest fitness
        goingToBreed = [habitat[0], habitat[1]]     #first indices have highest fitness
        Population.population.pop(goingToDie)       #Yes yes very sad... Anyways
        babyGene = Population.breed(Population.population[goingToBreed[0]],Population.population[goingToBreed[1]],Population.mutate)
        babies.append(babyGene)
        popSz = popSz - 1

    #Add the offspring at the end
    for baby in babies:
        Population.population.append(baby)