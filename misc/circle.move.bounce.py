import numpy as np
import cv2

height = 512
width = 768
image_org = np.zeros((height, width, 3))

x=120
y=100

radius = 30
color = (0,0,255)
thickness = -1

x_speed = 3
y_speed = 3

key = 0
while(key != 27):
    image = image_org.copy()
    cv2.circle(image, (x,y), radius, color, thickness)
    cv2.imshow("my image", image)
    key = cv2.waitKey(33)
    x = x+x_speed
    y = y+y_speed
    if(x+radius >= width):
       x_speed = -3
    if(x-radius <= 0):
       x_speed = 3
    if(y+radius >= height):
       y_speed = -3
    if(y-radius <= 0):
       y_speed = 3
cv2.destroyAllWindows()
