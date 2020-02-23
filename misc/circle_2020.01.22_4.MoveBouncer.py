import numpy as np
import cv2

def write_text(img, text, bottomLeftCornerOfText):
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    fontScale              = 2
    fontColor              = (255,255,255)
    lineType               = 2

    cv2.putText(img,text, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
height = 512
width = 768
image_org = np.zeros((height, width, 3))

x=120
y=100

radius = 30
red = (0,0,255)
green = (0,255,0)
thickness = -1

absolute_speed = 10
x_speed = absolute_speed
y_speed = absolute_speed

bar_left = int(width/4)
bar_right = int(width/4*3)
key = 0
while(key != 27):
    image = image_org.copy()
    cv2.circle(image, (x,y), radius, red, thickness)
    cv2.line(image, (bar_left, height-1), (bar_right, height-1), green, 5)
    cv2.imshow("my image", image)
    key = cv2.waitKey(33)
    if(key != -1):
        #key = key%256
        print('key=', key)
        if key == ord('a'):
            bar_left -= 20
            bar_right -= 20
        if key == ord('d'):
            bar_left += 20
            bar_right += 20                      
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
           write_text(image, 'Game Over', (bar_left, int(height/2)))
           cv2.imshow("my image", image)
           cv2.imwrite('gameOver.png', image)
           cv2.waitKey(2000)
           break
    if(y-radius <= 0):
       y_speed = absolute_speed
cv2.destroyAllWindows()
