import cv2
import numpy as np
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

    windowSize = 10
    dictFeature2To1 = {}
    dictFeature1To2 = {}

    for i in feature_coords1:
        # a = i[0] - windowSize
        # b = i[1] - windowSize
        # c = i[0] + windowSize
        # d = i[1] + windowSize
        windowIn1 = image1[i[0] - windowSize:i[0] + windowSize, i[1] - windowSize:i[1] + windowSize]
        if (windowIn1.shape != (windowSize * 2, windowSize * 2)): continue
        maxVal = -1
        index = [0,0]
        for j in feature_coords2:
            # a1 = j[0] - windowSize
            # b1 = j[1] - windowSize
            # c1 = j[0] + windowSize
            # d1 = j[1] + windowSize
            windowIn2 = image2[j[0] - windowSize:j[0] + windowSize, j[1] - windowSize:j[1] + windowSize]
            if (windowIn2.shape != (windowSize * 2, windowSize * 2)): continue
            product = np.mean((windowIn1 - windowIn1.mean()) * (windowIn2 - windowIn2.mean()))
            stds = windowIn1.std() * windowIn2.std()
            product /= stds
            if maxVal < product:
                maxVal = product
                index = j
        dictFeature2To1[i] = index


    for i in feature_coords2:
        # a = i[0] - windowSize
        # b = i[1] - windowSize
        # c = i[0] + windowSize
        # d = i[1] + windowSize
        windowIn2 = image2[i[0] - windowSize:i[0] + windowSize, i[1] - windowSize:i[1] + windowSize]
        if (windowIn2.shape != (windowSize * 2, windowSize * 2)):continue
        maxVal = -1
        index = [0,0]
        for j in feature_coords1:
            # a1 = j[0] - windowSize
            # b1 = j[1] - windowSize
            # c1 = j[0] + windowSize
            # d1 = j[1] + windowSize
            windowIn1 = image1[j[0] - windowSize:j[0] + windowSize, j[1] - windowSize:j[1] + windowSize]
            if (windowIn1.shape != (windowSize * 2, windowSize * 2)):continue
            product = np.mean((windowIn2 - windowIn2.mean()) * (windowIn1 - windowIn1.mean()))
            stds = windowIn2.std() * windowIn1.std()
            product /= stds
            if maxVal < product:
                maxVal = product
                index = j
        dictFeature1To2[i] = index

    print dictFeature2To1
    print dictFeature1To2

    matches = list()
    arr = list()

    for i in dictFeature2To1.keys():
        temp = dictFeature2To1[i]
        if dictFeature1To2[temp] == i:
            index1 = feature_coords1.index(i)
            index2 = feature_coords2.index(temp)
            arr.append([index1,index2])
            matches.append(i)
            matches.append(temp)

    return matches, arr


pic = cv2.imread('bikes1.png')
out = detect_features.detect_features(pic,20,0.2)
gray = cv2.cvtColor(pic, cv2.COLOR_RGB2GRAY)

pic1 = cv2.imread('bikes2.png')
out1 = detect_features.detect_features(pic1,20,0.2)
gray1 = cv2.cvtColor(pic1, cv2.COLOR_RGB2GRAY)


results,arr = match_features(out, out1, gray, gray1)


newImage = np.concatenate((pic,pic1),axis= 1)
offset = pic1.shape[1]

for i in range(0,len(results),2):
    cv2.line(newImage,(results[i][1],results[i][0]),(results[i+1][1]+offset,results[i+1][0]),(255,0,0))
    cv2.circle(newImage,(results[i][1],results[i][0]),5,(0,255,0))
    cv2.circle(newImage, (results[i+1][1]+offset,results[i+1][0]), 5, (0, 255, 0))
cv2.imshow("test",newImage)
cv2.waitKey(0)