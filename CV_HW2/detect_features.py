import cv2
import numpy as np
import math
import matplotlib.pyplot as plt



def detect_features(image):
    """
    Computer Vision 600.461/661 Assignment 2
    Args:
        image (numpy.ndarray): The input image to detect features on. Note: this is NOT the image name or image path.
    Returns:
        pixel_coords (list of tuples): A list of (row,col) tuples of detected feature locations in the image
    """
    pixel_coords = list()
    imgNew = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    row, col = imgNew.shape
    gradMatRow = np.zeros((row, col), np.float64)
    gradMatCol = np.zeros((row, col), np.float64)

    for i in range(1,row-1):
        for j in range(1,col-1):
            gradMatRow[i,j] = (imgNew[i + 1, j] - imgNew[i - 1, j])/2.0
            gradMatCol[i,j] = (imgNew[i,j+1]-imgNew[i,j-1])/2.0
    for i in range(1,row-1):
        gradMatCol[i,0] = imgNew[i,1]-imgNew[i,0]
        gradMatCol[i, col-1] = imgNew[i, col-1] - imgNew[i, col-2]
        gradMatRow[i, 0] = (imgNew[i + 1, 0] - imgNew[i - 1, 0]) / 2.0
    for j in range(1,col-1):
        gradMatRow[0, j] = imgNew[1, j]-imgNew[0, j]
        gradMatRow[row-1, j] = imgNew[row-1, j] - imgNew[row-2, j]
        gradMatCol[0, j] = (imgNew[0, j + 1] - imgNew[0, j - 1]) / 2.0

    gradMatRow[0, 0] = imgNew[1, 0] - imgNew[0, 0]
    gradMatRow[row - 1, 0] = imgNew[row - 1, 0] - imgNew[row - 2, 0]
    gradMatRow[0, col - 1] = imgNew[1, col - 1] - imgNew[0, col - 1]
    gradMatRow[row - 1, col - 1] = imgNew[row - 1, col - 1] - imgNew[row - 2, col - 1]
    gradMatCol[0, 0] = imgNew[0, 1] - imgNew[0, 0]
    gradMatCol[row - 1, 0] = imgNew[row - 1, 1] - imgNew[row - 1, 0]
    gradMatCol[0, col - 1] = imgNew[0, col - 2] - imgNew[0, col - 1]
    gradMatCol[row - 1, col - 1] = imgNew[row - 1, col - 1] - imgNew[row - 1, col - 2]

    for i in range(row-1):
        for j in range(col-1):
            H = np.zeros((2,2),np.float64)
            H[0, 0] = gradMatCol[i, j] ** 2
            H[0, 1] = gradMatCol[i, j] * gradMatRow[i, j]
            H[1, 0] = gradMatCol[i, j] * gradMatRow[i, j]
            H[1, 1] = gradMatRow[i, j] ** 2
            print H
            print ((H[0, 0] + H[1,1]))
            print math.sqrt(4*H[1,0]*H[0,1]+(H[0,0]-H[1,1])**2)

            EigenVal = 1/2.0*((H[0, 0]+H[1,1])-math.sqrt(4*H[1,0]*H[0,1]+(H[0,0]-H[1,1])**2))
            #print EigenVal







    return pixel_coords

pic = cv2.imread('bikes1.png')
out = detect_features(pic)