import cv2
import numpy as np
import detect_features

def match_features(feature_coords1, feature_coords2, image1, image2, windowSize):
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

    windowSize = windowSize
    dictFeature2To1 = {}
    dictFeature1To2 = {}
    image1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)

    for i in feature_coords1:
        windowIn1 = image1[i[0] - windowSize:i[0] + windowSize, i[1] - windowSize:i[1] + windowSize]
        if (windowIn1.shape != (windowSize * 2, windowSize * 2)): continue
        maxVal = -1
        index = [0,0]
        for j in feature_coords2:
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
        windowIn2 = image2[i[0] - windowSize:i[0] + windowSize, i[1] - windowSize:i[1] + windowSize]
        if (windowIn2.shape != (windowSize * 2, windowSize * 2)):continue
        maxVal = -1
        index = [0,0]
        for j in feature_coords1:
            windowIn1 = image1[j[0] - windowSize:j[0] + windowSize, j[1] - windowSize:j[1] + windowSize]
            if (windowIn1.shape != (windowSize * 2, windowSize * 2)):continue
            product = np.mean((windowIn2 - windowIn2.mean()) * (windowIn1 - windowIn1.mean()))
            stds = windowIn2.std() * windowIn1.std()
            product /= stds
            if maxVal < product:
                maxVal = product
                index = j
        dictFeature1To2[i] = index

    # print dictFeature2To1
    # print dictFeature1To2

    matches = list()
    listInPairs = list()
    for i in dictFeature2To1.keys():
        temp = dictFeature2To1[i]
        if dictFeature1To2[temp] == i:
            index1 = feature_coords1.index(i)
            index2 = feature_coords2.index(temp)
            listInPairs.append([index1,index2])
            matches.append(i)
            matches.append(temp)

    return matches, listInPairs
