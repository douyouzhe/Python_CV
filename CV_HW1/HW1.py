import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
result = cv2.imread("hough_simple_2.pgm")
im=cv2.imread("hough_image_2_result.pgm")
line=[]
for i in xrange(1,len(im)-1):
    for j in xrange(1,len(im[0])-1):
        a=im[i,j,0]
            #(int(im[i-1,j-1,0])+int(im[i-1,j,0])+int(im[i-1,j+1,0])+int(im[i,j-1,0])+int(im[i,j,0])+int(im[i,j+1,0])+int(im[i+1,j-1,0])+int(im[i+1,j,0])+int(im[i+1,j+1,0]))/9.0
        if a>250:
            line.append((i,j))
for i in line:
    rho = i[1]
    theta = np.pi*(i[0])/360
    print rho,math.degrees(theta)
    if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):
        pt1 = (int(rho / np.cos(theta)), 0)
        pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])
        cv2.line(result, pt1, pt2, (255))
    else:
        pt1 = (0, int(rho / np.sin(theta)))
        pt2 = (result.shape[1], int((rho - result.shape[1] * np.cos(theta)) / np.sin(theta)))
        cv2.line(result, pt1, pt2, (255), 1)
plt.imshow(result)
plt.show()