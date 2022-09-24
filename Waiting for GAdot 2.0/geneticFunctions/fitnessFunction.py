from skimage import color
import math

def labDistance(createdRGB, realLAB):
        createdLAB = color.rgb2lab(createdRGB)
        cLAB = createdLAB.reshape(createdLAB.shape[0]*createdLAB.shape[1],3)
        rLAB = realLAB.reshape(realLAB.shape[0]*realLAB.shape[1],3)

        distance = 0
        for i in range(cLAB.shape[0]):
            deltaX = cLAB[i][0] - rLAB[i][0]
            deltaY = cLAB[i][1] - rLAB[i][1]
            deltaZ = cLAB[i][2] - rLAB[i][2]
            delta = math.sqrt(deltaX**2 + deltaY**2 + deltaZ**2)
            distance = distance + delta
        
        return -1*distance