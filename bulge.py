import numpy as np
import cv2
from wand.image import Image


img = cv2.imread("test.jpg")

with Image.from_array(img) as img:
    img.distort('shepards', (0,0, 0,0,  0,img.width, 0,img.width,  img.height,0, img.height,0,  img.height,img.width, img.height,img.width,  (img.width/8),(img.height/3), (img.width*3/8),(img.height/3)))
    bulged = np.array(img)


cv2.imshow("test", bulged)
while(cv2.waitKey()!=27):
    print("Press esc to exit")