##############################################
## This file contains all mutation functions
## Pass the one you want to use as a parameter
## to population.
##
## Mutation functions expect an Organism
## object as only parameter
##############################################

import random

# If you want to test without any mutation. Not reccomended for actual runs.
def doNothing(Organism):
    return

# The mutation function used and reccomended in this project
def myMutate(Organism):
    #Chance of mutating one property of each gene
    singlePropertyMutate(Organism)

    #Chance of adding gene
    addMutate(Organism)

    #Chance of removing gene
    removeMutate(Organism)

# This has a chance to mutate a single property for each gene in Organism
# The mutation size is decided by a gaussian centered on 15% with a standard
# deviation of 4%
def singlePropertyMutate(Organism):
    # Note the latter mutations can only happen if the former have not.
    # and so, although probSizeMutate = probColorMutate + x. The probability
    # of a size mutation is only x. This is done in order to reduce the number
    # of random numbers that need get generated.
    probColorMutate = 0.004
    probSizeMutate = probColorMutate + 0.003
    probPosMutate = probSizeMutate + 0.003
    for gene in Organism.genes:
        r=random.random()
        if r < probColorMutate:
            mutationSize = max(1,int(round(random.gauss(15,4))))/100
            mutateColor(gene,mutationSize)
        elif(r<probSizeMutate):
            mutationSize = max(1,int(round(random.gauss(15,4))))/100
            mutateSize(gene,mutationSize)
        elif(r<probPosMutate):
            mutationSize = max(1,int(round(random.gauss(15,4))))/100
            mutatePosition(gene,mutationSize)

# This gives the chance to add a gene on to organism
def addMutate(Organism):
    probAddGene = 0.3
    r=random.random()
    if r < probAddGene:
        Organism.addGene(Organism.lims)

# This gives the chance to remove a random gene from an organism
def removeMutate(Organism):
    probRemGene = 0.2
    r=random.random()
    if r < probRemGene:
        Organism.removeGene()

# Mutate the r,g,b values of the gene to a random value within (1-M)*Value*(1+M). Where M is mutation size
def mutateColor(gene,mutationSize):
        r = min(max(0,random.randint(int(gene.color[0]*(1-mutationSize)),int(gene.color[0]*(1+mutationSize)))),255)
        g = min(max(0,random.randint(int(gene.color[1]*(1-mutationSize)),int(gene.color[1]*(1+mutationSize)))),255)
        b = min(max(0,random.randint(int(gene.color[2]*(1-mutationSize)),int(gene.color[2]*(1+mutationSize)))),255)
        gene.color = [r,g,b]

# Mutate the x,y values of the gene to a random value within (1-M)*Value*(1+M). Where M is mutation size
def mutatePosition(gene,mutationSize):
    x = max(0,random.randint(int(gene.position[0]*(1-mutationSize)),int(gene.position[0]*(1+mutationSize))))
    y = max(0,random.randint(int(gene.position[1]*(1-mutationSize)),int(gene.position[1]*(1+mutationSize))))
    gene.position = [min(x,gene.lims['XY']['X'][1]),min(y,gene.lims['XY']['Y'][1])]

# Mutate the radius of the gene to a random value within (1-M)*Value*(1+M). Where M is mutation size
def mutateSize(gene,mutationSize):
    gene.radius = max(1,random.randint(int(gene.radius*(1-mutationSize)),int(gene.radius*(1+mutationSize))))