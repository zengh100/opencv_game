import numpy as np
import cv2
img = np.zeros((512,512,3))

# Center coordinates 
center_coordinates = (120, 100) 
  
# Radius of circle 
radius = 30
   
# Red color in BGR 
color = (0, 0, 255) 
   
# Line thickness of -1 px 
thickness = -1
   
# Using cv2.circle() method 
# Draw a circle of red color of thickness -1 px 
cv2.circle(img, center_coordinates, radius, color, thickness) 
cv2.imshow("black image", img)

key = cv2.waitKey(0) #0:  wait for infinitely
cv2.destroyAllWindows()