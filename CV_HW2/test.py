import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
# pic = cv2.imread('graf1.png')
# imgNew = cv2.cvtColor(pic, cv2.COLOR_RGB2GRAY)
#
# dst = cv2.cornerHarris(imgNew,2,3,0.04)
# pic[dst>0.01*dst.max()]=[0,0,255]
#
# cv2.imshow('image', pic)
# cv2.waitKey(0)



import numpy
from scipy.ndimage import filters



def harris(image, sigma_d=1.0, sigma_i=1.5, count=512):

    image = image.astype(numpy.float32)
    h, w = image.shape[0:2]

    # compute image derivatives
    Ix = filters.gaussian_filter1d(image, sigma_d, 0, 0)
    Ix = filters.gaussian_filter1d(Ix, sigma_d, 1, 1)
    Iy = filters.gaussian_filter1d(image, sigma_d, 1, 0)
    Iy = filters.gaussian_filter1d(Iy, sigma_d, 0, 1)

    # compute elements of the structure tensor
    Ixx = filters.gaussian_filter(Ix**2, sigma_i, 0)
    Iyy = filters.gaussian_filter(Iy**2, sigma_i, 0)
    Ixy = filters.gaussian_filter(Ix * Iy, sigma_i, 0)

    # compute Harris feature strength, avoiding divide by zero
    imgH = (Ixx * Iyy - Ixy**2) / (Ixx + Iyy + 1e-8)

    # exclude points near the image border
    imgH[:16, :] = 0
    imgH[-16:, :] = 0
    imgH[:, :16] = 0
    imgH[:, -16:] = 0

    # non-maximum suppression in 5x5 regions
    maxH = filters.maximum_filter(imgH, (5,5))
    imgH = imgH * (imgH == maxH)

    # sort points by strength and find their positions
    sortIdx = numpy.argsort(imgH.flatten())[::-1]
    sortIdx = sortIdx[:count]
    yy = sortIdx / w
    xx = sortIdx % w

    # concatenate positions and values
    xyv = numpy.vstack((xx, yy, imgH.flatten()[sortIdx])).transpose()

    return xyv


if __name__ == "__main__":
    pic = cv2.imread('graf1.png')
    imgNew = cv2.cvtColor(pic, cv2.COLOR_RGB2GRAY)

    pts = harris(imgNew[:,:])
    pic[pts[3]>0.01*pts[3].max()]=[0,0,255]

    cv2.imshow('image', pic)
    cv2.waitKey(0)