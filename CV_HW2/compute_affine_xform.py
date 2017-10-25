# Author: TK
import cv2
import numpy as np
import random
from numpy.linalg import inv
import copy
import matplotlib.pyplot as plt

def compute_affine_xform(matches,features1,features2,image1,image2):
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
        affine_xform (numpy.ndarray): a 3x3 Affine transformation matrix between the two images, computed using the matches.
    """

    affine_xform = np.zeros((2,3))
    rnd = 1000
    maxVote = 0
    inliners = final = []
    for n in range(rnd):
        samplesIndex = random.sample(range(0, len(matches) - 1), 3)
        tmp1 = matches[samplesIndex[0]]
        tmp2 = matches[samplesIndex[1]]
        tmp3 = matches[samplesIndex[2]]
        x11 = features1[tmp1[0]][1]
        y11 = features1[tmp1[0]][0]
        x21 = features1[tmp2[0]][1]
        y21 = features1[tmp2[0]][0]
        x31 = features1[tmp3[0]][1]
        y31 = features1[tmp3[0]][0]
        x12 = features2[tmp1[1]][1]
        y12 = features2[tmp1[1]][0]
        x22 = features2[tmp2[1]][1]
        y22 = features2[tmp2[1]][0]
        x32 = features2[tmp3[1]][1]
        y32 = features2[tmp3[1]][0]
        A = np.array([[x11,y11,1,0,0,0],
                      [0,0,0,x11,y11,1],
                      [x21,y21,1,0,0,0],
                      [0,0,0,x21,y21,1],
                      [x31,y31,1,0,0,0],
                      [0,0,0,x31,y31,1]])
        b = np.array([[x12],
                      [y12],
                      [x22],
                      [y22],
                      [x32],
                      [y32]])
        AT = A.transpose()
        ATA = np.dot(AT,A)
        ATAAT = np.dot(inv(ATA),AT)
        t = np.dot(ATAAT,b)
        count = 0
        for pairs in matches:
            x11Test = features1[pairs[0]][1]
            y11Test = features1[pairs[0]][0]
            x12Test = features2[pairs[1]][1]
            y12Test = features2[pairs[1]][0]
            tmp1 = (t[0]*x11Test+t[1]*y11Test+t[2]-x12Test)**2
            tmp2 = (t[3]*x11Test+t[4]*y11Test+t[5]-y12Test)**2
            if(tmp1<1 and tmp2<1):
                count+=1
                inliners.append(pairs)
        if(count>maxVote):
            maxVote = count
            affine_xform = t.reshape(2,3)
            final = copy.deepcopy(inliners)
        else:
            inliners[:] = []
    return affine_xform, final
