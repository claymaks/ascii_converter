"""
Converts digital images to ascii text documents
"""

__author__ = "Clayton Maksymiuk"
__copyright__ = ""
__credits__ = ["Clayton Maksymiuk", "Joshua Schember"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Clayton Maksymiuk"
__email__ = ["clayton.maksymiuk@fishrco.com, cmaks@umich.edu", "joshuaschember@gmail.com"]
__status__ = "Developement"

import os
from sys import platform
import cv2
import time




IMG = input("Image: ")
CONV = int(input("Scale Down:  "))

start = time.time()
#naming system for files
def check_file(fn, n):
    n1 = n
    if n > 0:
        fn = fn[0:-len(str(n-1))] + str(n)
    for _, _, files in os.walk('./'):
        for file in files:
            if '.' in file:
                if file == fn + ".png":
                    n += 1
    if n != n1:
        return check_file(fn, n)
    return fn

def average(a, b):
    return (a+b)/2

if platform == "linux" or platform == "linux2":
    fn = IMG.split("/")[-1].split(".")[0]
elif platform == "darwin":
    fn = IMG.split("/")[-1].split(".")[0]
elif platform == "win32":
    fn = IMG.split("\\")[-1].split(".")[0]






gray = cv2.cvtColor(cv2.imread(IMG), cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (gray.shape[1]//CONV, gray.shape[0]//CONV))


n = 0
fn += str(gray.shape[0]) + "x" + str(gray.shape[1]) + "-" + str(n)
fn = check_file(fn, n)



file = open((fn + ".txt"), "w")
for y in range(0, gray.shape[0], 2):
    for x in range(0, gray.shape[1]):
        try:
            val = average(int(gray[y][x]), int(gray[y+1][x]))
            if (val) > 242.25:
                file.write(' ')
            elif (val) > 109.65:
                file.write('·')
            elif (val) > 96.9:
                file.write('+')
            elif (val) > 66.3:
                file.write('#')
            elif (val) > 43.35:
                file.write('▒')
            elif (val) > 12.75:
                file.write('▓')
            else:
                file.write('█')
        
        except:
            pass
    file.write("\n")
file.close()
print(time.time() - start)
