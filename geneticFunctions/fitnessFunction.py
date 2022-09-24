from skimage import color
import math

##############################################
## This file contains all fitness functions
## Pass the one you want to use as a parameter
## to population.
##
## Fitness functions expect an rgb image
## created by organism, and the refrence
## image in LAB units.
############################################

# This is the fitness function used and reccomended for project.
# Note: this fitness function has negative values, with an ideal fitness
# of 0. This is not an issue for rank based selection such as ours.
# But if you want to use a fitness based selection, you will likely
# have to adjust or create a new fitness function.
#
# This fitness is calculated by summing the 'distance' between the refrence
# image, and created image in LAB colorspace, for each pixel. For distance
# calculations the color coordinates are treated as spacial coordinates.
# LAB units are used because they are approximately perceptually uniform.
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