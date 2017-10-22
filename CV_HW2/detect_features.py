import cv2
import numpy as np
import nonmaxsuppts


def detect_features(image, nonmaxsupptsRadius, nonmaxsupptsThreshold):
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
    sobelRow = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    gradMatCol = cv2.filter2D(src = imgNew, ddepth = cv2.CV_64F, kernel = sobelCol)
    gradMatRow = cv2.filter2D(src = imgNew, ddepth = cv2.CV_64F, kernel = sobelRow)
    Ixx = gradMatCol**2
    Iyy = gradMatRow**2
    Ixy = gradMatCol*gradMatRow

    cornernessMat = np.zeros((row, col), np.float64)
    for y in range(1, row - 1):
        for x in range(1, col - 1):
            Sxx = Ixx[y - 1:y + 1 + 1, x - 1:x + 1 + 1].sum()
            Sxy = Ixy[y - 1:y + 1 + 1, x - 1:x + 1 + 1].sum()
            Syy = Iyy[y - 1:y + 1 + 1, x - 1:x + 1 + 1].sum()
            det = (Sxx * Syy) - (Sxy ** 2)
            cornernessMat[y,x] = det - 0.04 * ((Sxx + Syy) ** 2)

    maxVal = np.max(cornernessMat)
    pixel_coords = nonmaxsuppts.nonmaxsuppts(cornernessMat,
                                             nonmaxsupptsRadius,nonmaxsupptsThreshold*maxVal)
    print len(pixel_coords)

    for ls in pixel_coords:
        image.itemset((ls[0], ls[1], 0), 0)
        image.itemset((ls[0], ls[1], 1), 0)
        image.itemset((ls[0], ls[1], 2), 255)
    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    return pixel_coords
# pic = cv2.imread('graf1.png')
# out = detect_features(pic)