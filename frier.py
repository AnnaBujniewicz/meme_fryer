import numpy as np
import cv2
import random
from matplotlib import pyplot as plt
from wand.image import Image

def showsauteimage(path):

    img = cv2.imread(path,1)
    
    # blur
    ksize = (5, 5)
    blurred = cv2.GaussianBlur(img, ksize, cv2.BORDER_REFLECT)
    
    # noise

    prob = 0.4

    im = np.zeros(img.shape, img.dtype)
    im.astype(np.uint8)
    noise = cv2.randn(im, (0,0,0),(50,50,50))
    noise = noise * 0.4
    
    for i in range(noise.shape[0]):
        for j in range(noise.shape[1]):
            rdn = random.random()
            if rdn < prob:
                noise[i][j] = 0
            else:
                noise[i][j] = noise[i][j]
    

    im1 = np.zeros(img.shape, img.dtype)
    im1.astype(np.uint8)
    noise1 = cv2.randn(im1, (0,0,0),(50,50,50))
    noise1 = noise1 * 0.4

    for i in range(noise1.shape[0]):
        for j in range(noise1.shape[1]):
            rdn = random.random()
            if rdn < prob:
                noise1[i][j] = 0
            else:
                noise1[i][j] = noise1[i][j]

    rows,cols,chan = blurred.shape

    for y in range(rows):
        for x in range(cols):
            pixel = blurred[y][x]
            pixel_n = noise[y][x]
            t = pixel+pixel_n
            top = any([True for j in t if j >=230])
            if top:
                blurred[y,x] = [255,255,255]
            else:
                blurred[y,x] = t 

    for y in range(rows):
        for x in range(cols):
            pixel = blurred[y][x]
            pixel_1 = noise1[y][x]
            t = pixel-pixel_1
            top = any([True for j in t if j <=5])
            if top:
                blurred[y,x] = [0,0,0]
            else:
                blurred[y,x] = t 
    

    # contrast

    contrasted = blurred*1.4
    contrasted = np.clip(contrasted, 0, 255)
    contrasted=contrasted.astype("uint8")

    
    # saturation
    saturation_weights = [0.60, 0.80, 1.0]
    saturated = np.zeros(contrasted.shape, contrasted.dtype)
    for y in range(contrasted.shape[0]):
        for x in range(contrasted.shape[1]):
            for c in range(contrasted.shape[2]):
                saturated[y,x,c] = saturation_weights[c] * np.clip(contrasted[y,x,c] - 50, 0, 255)
    
    cv2.imshow("Here is your sauted image!", saturated)
    cv2.imwrite("sauted_image.png", saturated)


if __name__ == '__main__':
   
    img = cv2.imread("test_image1.png",1)
    
    # blur
    #ksize = (5, 5)
    #blurred = cv2.GaussianBlur(img, ksize, cv2.BORDER_REFLECT)
    
    # motion blur
    
    kernel_v = 20
    kernel_angle = 60
    vertical = np.zeros((kernel_v , kernel_v))
    vertical[:, int((kernel_v - 1)/2)] = np.ones(kernel_v)
    vertical = cv2.warpAffine(vertical, cv2.getRotationMatrix2D( (kernel_v / 2 -0.5 , kernel_v / 2 -0.5 ) , kernel_angle, 1.0), (kernel_v, kernel_v) )  
    vertical = vertical * ( 1.0 / np.sum(vertical) )
    vert_img = cv2.filter2D(img, -1, vertical)

    # noise

    prob = 0.1

    im = np.zeros(img.shape, img.dtype)
    im.astype(np.uint8)
    noise = cv2.randn(im, (0,0,0),(50,50,50))
    noise = noise * 0.9
    
    for i in range(noise.shape[0]):
        for j in range(noise.shape[1]):
            rdn = random.random()
            if rdn < prob:
                noise[i][j] = 0
            else:
                noise[i][j] = noise[i][j]
    

    im1 = np.zeros(img.shape, img.dtype)
    im1.astype(np.uint8)
    noise1 = cv2.randn(im1, (0,0,0),(50,50,50))
    noise1 = noise1 * 0.4

    for i in range(noise1.shape[0]):
        for j in range(noise1.shape[1]):
            rdn = random.random()
            if rdn < prob:
                noise1[i][j] = 0
            else:
                noise1[i][j] = noise1[i][j]

    rows,cols,chan = img.shape

    for y in range(rows):
        for x in range(cols):
            pixel = vert_img[y][x]
            pixel_n = noise[y][x]
            t = pixel+pixel_n
            top = any([True for j in t if j >=230])
            if top:
                vert_img[y,x] = [255,255,255]
            else:
                vert_img[y,x] = t 

    for y in range(rows):
        for x in range(cols):
            pixel = vert_img[y][x]
            pixel_1 = noise1[y][x]
            t = pixel-pixel_1
            top = any([True for j in t if j <=5])
            if top:
                vert_img[y,x] = [0,0,0]
            else:
                vert_img[y,x] = t 
    

    # contrast

    contrasted = vert_img*1.4
    contrasted = np.clip(contrasted, 0, 255)
    contrasted=contrasted.astype("uint8")

    
    # saturation
    saturation_weights = [0.70, 0.85, 1.0]
    saturated = np.zeros(contrasted.shape, contrasted.dtype)
    for y in range(contrasted.shape[0]):
        for x in range(contrasted.shape[1]):
            for c in range(contrasted.shape[2]):
                saturated[y,x,c] = saturation_weights[c] * np.clip(contrasted[y,x,c] - 50, 0, 255)


    #bulge
    with Image.from_array(saturated) as img:
        img.distort('shepards', (0,0, 0,0,  0,img.width, 0,img.width,  img.height,0, img.height,0,  img.height,img.width, img.height,img.width,  (img.width/8),(img.height/3), (img.width*3/8),(img.height/3)))
        bulged = np.array(img)
                

    cv2.imshow("test", bulged)
    while(cv2.waitKey()!=27):
        print("Press esc to exit")
