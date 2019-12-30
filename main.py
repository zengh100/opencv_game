import cv2
import numpy as np
img = np.zeros((512,512,3))
cv2.imshow("black image", img)

key = cv2.waitKey(0) #0:  wait for infinitely

#key = cv2.waitKey(3000)#pauses for 3 seconds before fetching next image
#if key == 27:#if ESC is pressed, exit loop
#    cv2.destroyAllWindows()
#    break
cv2.destroyAllWindows()