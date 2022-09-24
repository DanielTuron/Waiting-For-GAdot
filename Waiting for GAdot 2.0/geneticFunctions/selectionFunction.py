import random
def tournamentSelection(Population):
    #POPULATION NEEDS TO BE SORTED BEFORE COMING HERE
    REPLACE_RATE = 0.8
    TOURNAMENT_RATE = 0.1
    popSz = len(Population.population)
    replaceNum = round(REPLACE_RATE*popSz)
    TOURNAMENT_SIZE = round(TOURNAMENT_RATE*popSz)
    babies = []
    for i in range(replaceNum):
        tourney = sorted(random.sample(range(popSz),TOURNAMENT_SIZE))
        goingToDie = max(tourney)
        goingToBreed = [tourney[0], tourney[1]]
        Population.population.pop(goingToDie)
        babyGene = Population.breed(Population.population[goingToBreed[0]],Population.population[goingToBreed[1]],Population.mutate)
        babies.append(babyGene)
        popSz = popSz - 1
    for baby in babies:
        Population.population.append(baby)