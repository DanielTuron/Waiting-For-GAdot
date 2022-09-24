from Organism import Genome, Organism
import random

def breed(dominantOrganism,otherOrganism,mutationFunction):
    ratio = dominantOrganism.compare(otherOrganism)
    dominance = ratio/(1+ratio)         #The rate at which we should take dominant gene's dots
    genes = []
    otherGenes = []
    numGenes = max(len(dominantOrganism.genes),len(otherOrganism.genes))
    for i in range(numGenes):
        takeDominant = random.random() < dominance
        if takeDominant:
            if i < len(dominantOrganism.genes):
                genes.append(dominantOrganism.genes[i].copyGene())
        else:
            if i < len(otherOrganism.genes):
                genes.append(otherOrganism.genes[i].copyGene())

    baby = Organism(dominantOrganism.realImageLAB,dominantOrganism.fitnessFunc,genes = genes,lims=dominantOrganism.lims, mutate = mutationFunction)
    return baby
