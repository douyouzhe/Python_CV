import random
import cv2
import numpy as np
import sys
import detect_features

import match_features
import compute_affine_xform
import compute_proj_xform
import ratio_test
import ssift_descriptor

#edit here for different image pairs
#bikes1 <-> bikes2
pic1 = cv2.imread('bikes1.png')
pic2 = cv2.imread('bikes2.png')
featureList1 = detect_features.detect_features(pic1,20,0.1)
featureList2 = detect_features.detect_features(pic2,20,0.04)
pic1tmp = pic1.copy()
pic2tmp = pic2.copy()
for i in featureList1:
    color = (0, 0, 255)
    cv2.circle(pic1tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/bikes1_2/bikes1_features.pgm", pic1tmp)
for i in featureList2:
    color = (0, 0, 255)
    cv2.circle(pic2tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/bikes1_2/bikes2_features.pgm", pic2tmp)
listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,20)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in listInPairs:
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(color))
    cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(color))
    cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (color))
cv2.imwrite("output_images/bikes1_2/bikes1&2_matched_features.pgm", newImage)
affineMat, inliners= compute_affine_xform.compute_affine_xform(listInPairs,featureList1,featureList2, pic1, pic2)
for i in listInPairs:
    if i in inliners:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(255,0,0))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(255,0,0))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (255,0,0))
    else:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(0,0,255))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(0,0,255))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (0,0,255))
cv2.imwrite("output_images/bikes1_2/bikes1&2_inliners_outliners.pgm", newImage)
row,col = pic1.shape[:2]
image2From1 = cv2.warpAffine(pic1,affineMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/bikes1_2/bikes1&2_affine_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5*pic2
cv2.imwrite("output_images/bikes1_2/bikes1&2_stitch_affine_result.pgm", newImage)
projMat = compute_proj_xform.compute_proj_xform(listInPairs,featureList1,featureList2, pic1, pic2)
image2From1 = cv2.warpPerspective(pic1,projMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/bikes1_2/bikes1&2_proj_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5 * pic2
cv2.imwrite("output_images/bikes1_2/bikes1&2_stitch_proj_result.pgm", newImage)
a = ssift_descriptor.ssift_descriptor(featureList1,pic1)
b = ssift_descriptor.ssift_descriptor(featureList2,pic2)
dic = ratio_test.ratio_test(a,b)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in dic:
    if(dic[i]==0):continue
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(i[1],i[0]),(dic[i][1]+offSet,dic[i][0]),(color))
    cv2.circle(newImage,(i[1],i[0]),5,(color))
    cv2.circle(newImage,(dic[i][1]+offSet,dic[i][0]),5,(color))
cv2.imwrite("output_images/bikes1_2/bikes1&2_SSIFT_result.pgm", newImage)




# bikes1 <-> bikes3
pic1 = cv2.imread('bikes1.png')
pic2 = cv2.imread('bikes3.png')
featureList1 = detect_features.detect_features(pic1,20,0.1)
featureList2 = detect_features.detect_features(pic2,20,0.04)
pic1tmp = pic1.copy()
pic2tmp = pic2.copy()
for i in featureList1:
    color = (0, 0, 255)
    cv2.circle(pic1tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/bikes1_3/bikes1_features.pgm", pic1tmp)
for i in featureList2:
    color = (0, 0, 255)
    cv2.circle(pic2tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/bikes1_3/bikes3_features.pgm", pic2tmp)
listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,20)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in listInPairs:
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(color))
    cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(color))
    cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (color))
cv2.imwrite("output_images/bikes1_3/bikes1&3_matched_features.pgm", newImage)
affineMat, inliners= compute_affine_xform.compute_affine_xform(listInPairs,featureList1,featureList2, pic1, pic2)
for i in listInPairs:
    if i in inliners:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(255,0,0))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(255,0,0))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (255,0,0))
    else:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(0,0,255))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(0,0,255))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (0,0,255))
cv2.imwrite("output_images/bikes1_3/bikes1&3_inliners_outliners.pgm", newImage)
row,col = pic1.shape[:2]
image2From1 = cv2.warpAffine(pic1,affineMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/bikes1_3/bikes1&3_affine_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5*pic2
cv2.imwrite("output_images/bikes1_3/bikes1&3_stitch_affine_result.pgm", newImage)
projMat = compute_proj_xform.compute_proj_xform(listInPairs,featureList1,featureList2, pic1, pic2)
image2From1 = cv2.warpPerspective(pic1,projMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/bikes1_3/bikes1&3_proj_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5 * pic2
cv2.imwrite("output_images/bikes1_3/bikes1&3_stitch_proj_result.pgm", newImage)
a = ssift_descriptor.ssift_descriptor(featureList1,pic1)
b = ssift_descriptor.ssift_descriptor(featureList2,pic2)
dic = ratio_test.ratio_test(a,b)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in dic:
    if(dic[i]==0):continue
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(i[1],i[0]),(dic[i][1]+offSet,dic[i][0]),(color))
    cv2.circle(newImage,(i[1],i[0]),5,(color))
    cv2.circle(newImage,(dic[i][1]+offSet,dic[i][0]),5,(color))
cv2.imwrite("output_images/bikes1_3/bikes1&3_SSIFT_result.pgm", newImage)


# graf1 <-> graf2
pic1 = cv2.imread('graf1.png')
pic2 = cv2.imread('graf2.png')
featureList1 = detect_features.detect_features(pic1,20,0.01)
featureList2 = detect_features.detect_features(pic2,20,0.01)
pic1tmp = pic1.copy()
pic2tmp = pic2.copy()
for i in featureList1:
    color = (0, 0, 255)
    cv2.circle(pic1tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/graf1_2/graf1_features.pgm", pic1tmp)
for i in featureList2:
    color = (0, 0, 255)
    cv2.circle(pic2tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/graf1_2/graf2_features.pgm", pic2tmp)
listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,10)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in listInPairs:
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(color))
    cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(color))
    cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (color))
cv2.imwrite("output_images/graf1_2/graf1&2_matched_features.pgm", newImage)
affineMat, inliners= compute_affine_xform.compute_affine_xform(listInPairs,featureList1,featureList2, pic1, pic2)
for i in listInPairs:
    if i in inliners:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(255,0,0))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(255,0,0))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (255,0,0))
    else:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(0,0,255))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(0,0,255))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (0,0,255))
cv2.imwrite("output_images/graf1_2/graf1&2_inliners_outliners.pgm", newImage)
row,col = pic1.shape[:2]
image2From1 = cv2.warpAffine(pic1,affineMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/graf1_2/graf1&2_affine_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5*pic2
cv2.imwrite("output_images/graf1_2/graf1&2_stitch_affine_result.pgm", newImage)
projMat = compute_proj_xform.compute_proj_xform(listInPairs,featureList1,featureList2, pic1, pic2)
image2From1 = cv2.warpPerspective(pic1,projMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/graf1_2/graf1&2_proj_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5 * pic2
cv2.imwrite("output_images/graf1_2/graf1&2_stitch_proj_result.pgm", newImage)
a = ssift_descriptor.ssift_descriptor(featureList1,pic1)
b = ssift_descriptor.ssift_descriptor(featureList2,pic2)
dic = ratio_test.ratio_test(a,b)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in dic:
    if(dic[i]==0):continue
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(i[1],i[0]),(dic[i][1]+offSet,dic[i][0]),(color))
    cv2.circle(newImage,(i[1],i[0]),5,(color))
    cv2.circle(newImage,(dic[i][1]+offSet,dic[i][0]),5,(color))
cv2.imwrite("output_images/graf1_2/graf1&2_SSIFT_result.pgm", newImage)




# graf1 <-> graf3
pic1 = cv2.imread('graf1.png')
pic2 = cv2.imread('graf3.png')
featureList1 = detect_features.detect_features(pic1,20,0.3)
featureList2 = detect_features.detect_features(pic2,20,0.3)
pic1tmp = pic1.copy()
pic2tmp = pic2.copy()
for i in featureList1:
    color = (0, 0, 255)
    cv2.circle(pic1tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/graf1_3/graf1_features.pgm", pic1tmp)
for i in featureList2:
    color = (0, 0, 255)
    cv2.circle(pic2tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/graf1_3/graf3_features.pgm", pic2tmp)
listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,10)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in listInPairs:
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(color))
    cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(color))
    cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (color))
cv2.imwrite("output_images/graf1_3/graf1&3_matched_features.pgm", newImage)
affineMat, inliners= compute_affine_xform.compute_affine_xform(listInPairs,featureList1,featureList2, pic1, pic2)
for i in listInPairs:
    if i in inliners:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(255,0,0))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(255,0,0))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (255,0,0))
    else:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(0,0,255))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(0,0,255))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (0,0,255))
cv2.imwrite("output_images/graf1_3/graf1&3_inliners_outliners.pgm", newImage)
row,col = pic1.shape[:2]
image2From1 = cv2.warpAffine(pic1,affineMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/graf1_3/graf1&3_affine_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5*pic2
cv2.imwrite("output_images/graf1_3/graf1&3_stitch_affine_result.pgm", newImage)
projMat = compute_proj_xform.compute_proj_xform(listInPairs,featureList1,featureList2, pic1, pic2)
image2From1 = cv2.warpPerspective(pic1,projMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/graf1_3/graf1&3_proj_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5 * pic2
cv2.imwrite("output_images/graf1_3/graf1&3_stitch_proj_result.pgm", newImage)
a = ssift_descriptor.ssift_descriptor(featureList1,pic1)
b = ssift_descriptor.ssift_descriptor(featureList2,pic2)
dic = ratio_test.ratio_test(a,b)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in dic:
    if(dic[i]==0):continue
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(i[1],i[0]),(dic[i][1]+offSet,dic[i][0]),(color))
    cv2.circle(newImage,(i[1],i[0]),5,(color))
    cv2.circle(newImage,(dic[i][1]+offSet,dic[i][0]),5,(color))
cv2.imwrite("output_images/graf1_3/graf1&3_SSIFT_result.pgm", newImage)



# leuven1 <-> leuven2
pic1 = cv2.imread('leuven1.png')
pic2 = cv2.imread('leuven2.png')
featureList1 = detect_features.detect_features(pic1,20,0.1)
featureList2 = detect_features.detect_features(pic2,20,0.07)
pic1tmp = pic1.copy()
pic2tmp = pic2.copy()
for i in featureList1:
    color = (0, 0, 255)
    cv2.circle(pic1tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/leuven1_2/leuven1.pgm", pic1tmp)
for i in featureList2:
    color = (0, 0, 255)
    cv2.circle(pic2tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/leuven1_2/leuven2.pgm", pic2tmp)
listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,10)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in listInPairs:
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(color))
    cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(color))
    cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (color))
cv2.imwrite("output_images/leuven1_2/leuven1&2_matched_features.pgm", newImage)
affineMat, inliners= compute_affine_xform.compute_affine_xform(listInPairs,featureList1,featureList2, pic1, pic2)
for i in listInPairs:
    if i in inliners:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(255,0,0))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(255,0,0))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (255,0,0))
    else:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(0,0,255))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(0,0,255))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (0,0,255))
cv2.imwrite("output_images/leuven1_2/leuven1&2_inliners_outliners.pgm", newImage)
row,col = pic1.shape[:2]
image2From1 = cv2.warpAffine(pic1,affineMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/leuven1_2/leuven1&2_affine_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5*pic2
cv2.imwrite("output_images/leuven1_2/leuven1&2_stitch_affine_result.pgm", newImage)
projMat = compute_proj_xform.compute_proj_xform(listInPairs,featureList1,featureList2, pic1, pic2)
image2From1 = cv2.warpPerspective(pic1,projMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/leuven1_2/leuven1&2_proj_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5 * pic2
cv2.imwrite("output_images/leuven1_2/leuven1&2_stitch_proj_result.pgm", newImage)
a = ssift_descriptor.ssift_descriptor(featureList1,pic1)
b = ssift_descriptor.ssift_descriptor(featureList2,pic2)
dic = ratio_test.ratio_test(a,b)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in dic:
    if(dic[i]==0):continue
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(i[1],i[0]),(dic[i][1]+offSet,dic[i][0]),(color))
    cv2.circle(newImage,(i[1],i[0]),5,(color))
    cv2.circle(newImage,(dic[i][1]+offSet,dic[i][0]),5,(color))
cv2.imwrite("output_images/leuven1_2/leuven1&2_SSIFT_result.pgm", newImage)



#leuven1 <-> leuven3
pic1 = cv2.imread('leuven1.png')
pic2 = cv2.imread('leuven3.png')
featureList1 = detect_features.detect_features(pic1,20,0.05)
featureList2 = detect_features.detect_features(pic2,20,0.015)
pic1tmp = pic1.copy()
pic2tmp = pic2.copy()
for i in featureList1:
    color = (0, 0, 255)
    cv2.circle(pic1tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/leuven1_3/leuven1.pgm", pic1tmp)
for i in featureList2:
    color = (0, 0, 255)
    cv2.circle(pic2tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/leuven1_3/leuven3.pgm", pic2tmp)
listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,10)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in listInPairs:
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(color))
    cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(color))
    cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (color))
cv2.imwrite("output_images/leuven1_3/leuven1&3_matched_features.pgm", newImage)
affineMat, inliners= compute_affine_xform.compute_affine_xform(listInPairs,featureList1,featureList2, pic1, pic2)
for i in listInPairs:
    if i in inliners:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(255,0,0))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(255,0,0))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (255,0,0))
    else:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(0,0,255))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(0,0,255))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (0,0,255))
cv2.imwrite("output_images/leuven1_3/leuven1&3_inliners_outliners.pgm", newImage)
row,col = pic1.shape[:2]
image2From1 = cv2.warpAffine(pic1,affineMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/leuven1_3/leuven1&3_affine_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5*pic2
cv2.imwrite("output_images/leuven1_3/leuven1&3_stitch_affine_result.pgm", newImage)
projMat = compute_proj_xform.compute_proj_xform(listInPairs,featureList1,featureList2, pic1, pic2)
image2From1 = cv2.warpPerspective(pic1,projMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/leuven1_3/leuven1&3_proj_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5 * pic2
cv2.imwrite("output_images/leuven1_3/leuven1&3_stitch_proj_result.pgm", newImage)
a = ssift_descriptor.ssift_descriptor(featureList1,pic1)
b = ssift_descriptor.ssift_descriptor(featureList2,pic2)
dic = ratio_test.ratio_test(a,b)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in dic:
    if(dic[i]==0):continue
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(i[1],i[0]),(dic[i][1]+offSet,dic[i][0]),(color))
    cv2.circle(newImage,(i[1],i[0]),5,(color))
    cv2.circle(newImage,(dic[i][1]+offSet,dic[i][0]),5,(color))
cv2.imwrite("output_images/leuven1_3/leuven1&3_SSIFT_result.pgm", newImage)



# wall1 <-> wall2
pic1 = cv2.imread('wall1.png')
pic2 = cv2.imread('wall2.png')
row,col = pic2.shape[:2]
pic1 = cv2.resize(pic1,(col,row))
featureList1 = detect_features.detect_features(pic1,20,0.27)
featureList2 = detect_features.detect_features(pic2,20,0.3)
pic1tmp = pic1.copy()
pic2tmp = pic2.copy()
for i in featureList1:
    color = (0, 0, 255)
    cv2.circle(pic1tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/wall1_2/wall1_features.pgm", pic1tmp)
for i in featureList2:
    color = (0, 0, 255)
    cv2.circle(pic2tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/wall1_2/wall2_features.pgm", pic2tmp)
listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,10)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in listInPairs:
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(color))
    cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(color))
    cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (color))
cv2.imwrite("output_images/wall1_2/wall1&2_matched_features.pgm", newImage)
affineMat, inliners= compute_affine_xform.compute_affine_xform(listInPairs,featureList1,featureList2, pic1, pic2)
for i in listInPairs:
    if i in inliners:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(255,0,0))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(255,0,0))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (255,0,0))
    else:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(0,0,255))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(0,0,255))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (0,0,255))

cv2.imwrite("output_images/wall1_2/wall1&2_inliners_outliners.pgm", newImage)
row,col = pic1.shape[:2]
image2From1 = cv2.warpAffine(pic1,affineMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/wall1_2/wall1&2_affine_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5*pic2
cv2.imwrite("output_images/wall1_2/wall1&2_stitch_affine_result.pgm", newImage)
projMat = compute_proj_xform.compute_proj_xform(listInPairs,featureList1,featureList2, pic1, pic2)
image2From1 = cv2.warpPerspective(pic1,projMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/wall1_2/wall1&2_proj_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5 * pic2
cv2.imwrite("output_images/wall1_2/wall1&2_stitch_proj_result.pgm", newImage)
a = ssift_descriptor.ssift_descriptor(featureList1,pic1)
b = ssift_descriptor.ssift_descriptor(featureList2,pic2)
dic = ratio_test.ratio_test(a,b)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in dic:
    if(dic[i]==0):continue
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(i[1],i[0]),(dic[i][1]+offSet,dic[i][0]),(color))
    cv2.circle(newImage,(i[1],i[0]),5,(color))
    cv2.circle(newImage,(dic[i][1]+offSet,dic[i][0]),5,(color))
cv2.imwrite("output_images/wall1_2/wall1&2_SSIFT_result.pgm", newImage)

#wall1 <-> wall3
pic1 = cv2.imread('wall1.png')
pic2 = cv2.imread('wall3.png')
row,col = pic2.shape[:2]
pic1 = cv2.resize(pic1,(col,row))
featureList1 = detect_features.detect_features(pic1,20,0.2)
featureList2 = detect_features.detect_features(pic2,20,0.15)
pic1tmp = pic1.copy()
pic2tmp = pic2.copy()
for i in featureList1:
    color = (0, 0, 255)
    cv2.circle(pic1tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/wall1_3/wall1_features.pgm", pic1tmp)
for i in featureList2:
    color = (0, 0, 255)
    cv2.circle(pic2tmp, (i[1],i[0]), 5, (color))
cv2.imwrite("output_images/wall1_3/wall3_features.pgm", pic2tmp)
listInPairs = match_features.match_features(featureList1,featureList2,pic1,pic2,10)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in listInPairs:
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(color))
    cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(color))
    cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (color))
cv2.imwrite("output_images/wall1_3/wall1&3_matched_features.pgm", newImage)
affineMat, inliners= compute_affine_xform.compute_affine_xform(listInPairs,featureList1,featureList2, pic1, pic2)
for i in listInPairs:
    if i in inliners:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(255,0,0))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(255,0,0))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (255,0,0))
    else:
        cv2.line(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),(featureList2[i[1]][1]+offSet,featureList2[i[1]][0]),(0,0,255))
        cv2.circle(newImage,(featureList1[i[0]][1],featureList1[i[0]][0]),5,(0,0,255))
        cv2.circle(newImage, (featureList2[i[1]][1]+offSet,featureList2[i[1]][0]), 5, (0,0,255))
cv2.imwrite("output_images/wall1_3/wall1&3_inliners_outliners.pgm", newImage)
row,col = pic1.shape[:2]
image2From1 = cv2.warpAffine(pic1,affineMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/wall1_3/wall1&3_affine_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5*pic2
cv2.imwrite("output_images/wall1_3/wall1&3_stitch_affine_result.pgm", newImage)
projMat = compute_proj_xform.compute_proj_xform(listInPairs,featureList1,featureList2, pic1, pic2)
image2From1 = cv2.warpPerspective(pic1,projMat,(col, row))
newImage = np.concatenate((image2From1,pic2),axis= 1)
cv2.imwrite("output_images/wall1_3/wall1&3_proj_result.pgm", newImage)
newImage = cv2.warpAffine(pic1, affineMat, (pic1.shape[1]+100,pic1.shape[0]+100))
newImage[0:pic2.shape[0],0:pic2.shape[1]] = 0.5*newImage[0:pic2.shape[0],0:pic2.shape[1]]+0.5 * pic2
cv2.imwrite("output_images/wall1_3/wall1&3_stitch_proj_result.pgm", newImage)
a = ssift_descriptor.ssift_descriptor(featureList1,pic1)
b = ssift_descriptor.ssift_descriptor(featureList2,pic2)
dic = ratio_test.ratio_test(a,b)
newImage = np.concatenate((pic1,pic2),axis= 1)
offSet = pic1.shape[1]
for i in dic:
    if(dic[i]==0):continue
    color = np.random.randint(0, 255, 3)
    cv2.line(newImage,(i[1],i[0]),(dic[i][1]+offSet,dic[i][0]),(color))
    cv2.circle(newImage,(i[1],i[0]),5,(color))
    cv2.circle(newImage,(dic[i][1]+offSet,dic[i][0]),5,(color))
cv2.imwrite("output_images/wall1_3/wall1&3_SSIFT_result.pgm", newImage)
