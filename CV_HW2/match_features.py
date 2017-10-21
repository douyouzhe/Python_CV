import cv2
import numpy as np
import matplotlib.pyplot as plt
import detect_features


def match_features(feature_coords1, feature_coords2, image1, image2):
    """
    Computer Vision 600.461/661 Assignment 2
    Args:
        feature_coords1 (list of tuples): list of (row,col) tuple feature coordinates from image1
        feature_coords2 (list of tuples): list of (row,col) tuple feature coordinates from image2
        image1 (numpy.ndarray): The input image corresponding to features_coords1
        image2 (numpy.ndarray): The input image corresponding to features_coords2
    Returns:
        matches (list of tuples): list of index pairs of possible matches. For example, if the 4-th feature in feature_coords1 and the 0-th feature
                                  in feature_coords2 are determined to be matches, the list should contain (4,0).
    """

    window_size = 10
    dict_feature1 = {}
    dict_feature2 = {}

    for i in feature_coords1:
        a = i[0] - window_size
        b = i[1] - window_size
        c = i[0] + window_size
        d = i[1] + window_size
        temp = image1[a:c, b:d]
        if (temp.shape != (window_size * 2, window_size * 2)):
            continue
        max_p = -1
        index = [0,0]

        for j in feature_coords2:
            a1 = j[0] - window_size
            b1 = j[1] - window_size
            c1 = j[0] + window_size
            d1 = j[1] + window_size
            temp1 = image2[a1:c1, b1:d1]

            if (temp1.shape != (window_size * 2, window_size * 2)):
                continue
            product = np.mean((temp - temp.mean()) * (temp1 - temp1.mean()))
            stds = temp.std() * temp1.std()
            product /= stds
            if max_p < product:
                max_p = product
                index = j

        dict_feature1[i] = index


    for i in feature_coords2:

        a = i[0] - window_size
        b = i[1] - window_size
        c = i[0] + window_size
        d = i[1] + window_size
        temp = image2[a:c, b:d]
        if (temp.shape != (window_size * 2, window_size * 2)):
            continue
        max_p = -1
        index = [0,0]
        for j in feature_coords1:
            a1 = j[0] - window_size
            b1 = j[1] - window_size
            c1 = j[0] + window_size
            d1 = j[1] + window_size
            temp1 = image1[a1:c1, b1:d1]
            if (temp1.shape != (window_size * 2, window_size * 2)):
                continue
            product = np.mean((temp - temp.mean()) * (temp1 - temp1.mean()))
            stds = temp.std() * temp1.std()
            product /= stds
            if max_p < product:
                max_p = product
                index = j
        dict_feature2[i] = index

    print dict_feature1
    print dict_feature2

    matches = list()
    arr = list()

    for i in dict_feature1.keys():
        temp = dict_feature1[i]
        if dict_feature2[temp] == i:
            index1 = feature_coords1.index(i)
            index2 = feature_coords2.index(temp)
            arr.append([index1,index2])
            matches.append(i)
            matches.append(temp)

    return matches, arr


pic = cv2.imread('bikes1.png')
out = detect_features.detect_features(pic)
gray = cv2.cvtColor(pic, cv2.COLOR_RGB2GRAY)

pic1 = cv2.imread('bikes2.png')
out1 = detect_features.detect_features(pic1)
gray1 = cv2.cvtColor(pic1, cv2.COLOR_RGB2GRAY)


results,arr = match_features(out, out1, gray, gray1)


print arr

newImage = np.concatenate((pic,pic1),axis= 1)
offset = pic1.shape[1]

for i in range(0,len(results),2):
    cv2.line(newImage,(results[i][1],results[i][0]),(results[i+1][1]+offset,results[i+1][0]),(255,0,0))
    cv2.circle(newImage,(results[i][1],results[i][0]),5,(0,255,0))
    cv2.circle(newImage, (results[i+1][1]+offset,results[i+1][0]), 5, (0, 255, 0))
cv2.imshow("test",newImage)
cv2.waitKey(0)