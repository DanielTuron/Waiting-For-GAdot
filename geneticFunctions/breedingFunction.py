##############################################
## This file contains all breeding functions
## Pass the one you want to use as a parameter
## to population.
##
## Breeding functions expect two Organisms
## and a mutation function as parameters
############################################

from Organism import Organism
import random

# This breeding function works by calculating a dominiance ratio
# based on how much stronger one organism was. And then taking genes
# one by one from two parents, at an approximate ratio given by the
# dominance ratio.
def breed(dominantOrganism,otherOrganism,mutationFunction):
    ratio = dominantOrganism.compare(otherOrganism) #This comparison function is currently based on negative fitness
    dominance = ratio/(1+ratio)         #The rate at which we should take dominant gene's dots
    genes = []
    numGenes = max(len(dominantOrganism.genes),len(otherOrganism.genes))    #If we are adding and removing gene's these may be different
    for i in range(numGenes):
        takeDominant = random.random() < dominance
        if takeDominant:
            #make sure the gene exists
            if i < len(dominantOrganism.genes):
                genes.append(dominantOrganism.genes[i].copyGene())
        else:
            #make sure the gene exists
            if i < len(otherOrganism.genes):
                genes.append(otherOrganism.genes[i].copyGene())

    #Now create the baby with these gene's, and mutate it with the passed mutation function
    baby = Organism(dominantOrganism.realImageLAB,dominantOrganism.fitnessFunc,genes = genes,lims=dominantOrganism.lims, mutate = mutationFunction)
    return baby
