##############################################
## The Organism class contains all information
## on individual 'paintings'
##
## Organism's have properties...
## canvasSize = ['width of canvas in pixels', 
##               'height of canvas in pixels']
## genes = list of Genomes for Organism
## fitnessFunc = fittness function being used
## realImageLAB = refrence image in LAB units
## lims = dict containing information on the
##          limits of the properties for this
##          Organism's Genomes.
##############################################

import random
import numpy as np
import cv2
from Genome import Genome

# Inputs -
#       realImageLAB - refrence image in LAB color units
#       fitnessFunction - fitness function being used
#       genes - If we already know the wanted genes (breeding)
#           pass them here
#       lims - The limits on properties for Genome's
#       startingGenes - How many genes to have on first generation
#       mutate - If we are mutating this organism, pass the function
class Organism:
    def __init__(self,realImageLAB,fitnessFunction,genes=None,lims=None,*,startingGenes = 50, mutate = None):
        self.canvasSize = [realImageLAB.shape[1],realImageLAB.shape[0]]
        if(lims==None):
            lims = {}
            lims['RGB'] = {}
            lims['RGB']['R'] = [0,255]
            lims['RGB']['G'] = [0,255]
            lims['RGB']['B'] = [0,255]
            lims['XY'] = {}
            lims['XY']['X'] = [0,self.canvasSize[0]]
            lims['XY']['Y'] = [0,self.canvasSize[1]]
            lims['radius'] = [3,15]
            self.lims = lims
        else:
            self.lims = lims

        if genes==None:
            self.genes=[]
            for i in range(startingGenes):
                self.addGene(self.lims)
        else:
            self.genes = genes

        self.realImageLAB = realImageLAB
        self.fitnessFunc = fitnessFunction
        
        if(mutate!=None):
            mutate(self)
        self.fitness = self.getFitness(realImageLAB)
    
    # Create a visual image of this Organism's 'painting'
    def makeImage(self):
        dots = self.genes
        image = np.zeros((self.canvasSize[1],self.canvasSize[0],3), np.uint8)
        image.fill(255)
        for dot in dots:
            image = cv2.ellipse(image, dot.position, (0,0),
                            0, 0, 0, dot.color, dot.radius)
        cv2.imshow("window",image)
        cv2.waitKey(0)

    # Create the RGB image from this Organism and send it to fitness function to get the fitness value
    def getFitness(self,realLAB):
        genes = self.genes
        image = np.zeros((self.canvasSize[1],self.canvasSize[0],3), np.uint8)
        image.fill(255)
        for gene in genes:
            image = cv2.ellipse(image, gene.position, (0,0),
                            0, 0, 0, gene.color, gene.radius)
        
        return self.fitnessFunc(image,realLAB)
    
    # ONLY WORKS FOR NEGATIVE FITNESS
    # Used for some applications in breeding, ratio of dominance between organisms
    def compare(self,otherOrganism):
        myF = self.fitness
        otherF = otherOrganism.fitness
        ratio = otherF/myF      #Note fitness is negative
        return ratio

    # Create a Genome with random values within limits
    def addGene(self,lims):
        self.genes.append(Genome(lims=lims))
    
    # Remove a random Genome from Organism
    def removeGene(self):
        self.genes.pop(random.randint(0,len(self.genes)-1))

        

    


