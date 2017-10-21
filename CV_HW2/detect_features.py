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
    imgNew = image.copy()
    imgNew = cv2.cvtColor(imgNew, cv2.COLOR_RGB2GRAY)
    row, col = imgNew.shape
    imgNew = cv2.GaussianBlur(imgNew, (5,5), 0)

    # self-implement np.gradient
    # gradMatRow = np.zeros((row, col), np.float64)
    # gradMatCol = np.zeros((row, col), np.float64)
    # cornernessMat = np.zeros((row, col), np.float64)
    # for i in range(1,row-1):
    #     for j in range(1,col-1):
    #         gradMatRow[i,j] = (imgNew[i + 1, j] - imgNew[i - 1, j])/2.0
    #         gradMatCol[i,j] = (imgNew[i,j+1]-imgNew[i,j-1])/2.0
    # for i in range(1,row-1):
    #     gradMatCol[i,0] = imgNew[i,1]-imgNew[i,0]
    #     gradMatCol[i, col-1] = imgNew[i, col-1] - imgNew[i, col-2]
    #     gradMatRow[i, 0] = (imgNew[i + 1, 0] - imgNew[i - 1, 0]) / 2.0
    # for j in range(1,col-1):
    #     gradMatRow[0, j] = imgNew[1, j]-imgNew[0, j]
    #     gradMatRow[row-1, j] = imgNew[row-1, j] - imgNew[row-2, j]
    #     gradMatCol[0, j] = (imgNew[0, j + 1] - imgNew[0, j - 1]) / 2.0
    # gradMatRow[0, 0] = imgNew[1, 0] - imgNew[0, 0]
    # gradMatRow[row - 1, 0] = imgNew[row - 1, 0] - imgNew[row - 2, 0]
    # gradMatRow[0, col - 1] = imgNew[1, col - 1] - imgNew[0, col - 1]
    # gradMatRow[row - 1, col - 1] = imgNew[row - 1, col - 1] - imgNew[row - 2, col - 1]
    # gradMatCol[0, 0] = imgNew[0, 1] - imgNew[0, 0]
    # gradMatCol[row - 1, 0] = imgNew[row - 1, 1] - imgNew[row - 1, 0]
    # gradMatCol[0, col - 1] = imgNew[0, col - 2] - imgNew[0, col - 1]
    # gradMatCol[row - 1, col - 1] = imgNew[row - 1, col - 1] - imgNew[row - 1, col - 2]
    #gradMatRow,gradMatCol = np.gradient(imgNew)
    sobelCol = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    sobelRow = np.array([[-1, -2, -1], [0,0,0], [1, 2,1]])

    gradMatCol = cv2.filter2D(src = imgNew, ddepth = cv2.CV_64F, kernel = sobelCol)
    gradMatRow = cv2.filter2D(src = imgNew, ddepth = cv2.CV_64F, kernel = sobelRow)
    Ixx = gradMatCol**2
    Iyy = gradMatRow**2
    Ixy = gradMatCol*gradMatRow
    offset = int(3 / 2)

    cornernessMat = np.zeros((row, col), np.float64)
    for y in range(offset, row - offset):
        for x in range(offset, col - offset):
            windowIxx = Ixx[y - offset:y + offset + 1, x - offset:x + offset + 1]
            windowIxy = Ixy[y - offset:y + offset + 1, x - offset:x + offset + 1]
            windowIyy = Iyy[y - offset:y + offset + 1, x - offset:x + offset + 1]
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()
            det = (Sxx * Syy) - (Sxy ** 2)
            trace = Sxx + Syy
            cornernessMat[y,x] = det - 0.04 * (trace ** 2)



    # cornernessMat = np.zeros((row, col), np.float64)
    # for i in range(1, row-1):
    #     for j in range(1,col-1):
    #         a = (gradMatCol[(i - 1):(i + 2), (j - 1):(j + 2)]**2).sum()
    #         c = (gradMatRow[(i - 1):(i + 2), (j - 1):(j + 2)]**2).sum()
    #         b = (gradMatCol[(i - 1):(i + 2), (j - 1):(j + 2)]\
    #         * gradMatRow[(i - 1):(i + 2), (j - 1):(j + 2)]).sum()
    #         lambda1 = 1/2.0*(a+c+math.sqrt(b**2+(a-c)**2))
    #         lambda2 = 1 / 2.0 * (a + c - math.sqrt(b ** 2 + (a - c) ** 2))
    #         k = 0.05
    #         cornernessMat[i,j] = lambda1*lambda2 - k * (lambda1+lambda2)**2
    #

    maxVal = np.max(cornernessMat)
    pixel_coords = nonmaxsuppts.nonmaxsuppts(cornernessMat,5,0.15*maxVal)
    print len(pixel_coords)

    for ls in pixel_coords:
        #cv2.circle(img=image, center=(ls[1],ls[0]), radius=5, color=(0, 0, 255))
        image.itemset((ls[0], ls[1], 0), 0)
        image.itemset((ls[0], ls[1], 1), 0)
        image.itemset((ls[0], ls[1], 2), 255)
    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    return pixel_coords
# pic = cv2.imread('graf1.png')
# out = detect_features(pic)