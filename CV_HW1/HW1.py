import numpy as np
import cv2
from matplotlib import pyplot as plt



def p1(gray_in, thresh_val): # return binary_out
    ## can use the following function
    #ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

    twoObj = cv2.imread(gray_in,0)# 0 is for grayscale images
    row, col = twoObj.shape
    binaryImage = np.zeros((np.shape(twoObj)[0], np.shape(twoObj)[1]), np.uint8);
    for i in range(0, row):
        for j in range(0, col):
            if (twoObj[i, j] > thresh_val):
                binaryImage[i, j] = 255
            else:
                binaryImage[i, j] = 0
    return binaryImage


###### test p1 #######
#pic = p1('two_objects.pgm',125)
#cv2.imshow('',pic)
#cv2.waitKey(0)
#cv2.imwrite("binaryImage.pgm", pic)


#cc Algorithm
# if A = O          do nothing
# else if D labeled
#      copy label to A
# else if (not B labeled) and (not C labeled)
#      increment label numbering and label A
# else if B xor C labeled
#      copy label to A
# else if B and C labeled
#      if B label = C label
#           copy label to A
#      else
#           copy either B label or C label to A
#           record equivalence of labels



def p2(binary_in):  # return labels_out
    image = cv2.imread(binary_in, 0)
    shape = image.shape
    a = np.zeros(shape, int); # label matrix
    k = 1
    b = []
    c = []

    for i in range(shape[0]): # 1 is white o is background
        for j in range(shape[1]):
            if image[i,j] == 0:
                a[i,j] = 0
            elif image[i,j] == 255 and a[i-1,j-1] != 0: #D is labeled
                a[i,j] = a[i-1,j-1];
            elif image[i,j] == 255 and a[i-1,j] == 0 and a[i,j-1] == 0: #B and C are not labeled
                a[i,j] = k
                k+=1
            elif image[i,j] == 255 and a[i-1,j] !=0 and a[i,j-1] ==0: #B is labeled
                a[i,j] = a[i-1,j]
            elif image[i,j] == 255 and a[i,j-1] !=0 and a[i-1,j] ==0: #C is labeled
                a[i,j] = a[i,j-1]
            elif a[i,j-1] !=0 and a[i-1,j] !=0: #B and C are labeled
                if a[i,j-1] ==  a[i-1,j] :
                    a[i,j] = a[i,j-1]
                else:
                    a[i,j] = a[i,j-1]
                    b.append(a[i-1,j])
                    c.append(a[i,j-1])

    dic = {}
    group = 100
    ls=[]
    for k in range(len(b)):
        ls.append([b[k],c[k]])
    ls.sort()

    for k in range(len(ls)):  # Create Eq_Table
        if (ls[k][0] in dic) and (ls[k][1] in dic):
            m = dic.get(ls[k][0])
            n = dic.get(ls[k][1])
            if(m<n):
                for i in dic:
                    if dic.get(i)==n:
                        dic[i]=m
            else:
                for i in dic:
                    if dic.get(i)==m:
                        dic[i]=n
        if ls[k][0] in dic:
            dic[ls[k][1]] = dic.get(ls[k][0])
        if ls[k][1] in dic:
            dic[ls[k][0]] = dic.get(ls[k][1])
        else:
            group = group + 100
            dic[ls[k][0]] = group
            dic[ls[k][1]] = group
    row,col = a.shape
    pic = np.zeros([row,col])
    for i in range(0, row):
        for j in range(0, col):
            if(a[i,j]!=0):
                pic[i,j] = dic.get(a[i,j])

    return pic

###### test p2 #######
pic = p2('binaryImage.pgm')
#cv2.imshow('',pic)
#cv2.waitKey(0)
cv2.imwrite("newLabel.pgm", pic)
