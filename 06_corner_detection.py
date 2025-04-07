import numpy as np
import cv2

img = cv2.imread("./resources/poligons.jpg")
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grey,  #source image
                                  100,  #number of corners  
                                  0.1,  #minimum quality
                                  10)   #minimum euclidean distance

#corners = np.int0(corners)
corners = np.array(corners, dtype=np.int64)  
for corner in corners:
    x, y = np.ravel(corner) #or x, y corner.ravel()
    print(f"x= {x}, y= {y}")
    img = cv2.circle(img, (x, y), 4, (255, 0, 0), 1)


cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()