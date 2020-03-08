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

# Center coordinates 
center_x = 120
center_y = 100 

  
# Radius of circle 
radius = 30
   
# Red color in BGR 
color = (0, 0, 255) 
   
# Line thickness of -1 px 
thickness = -1

absolute_speed = 10
x_speed = absolute_speed
y_speed = absolute_speed

bar_left = int(width/4)
bar_right = int(width*3/4)
bar_height = height -1

key = 0
while(key != 27):   
    # Using cv2.circle() method 
    # Draw a circle of red color of thickness -1 px
    image = image_org.copy()
    cv2.circle(image, (center_x, center_y), radius, color, thickness)
    cv2.line(image, (bar_left, bar_height), (bar_right, bar_height), (0,255,0), 5)

    text = '(' + str(center_x) + ',' + str(center_y) + ')'
    write_text(image, text,(center_x, center_y))
    
    
    cv2.imshow("black image", image)
    center_x += x_speed
    center_y += y_speed

    
    if(center_x+radius>=width): 
        x_speed = -absolute_speed
    if(center_x-radius<=0): 
        x_speed = absolute_speed
    if(center_y+radius>=height): 
        y_speed = -absolute_speed
        
        if(center_x < bar_left or center_x > bar_right):
           write_text(image, 'Game Over', (bar_left, int(height/2)))
           cv2.imshow("black image", image)
           cv2.imwrite('gameOver.png', image)
           cv2.waitKey(2000)
           break
        
    if(center_y-radius<=0): 
        y_speed = absolute_speed
        
    key = cv2.waitKey(33) #0:  wait for infinitely
    if key == ord('a'):
        bar_left -= 20
        bar_right -= 20
        
    if key == ord('d'):
        bar_left += 20
        bar_right += 20
        
cv2.destroyAllWindows()
