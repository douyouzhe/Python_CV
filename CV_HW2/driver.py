import cv2
import numpy as np
import detect_features
import match_features
import compute_affine_xform
import compute_proj_xform

#edit here for new image pairs
# pic1 = cv2.imread('bikes1.png')
# pic2 = cv2.imread('bikes2.png')
# featureList1 = detect_features.detect_features(pic1,20,0.2)
# featureList2 = detect_features.detect_features(pic2,20,0.08)
# results,listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,20)

# pic1 = cv2.imread('bikes1.png')
# pic2 = cv2.imread('bikes3.png')
# featureList1 = detect_features.detect_features(pic1,20,0.2)
# featureList2 = detect_features.detect_features(pic2,20,0.08)
# results,listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,20)

# pic1 = cv2.imread('graf1.png')
# pic2 = cv2.imread('graf2.png')
# featureList1 = detect_features.detect_features(pic1,20,0.32)
# featureList2 = detect_features.detect_features(pic2,20,0.4)
# results,listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,20)

pic1 = cv2.imread('graf1.png')
pic2 = cv2.imread('graf3.png')
featureList1 = detect_features.detect_features(pic1,10,0.32)
featureList2 = detect_features.detect_features(pic2,10,0.4)
results,listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,20)

# pic1 = cv2.imread('leuven1.png')
# pic2 = cv2.imread('leuven2.png')
# featureList1 = detect_features.detect_features(pic1,20,0.25)
# featureList2 = detect_features.detect_features(pic2,20,0.2)
# results,listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,10)


###################################

#display image side by side and the matches
# newImage = np.concatenate((pic1,pic2),axis= 1)
# offSet = pic1.shape[1]
# for i in range(0,len(results),2):
#     cv2.line(newImage,(results[i][1],results[i][0]),(results[i+1][1]+offSet,results[i+1][0]),(255,0,0))
#     cv2.circle(newImage,(results[i][1],results[i][0]),5,(0,255,0))
#     cv2.circle(newImage, (results[i+1][1]+offSet,results[i+1][0]), 5, (0, 255, 0))
# cv2.imshow("test",newImage)
# cv2.waitKey(0)


# affineMat = compute_affine_xform.compute_affine_xform(listInPairs,featureList1,featureList2, pic1, pic2)
# print affineMat
# row,col = pic1.shape[:2]
# image2From1 = cv2.warpAffine(pic1,affineMat,(col, row))
# newImage = np.concatenate((image2From1,pic2),axis= 1)
# cv2.imshow("test",newImage)
# cv2.waitKey(0)

projMat = compute_proj_xform.compute_proj_xform(listInPairs,featureList1,featureList2, pic1, pic2)
row,col = pic1.shape[:2]
image2From1 = cv2.warpPerspective(pic1,projMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imshow("test",newImage)
cv2.waitKey(0)