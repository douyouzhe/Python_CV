import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import nonmaxsuppts


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
    cornernessMat = np.zeros((row, col), np.float64)

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

    for i in range(1, row-1):
        for j in range(1,col-1):
            a = (gradMatCol[(i - 1):(i + 2), (j - 1):(j + 2)]**2).sum()
            c = (gradMatRow[(i - 1):(i + 2), (j - 1):(j + 2)]**2).sum()
            b = (gradMatCol[(i - 1):(i + 2), (j - 1):(j + 2)]\
            * gradMatRow[(i - 1):(i + 2), (j - 1):(j + 2)]).sum()

            #print a, b, c

            lambda1 = 1/2.0*(a+c+math.sqrt(b**2+(a-c)**2))
            lambda2 = 1 / 2.0 * (a + c - math.sqrt(b ** 2 + (a - c) ** 2))
            k = 0.05
            cornernessMat[i,j] = lambda1*lambda2 - k * (lambda1+lambda2)**2

    pixel_coords = nonmaxsuppts.nonmaxsuppts(cornernessMat,1,2053700411)

    return pixel_coords

pic = cv2.imread('bikes1.png')
out = detect_features(pic)