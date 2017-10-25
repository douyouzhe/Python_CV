import random
import cv2
import numpy as np
import sys
import detect_features
import match_features
import compute_affine_xform
import compute_proj_xform
import ssift_descriptor

def ratio_test (descriptor1 , descriptor2):
    a = descriptor1
    b = descriptor2
    dic = {}
    dic2Min = {}
    for i in a:
        min = secondMin= sys.maxint
        dic[i] = 0,0
        for j in b:
            dist = ((a[i]-b[j])**2).sum()
            if(dist< min):
                secondMin = min
                dic2Min[i] = dic[i]
                min = dist
                dic[i] = j
            elif ((dist<secondMin) and (dist!=min)):
                    secondMin = dist
                    dic2Min[i] = j
    for i in dic:
        dist1 = ((a[i] - b[dic[i]]) ** 2).sum()
        dist2 = ((a[i] - b[dic2Min[i]]) ** 2).sum()
        if(dist1/dist2)>0.5:
            dic[i] = 0

    return dic