import cv2
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(threshold=np.nan)
def conv(x,h_x,h_y):
    g_x = [[0] * len(x[0]) for row in range(len(x))]
    g_y=[[0] * len(x[0]) for row in range(len(x))]
    for i in range(3,4):
        for j in range(3,4):

            print i
            print j
            print x[i-1,j-1,0]*h_x[0][0]+x[i,j-1,0]*h_x[1][0]+x[i+1,j-1,0]*h_x[2][0]+ x[i-1,j,0]*h_x[0][1]+x[i,j,0]*h_x[1][1]+x[i+1,j,0]*h_x[2][1]+ x[i-1,j+1,0]*h_x[0][2]+x[i,j+1,0]*h_x[1][2]+x[i+1,j+1,0]*h_x[2][2]
            print x[i-1,j-1,0]*h_y[0][0]+x[i,j-1,0]*h_y[1][0]+x[i+1,j-1,0]*h_y[2][0]+ x[i-1,j,0]*h_y[0][1]+x[i,j,0]*h_y[1][1]+x[i+1,j,0]*h_y[2][1]+ x[i-1,j+1,0]*h_y[0][2]+x[i,j+1,0]*h_y[1][2]+x[i+1,j+1,0]*h_y[2][2]

    return g_x,g_y
x = cv2.imread('hough_simple_2.pgm')
#im = cv2.GaussianBlur(im,(15,15),0)
h_x=[[-1,0,1],[-2,0,2],[-1,0,1]]
h_y=[[1,2,1],[0,0,0],[-1,-2,-1]]
g_x,g_y=conv(x,h_x,h_x)

i=3
j=3
print x[i - 1:i + 2, j - 1:j + 2,0]
print x[i-1,j-1,0]*h_x[0][0]+x[i,j-1,0]*h_x[1][0]+x[i+1,j-1,0]*h_x[2][0]+ x[i-1,j,0]*h_x[0][1]+x[i,j,0]*h_x[1][1]+x[i+1,j,0]*h_x[2][1]+ x[i-1,j+1,0]*h_x[0][2]+x[i,j+1,0]*h_x[1][2]+x[i+1,j+1,0]*h_x[2][2]
print x[i-1,j-1,0]*h_y[0][0]+x[i,j-1,0]*h_y[1][0]+x[i+1,j-1,0]*h_y[2][0]+ x[i-1,j,0]*h_y[0][1]+x[i,j,0]*h_y[1][1]+x[i+1,j,0]*h_y[2][1]+ x[i-1,j+1,0]*h_y[0][2]+x[i,j+1,0]*h_y[1][2]+x[i+1,j+1,0]*h_y[2][2]


#print x[i-1,j-1,0]*h_x[0][0]+x[i,j-1,0]*h_x[1][0]+x[i+1,j-1,0]*h_x[2][0]+ x[i-1,j,0]*h_x[0][1]+x[i,j,0]*h_x[1][1]+x[i+1,j,0]*h_x[2][1]+ x[i-1,j+1,0]*h_x[0][2]+x[i,j+1,0]*h_x[1][2]+x[i+1,j+1,0]*h_x[2][2]


