import numpy as np
import cv2
from sys import platform
import os


img = input("Image: ")
CONV = int(input("Scale Down:  "))


#naming system for files
def check_file(fn, n):
    n1 = n
    if n > 0:
        fn = fn[0:-len(str(n-1))] + str(n)
    for subdir, dirs, files in os.walk('./'):
        for file in files:
            if '.' in file:
                if file == fn + ".png":
                    n += 1
    if n != n1:
        return check_file(fn, n)
    return fn
        
def average(a,b):
    return (a+b)/2

if platform == "linux" or platform == "linux2":
    fn = img.split("/")[-1].split(".")[0]
elif platform == "darwin":
    fn = img.split("/")[-1].split(".")[0]
elif platform == "win32":
    fn = img.split("\\")[-1].split(".")[0]





image = cv2.imread(img)
arog = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (gray.shape[1]//CONV, gray.shape[0]//CONV))

n = 0
fn += str(gray.shape[0]) + "x" + str(gray.shape[1]) + "-" + str(n)
fn = check_file(fn, n)



#cv2.imshow("Gray", gray)
cv2.imwrite((fn + ".png"),gray)

c = []
val = ' '
for y in range(0, gray.shape[0], 2):
    r = []
    for x in range(0, gray.shape[1]):
        try:
            if (average(gray[y][x]/255,gray[y+1][x]/255)) > .9:
                val = ' '
            elif (average(gray[y][x]/255,gray[y+1][x]/255)) > .8:
                val = '·'
            elif (average(gray[y][x]/255,gray[y+1][x]/255)) > .7:
                val = '-'
            elif (average(gray[y][x]/255,gray[y+1][x]/255)) > .6:
                val = '='
            elif (average(gray[y][x]/255,gray[y+1][x]/255)) > .5:
                val = '+'
            elif (average(gray[y][x]/255,gray[y+1][x]/255)) > .4:
                val = '#'
            elif (average(gray[y][x]/255,gray[y+1][x]/255)) > .3:
                val = '▒'
            elif (average(gray[y][x]/255,gray[y+1][x]/255)) > .2:
                val = '▓'
            else:
                val = '█'
        
            r.append(val)
        except:
            pass
    c.append(r)




file = open((fn + ".txt"), "w")

for y in range(0, gray.shape[0]//2):
    for x in range(0, gray.shape[1]):
        file.write(c[y][x])
    file.write("\n")
file.close()

    


