##############################################
## The Genome class contains all information
## on individual 'dots'
##
## Genome's have properties
## color = ['r','g', 'b'] (ints)
## position = ['x', 'y'] (ints)
## radius = int
## lims = dict containing information on the
##          limits of the other properties
##############################################

import random

# To initiate a Genome, pass the properties (color,radius,position), or the limits to randomly calculate these values within
# Initiation will FAIL if neither are passed
class Genome:
    def __init__(self,properties = None,lims=None):
        #The first run, as well as for some mutations, the properties will not be passed, in this case lims must be passed
        if(properties==None):
            maxRed = lims['RGB']['R'][1]
            maxGreen = lims['RGB']['G'][1]
            maxBlue = lims['RGB']['B'][1] 
            maxRadius = lims['radius'][1]
            maxX = lims['XY']['X'][1]
            maxY = lims['XY']['Y'][1]

            minRed = lims['RGB']['R'][0]
            minGreen = lims['RGB']['G'][0]
            minBlue = lims['RGB']['B'][0] 
            minRadius = lims['radius'][0]
            minX = lims['XY']['X'][0]
            minY = lims['XY']['Y'][0]    

            red = random.randint(minRed,maxRed)
            green = random.randint(minGreen,maxGreen)
            blue = random.randint(minBlue,maxBlue)
            x = random.randint(minX,maxX)
            y = random.randint(minY,maxY)
            radius = random.randint(minRadius,maxRadius)
        else:
            [red,green,blue] = properties['color']
            radius = properties['radius']
            [x,y] = properties['position']   
        self.lims=lims 
        self.color = [red,green,blue]
        self.position = [x,y]
        self.radius = radius

    # Create deep copy of genome, used when breeding
    def copyGene(self):
        properties = {}
        properties['color'] = self.color
        properties['radius'] = self.radius
        properties['position'] = self.position
        return Genome(properties,self.lims)
    
    