import random
class Genome:
    def __init__(self,properties = None,lims=None):
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

    def copyGene(self):
        properties = {}
        properties['color'] = self.color
        properties['radius'] = self.radius
        properties['position'] = self.position
        return Genome(properties,self.lims)
    
    def mutateColor(self,mutationSize):
        r = min(max(0,random.randint(int(self.color[0]*(1-mutationSize)),int(self.color[0]*(1+mutationSize)))),255)
        g = min(max(0,random.randint(int(self.color[1]*(1-mutationSize)),int(self.color[1]*(1+mutationSize)))),255)
        b = min(max(0,random.randint(int(self.color[2]*(1-mutationSize)),int(self.color[2]*(1+mutationSize)))),255)
        self.color = [r,g,b]

    def mutatePosition(self,mutationSize):

        x = max(0,random.randint(int(self.position[0]*(1-mutationSize)),int(self.position[0]*(1+mutationSize))))
        y = max(0,random.randint(int(self.position[1]*(1-mutationSize)),int(self.position[1]*(1+mutationSize))))
        self.position = [min(x,self.lims['XY']['X'][1]),min(y,self.lims['XY']['Y'][1])]

    def mutateSize(self,mutationSize):
        self.radius = max(1,random.randint(int(self.radius*(1-mutationSize)),int(self.radius*(1+mutationSize))))