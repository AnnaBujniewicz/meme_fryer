import numpy as np
import cv2

img = cv2.imread("test_image.png")

kernel_size = 30
kernel_angle = 180

def on_trackbar_v(val):
    global kernel_size
    kernel_size = val
    vertical = np.zeros((kernel_size , kernel_size))
    vertical[:, int((kernel_size - 1)/2)] = np.ones(kernel_size)
    vertical = cv2.warpAffine(vertical, cv2.getRotationMatrix2D( (kernel_size / 2 -0.5 , kernel_size / 2 -0.5 ) , kernel_angle, 1.0), (kernel_size, kernel_size) )  
    vertical = vertical * ( 1.0 / np.sum(vertical) )
    vert_img = cv2.filter2D (img, -1, vertical)
    cv2.imshow("test", vert_img)


def on_trackbar_a(ang):
    global kernel_angle
    kernel_angle = ang
    vertical = np.zeros((kernel_size , kernel_size))
    vertical[:, int((kernel_size - 1)/2)] = np.ones(kernel_size)
    vertical = cv2.warpAffine(vertical, cv2.getRotationMatrix2D( (kernel_size / 2 -0.5 , kernel_size / 2 -0.5 ) , kernel_angle, 1.0), (kernel_size, kernel_size) )  
    vertical = vertical * ( 1.0 / np.sum(vertical) )
    vert_img = cv2.filter2D (img, -1, vertical)
    cv2.imshow("test", vert_img)


cv2.imshow("test", img)

cv2.namedWindow("bar")
cv2.createTrackbar("size", "bar" , 1, 500, on_trackbar_v)
cv2.createTrackbar("angle", "bar" , 0, 365, on_trackbar_a)

while(cv2.waitKey()!=27):
    print("Press esc to exit")