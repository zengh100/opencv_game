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

absolute_speed = 10
x_speed = absolute_speed
y_speed = absolute_speed

bar_left = int(width/4)
bar_right = int(width/4*3)
key = 0
while(key != 27):
    image = image_org.copy()
    cv2.circle(image, (x,y), radius, color, thickness)
    cv2.line(image, (bar_left, height-1), (bar_right, height), color, 5)
    cv2.imshow("my circle game", image)
    key = cv2.waitKey(33)
    x = x+x_speed
    y = y+y_speed
    if(x+radius >= width):
       x_speed = -absolute_speed
    if(x-radius <= 0):
       x_speed = absolute_speed
    if(y+radius >= height):
       y_speed = -absolute_speed
       cv2.imwrite('reachBottom.png', image)
       if(x< bar_left or x > bar_right):
           cv2.waitKey(1000)
           break
    if(y-radius <= 0):
       y_speed = absolute_speed
cv2.destroyAllWindows()
