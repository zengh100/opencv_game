import numpy as np
import cv2

height = 512
width = 768
image_org = np.zeros((height, width, 3))

# Center coordinates 
center_x = 120
center_y = 100 

  
# Radius of circle 
radius = 30
   
# Red color in BGR 
color = (0, 0, 255) 
   
# Line thickness of -1 px 
thickness = -1

x_speed = 3
y_speed = 3

key = 0
while(key != 27):   
    # Using cv2.circle() method 
    # Draw a circle of red color of thickness -1 px
    image = image_org.copy()
    cv2.circle(image, (center_x, center_y), radius, color, thickness) 
    cv2.imshow("black image", image)
    center_x += x_speed
    center_y += y_speed    
    if(center_x+radius>=width): 
        x_speed = -3
    if(center_x-radius<=0): 
        x_speed = 3
    if(center_y+radius>=512): 
        y_speed = -3
    if(center_y-radius<=0): 
        y_speed = 3
        
    key = cv2.waitKey(33) #0:  wait for infinitely

cv2.destroyAllWindows()
