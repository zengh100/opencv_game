import numpy as np
import cv2

height = 512
width = 768
image = np.zeros((height, width, 3))

x=120
y=100

radius = 30
color = (0,0,255)
thickness = -1

key = 0
while(key != 27):
    cv2.circle(image, (x,y), radius, color, thickness)
    cv2.imshow("my image", image)
    key = cv2.waitKey(33)
    x = x+3
    y = y+3
