from ast import Or
import random
def doNothing(Organism):
    return

def myMutate(Organism):
    singlePropertyMutate(Organism)
    addMutate(Organism)
    removeMutate(Organism)


def singlePropertyMutate(Organism):
    probColorMutate = 0.004
    probSizeMutate = 0.007
    probPosMutate = 0.01
    for gene in Organism.genes:
        r=random.random()
        mutationSize = max(1,int(round(random.gauss(15,4))))/100
        if r < probColorMutate:
            gene.mutateColor(mutationSize)
        elif(r<probSizeMutate):
            gene.mutateSize(mutationSize)
        elif(r<probPosMutate):
            gene.mutatePosition(mutationSize)

def addMutate(Organism):
    probAddGene = 0.3
    r=random.random()
    if r < probAddGene:
        Organism.addGene(Organism.lims)

def removeMutate(Organism):
    probRemGene = 0.2
    r=random.random()
    if r < probRemGene:
        Organism.removeGene()

