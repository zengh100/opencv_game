import numpy as np
import cv2
img = np.zeros((512,512,3))

# Center coordinates 
center_x = 120
center_y = 100 

  
# Radius of circle 
radius = 30
   
# Red color in BGR 
color = (0, 0, 255) 
   
# Line thickness of -1 px 
thickness = -1

x_speed = 1
y_speed = 1
while(1):   
    # Using cv2.circle() method 
    # Draw a circle of red color of thickness -1 px 
    cv2.circle(img, (center_x, center_y), radius, (0,0,0), thickness) 
    center_x += x_speed
    center_y += y_speed
    if(center_x>=512): 
        x_speed = -1
    if(center_x<=0): 
        x_speed = 1
    if(center_y>=512): 
        y_speed = -1
    if(center_y<=0): 
        y_speed = 1

    cv2.circle(img, (center_x, center_y), radius, color, thickness) 
    cv2.imshow("black image", img)
    key = cv2.waitKey(33) #0:  wait for infinitely
    if(key == 27): 
        break
cv2.destroyAllWindows()