import random
import cv2
import numpy as np
import copy
from skimage import data
from skimage import transform as tf
from skimage.color import rgb2gray
from skimage.feature import (match_descriptors, corner_harris,
                             corner_peaks, ORB, plot_matches)
import matplotlib.pyplot as plt
import match_features

pic1 = cv2.imread('hopkins1.JPG')
pic2 = cv2.imread('hopkins2.JPG')
pic1_gray= cv2.cvtColor(pic1.copy(), cv2.COLOR_RGB2GRAY)
pic2_gray= cv2.cvtColor(pic2.copy(), cv2.COLOR_RGB2GRAY)

descriptor_extractor = ORB(n_keypoints=200)

descriptor_extractor.detect_and_extract(pic1_gray)
keypoints1 = np.ndarray.astype(descriptor_extractor.keypoints,int)
descriptors1 = descriptor_extractor.descriptors
descriptor_extractor.detect_and_extract(pic2_gray)
keypoints2 = np.ndarray.astype(descriptor_extractor.keypoints,int)
descriptors2 = descriptor_extractor.descriptors
feature_coords1=[]
feature_coords2=[]
for i in range(len(keypoints1)):
    feature_coords1.append((keypoints1[i][0], keypoints1[i][1]))
for i in range(len(keypoints2)):
    feature_coords2.append((keypoints2[i][0], keypoints2[i][1]))
listInPairs = match_features.match_features(feature_coords1,feature_coords2,pic1,pic2)
# newImage = np.concatenate((pic1,pic2),axis= 1)
# offSet = pic1.shape[1]
# for i in listInPairs:
#     color = np.random.randint(0, 255, 3)
#     cv2.line(newImage,(feature_coords1[i[0]][1],feature_coords1[i[0]][0]),(feature_coords2[i[1]][1]+offSet,feature_coords2[i[1]][0]),(color))
#     cv2.circle(newImage,(feature_coords1[i[0]][1],feature_coords1[i[0]][0]),5,(color))
#     cv2.circle(newImage, (feature_coords2[i[1]][1]+offSet,feature_coords2[i[1]][0]), 5, (color))
# cv2.imshow('image',newImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

fundamental_matrix = np.zeros((3,3))


rnd = 1000
maxVote = 0
inliners = final = []
for n in range(rnd):
    samplesIndex = random.sample(range(0, len(listInPairs) - 1), 9)
    tmp1 = listInPairs[samplesIndex[0]]
    tmp2 = listInPairs[samplesIndex[1]]
    tmp3 = listInPairs[samplesIndex[2]]
    tmp4 = listInPairs[samplesIndex[3]]
    tmp5 = listInPairs[samplesIndex[4]]
    tmp6 = listInPairs[samplesIndex[5]]
    tmp7 = listInPairs[samplesIndex[6]]
    tmp8 = listInPairs[samplesIndex[7]]
    tmp9 = listInPairs[samplesIndex[8]]
    x11 = feature_coords1[tmp1[0]][1]
    y11 = feature_coords1[tmp1[0]][0]
    x21 = feature_coords1[tmp2[0]][1]
    y21 = feature_coords1[tmp2[0]][0]
    x31 = feature_coords1[tmp3[0]][1]
    y31 = feature_coords1[tmp3[0]][0]
    x41 = feature_coords1[tmp4[0]][1]
    y41 = feature_coords1[tmp4[0]][0]
    x51 = feature_coords1[tmp5[0]][1]
    y51 = feature_coords1[tmp5[0]][0]
    x61 = feature_coords1[tmp6[0]][1]
    y61 = feature_coords1[tmp6[0]][0]
    x71 = feature_coords1[tmp7[0]][1]
    y71 = feature_coords1[tmp7[0]][0]
    x81 = feature_coords1[tmp8[0]][1]
    y81 = feature_coords1[tmp8[0]][0]
    x91 = feature_coords1[tmp9[0]][1]
    y91 = feature_coords1[tmp9[0]][0]
    x12 = feature_coords2[tmp1[1]][1]
    y12 = feature_coords2[tmp1[1]][0]
    x22 = feature_coords2[tmp2[1]][1]
    y22 = feature_coords2[tmp2[1]][0]
    x32 = feature_coords2[tmp3[1]][1]
    y32 = feature_coords2[tmp3[1]][0]
    x42 = feature_coords2[tmp4[1]][1]
    y42 = feature_coords2[tmp4[1]][0]
    x52 = feature_coords2[tmp5[1]][1]
    y52 = feature_coords2[tmp5[1]][0]
    x62 = feature_coords2[tmp6[1]][1]
    y62 = feature_coords2[tmp6[1]][0]
    x72 = feature_coords2[tmp7[1]][1]
    y72 = feature_coords2[tmp7[1]][0]
    x82 = feature_coords2[tmp8[1]][1]
    y82 = feature_coords2[tmp8[1]][0]
    x92 = feature_coords2[tmp9[1]][1]
    y92 = feature_coords2[tmp9[1]][0]

    A = np.array([[x11*x12,x11*y12,x11,y11*x12,y11*y12,y11,x12,y12,1],
                  [x21*x22,x21*y22,x21,y21*x22,y21*y22,y21,x22,y22,1],
                  [x31*x32,x31*y32,x31,y31*x32,y31*y32,y31,x32,y32,1],
                  [x41*x42,x41*y42,x41,y41*x42,y41*y42,y41,x42,y42,1],
                  [x51*x52,x51*y52,x51,y51*x52,y51*y52,y51,x52,y52,1],
                  [x61*x62,x61*y62,x61,y61*x62,y61*y62,y61,x62,y62,1],
                  [x71*x72,x71*y72,x71,y71*x72,y71*y72,y71,x72,y72,1],
                  [x81*x82,x81*y82,x81,y81*x82,y81*y82,y81,x82,y82,1],
                  [x91*x92,x91*y92,x91,y91*x92,y91*y92,y91,x92,y92,1]])

    w, v = np.linalg.eig(np.dot(A.T, A))
    h = v.T[np.argmin(w)]  # or argmax???
    h = np.reshape(h, (3, 3))
    count = 0
    for pairs in listInPairs:
        x11Test = feature_coords1[pairs[0]][1]
        y11Test = feature_coords1[pairs[0]][0]
        x12Test = feature_coords2[pairs[1]][1]
        y12Test = feature_coords2[pairs[1]][0]
        tmp1 = np.array([[x12Test],
                      [y12Test],
                      [1]])
        tmp2 = np.array([[x11Test,y11Test,1]])
        if(np.dot(np.dot(tmp2,h),tmp1)<0.1):
            count+=1
            inliners.append(pairs)
    if (count>maxVote):
        print count
        maxVote = count
        fundamental_matrix = h
        final = copy.deepcopy(inliners)
    else:
        inliners[:] = []
print fundamental_matrix


for points in range(10):
    samplesIndex = random.sample(range(0, len(final) - 1), 1)
    tmp1 = final[samplesIndex[0]]
    x11 = feature_coords1[tmp1[0]][1]
    y11 = feature_coords1[tmp1[0]][0]
    # Ax + By + C = 0
    A = (x11*fundamental_matrix[0,0]+y11*fundamental_matrix[1,0]+fundamental_matrix[2,0])
    B = (x11*fundamental_matrix[0,1]+y11*fundamental_matrix[1,1]+fundamental_matrix[2,1])
    C = (x11*fundamental_matrix[0,2]+y11*fundamental_matrix[1,2]+fundamental_matrix[2,2])
    point1 = np.ndarray.astype(np.array([0,-C/B]),int)
    point2 = np.ndarray.astype(np.array([-C/A,0]),int)
    offSet = pic1.shape[1]
    color = np.random.randint(0, 255, 3)
    cv2.circle(pic1, (x11,y11), 5, (color))
    cv2.line(pic2,(point1[0],point1[1]),(point2[0],point2[1]),(color))
#cv2.imshow('image',newImage)
newImage = np.concatenate((pic1,pic2),axis= 1)
#cv2.imwrite("marks.JPG", newImage)
cv2.imshow('image',newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()




