import cv2
import random

img = cv2.imread("./resources/poligons.jpg", -1)
print(type(img)) #numpy.ndarray
print(img.shape) #rows/height, columns/width, channels/rgb->opencv uses bgr

"""
pixel:
blue, green, red
[0, 0, 0]
0 - 255
"""

for i in range(50, img.shape[0], 2):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


tag = img[200:300, 50:250]
img[300:400, 250:450] = tag

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()