
import os
from sys import platform
import cv2
import time





def averager(IMG):
    image = cv2.imread(IMG)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    val = 0
    for y in range(0, gray.shape[0], 2):
        r = []
        for x in range(0, gray.shape[1]):
            try:
                val += 100*(gray[y][x]/255)
                
                
            except:
                pass

    print(IMG, ":", val/(image.shape[0]*image.shape[1]))


for i in range(1,13):
    if len(str(i)) == 1:
        f = "ascii/0" + str(i) + ".png"
    else:
        f = "ascii/" + str(i) + ".png"
    averager(f)
