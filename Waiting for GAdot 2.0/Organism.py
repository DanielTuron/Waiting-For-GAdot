import random
import numpy as np
import cv2
import math
from skimage import color
from Genome import Genome
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
    
    def makeImage(self):
        dots = self.genes
        image = np.zeros((self.canvasSize[1],self.canvasSize[0],3), np.uint8)
        image.fill(255)
        for dot in dots:
            image = cv2.ellipse(image, dot.position, (0,0),
                            0, 0, 0, dot.color, dot.radius)
        cv2.imshow("window",image)
        cv2.waitKey(0)

    def getFitness(self,realLAB):
        genes = self.genes
        image = np.zeros((self.canvasSize[1],self.canvasSize[0],3), np.uint8)
        image.fill(255)
        for gene in genes:
            image = cv2.ellipse(image, gene.position, (0,0),
                            0, 0, 0, gene.color, gene.radius)
        
        return self.fitnessFunc(image,realLAB)
    
    def compare(self,otherGene):
        myF = self.fitness
        otherF = otherGene.fitness
        ratio = otherF/myF      #Note fitness is negative
        return ratio

    def addGene(self,lims):
        self.genes.append(Genome(lims=lims))
    
    def removeGene(self):
        self.genes.pop(random.randint(0,len(self.genes)-1))

        

    


