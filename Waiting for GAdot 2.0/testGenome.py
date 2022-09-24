from Organism import Genome
import cv2
realIm = cv2.imread("farmSample.jpg")
gg = Genome()
f = gg.getFitness(realIm)
print(f)


gg.makeImage()