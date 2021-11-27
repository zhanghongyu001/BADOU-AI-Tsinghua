import cv2
import numpy as np
def fc (img):
    height,width,channles = img.shape
    image1 =np.zeros((1000,1000,channles),np.uint8)
    h = 1000/height
    w = 1000/width
    for i in range(1000):
        for j in range(1000):
            x=int(i/h)
            y=int(j/w)
            image1[i,j]=img[x,y]
    return image1

img =cv2.imread('lenna.png')
pic=fc(img)
print(pic)
print(pic.shape)
cv2.imshow('change',pic)
cv2.imshow('ori',img)
cv2.waitKey(0)