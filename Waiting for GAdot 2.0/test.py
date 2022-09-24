import cv2
import numpy as np
from skimage import io, color
image = cv2.imread("hq2.jpg")
    
# Window name in which image is displayed
window_name = 'Image'
   
center_coordinates = (0, 35)
  
axesLength = (0, 0)
  
angle = 0
  
startAngle = 0
  
endAngle = 0
   
# Red color in BGR
color = (130, 210, 255)
   
# Line thickness of 5 px
thickness = 15
   
# Using cv2.ellipse() method
# Draw a ellipse with red line borders of thickness of 5 px
image = cv2.ellipse(image, center_coordinates, axesLength,
           angle, startAngle, endAngle, color, thickness)
   
cv2.imshow(window_name,image)
cv2.waitKey(0)
rgb = cv2.imread("hq2.jpg")
from fitnessFunc import fitnessFunc

x=fitnessFunc(image,rgb)
print(x)

print("done")


