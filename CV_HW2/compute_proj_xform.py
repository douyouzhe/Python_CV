# Author: TK
import cv2
import numpy as np
import random
from numpy.linalg import inv
from numpy import linalg as LA
import matplotlib.pyplot as plt

def compute_proj_xform(matches,features1,features2,image1,image2):
    """
    Computer Vision 600.461/661 Assignment 2
    Args:
        matches (list of tuples): list of index pairs of possible matches. For example, if the 4-th feature in feature_coords1 and the 0-th feature
                                  in feature_coords2 are determined to be matches, the list should contain (4,0).
        features1 (list of tuples) : list of feature coordinates corresponding to image1
        features2 (list of tuples) : list of feature coordinates corresponding to image2
        image1 (numpy.ndarray): The input image corresponding to features_coords1
        image2 (numpy.ndarray): The input image corresponding to features_coords2
    Returns:
        proj_xform (numpy.ndarray): a 3x3 Projective transformation matrix between the two images, computed using the matches.
    """
    
    proj_xform = np.zeros((3,3))
    threeSamplesIn1 = np.zeros((3,3))
    threeSamplesIn2 = np.zeros((3,3))
    rnd = 10000
    maxVote = 0
    for n in range(rnd):
        correspondences = []
        samplesIndex = random.sample(range(0, len(matches) - 1), 4)
        tmp1 = matches[samplesIndex[0]]
        tmp2 = matches[samplesIndex[1]]
        tmp3 = matches[samplesIndex[2]]
        tmp4 = matches[samplesIndex[3]]
        x11 = features1[tmp1[0]][1]
        y11 = features1[tmp1[0]][0]
        x21 = features1[tmp2[0]][1]
        y21 = features1[tmp2[0]][0]
        x31 = features1[tmp3[0]][1]
        y31 = features1[tmp3[0]][0]
        x41 = features1[tmp4[0]][1]
        y41 = features1[tmp4[0]][0]
        x12 = features2[tmp1[1]][1]
        y12 = features2[tmp1[1]][0]
        x22 = features2[tmp2[1]][1]
        y22 = features2[tmp2[1]][0]
        x32 = features2[tmp3[1]][1]
        y32 = features2[tmp3[1]][0]
        x42 = features2[tmp4[1]][1]
        y42 = features2[tmp4[1]][0]
        correspondences.append([x11, y11, x12, y12])
        correspondences.append([x21, y21, x22, y22])
        correspondences.append([x31, y31, x32, y32])
        correspondences.append([x41, y41, x42, y42])
        aList = []
        for corr in correspondences:
            p1 = np.matrix([corr[0], corr[1], 1])
            p2 = np.matrix([corr[2], corr[3], 1])
            a2 = [0, 0, 0, -p2.item(2) * p1.item(0), -p2.item(2) * p1.item(1), -p2.item(2) * p1.item(2),
                  p2.item(1) * p1.item(0), p2.item(1) * p1.item(1), p2.item(1) * p1.item(2)]
            a1 = [-p2.item(2) * p1.item(0), -p2.item(2) * p1.item(1), -p2.item(2) * p1.item(2), 0, 0, 0,
                  p2.item(0) * p1.item(0), p2.item(0) * p1.item(1), p2.item(0) * p1.item(2)]
            aList.append(a1)
            aList.append(a2)
        A = np.matrix(aList)
        w, v = np.linalg.eig(np.dot(A.T, A))
        h = v.T[np.argmin(w)]
        h = np.reshape(h, (3, 3))
        h = (1 / h.item(8)) * h
        count = 0
        for pairs in matches:
            x11Test = features1[pairs[0]][1]
            y11Test = features1[pairs[0]][0]
            x12Test = features2[pairs[1]][1]
            y12Test = features2[pairs[1]][0]
            den = h[2,0]*x11Test+h[2,1]*y11Test+h[2,2]
            tmp1 = ((h[0,0]*x11Test+h[0,1]*y11Test+h[0,2])/den-x12Test)**2
            tmp2 = ((h[1,0]*x11Test+h[1,1]*y11Test+h[1,2])/den-y12Test)**2
            if(tmp1<1 and tmp2<1): count+=1
        if (count > maxVote):
            maxVote = count
            proj_xform = h
    return proj_xform
