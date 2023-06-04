import cv2
import numpy as np
import glob
import os
 
img_array = []
files = glob.glob('/home/student/Downloads/face-distributed-main/main/output/*.jpg')
files.sort(key=os.path.getmtime)
for filename in files:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    print(filename) 
 
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 25, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
