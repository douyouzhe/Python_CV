import numpy as np
import cv2
import matplotlib.pyplot as plt


def p2(binary_in):  # return labels_out
    # cc Algorithm
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
    image = cv2.imread(binary_in, 0)
    shape = image.shape
    a = np.zeros(shape, int)
    label=1 # label before equivalence
    dic = {}
    group = 0 # label after equivalence
    ls=[]

    for i in range(shape[0]): # 255 is white 0 is background
        for j in range(shape[1]):
            if image[i,j] == 0:
                a[i,j] = 0 # pass background
            elif a[i-1,j-1] != 0: #D is labeled
                a[i,j] = a[i-1,j-1]
            elif a[i-1,j] == 0 and a[i,j-1] == 0: #B and C are not labeled
                a[i,j] = label
                label+=1
            elif a[i-1,j] !=0 and a[i,j-1] ==0: #B is labeled
                a[i,j] = a[i-1,j]
            elif a[i,j-1] !=0 and a[i-1,j] ==0: #C is labeled
                a[i,j] = a[i,j-1]
            elif a[i,j-1] !=0 and a[i-1,j] !=0: #B and C are labeled
                if a[i,j-1] ==  a[i-1,j]:
                    a[i,j] = a[i,j-1]
                else:
                    a[i,j] = a[i,j-1]
                    ls.append([a[i-1,j],a[i,j-1]]) # save paired labels
    ls.sort()#unnucessary in this case
    for k in range(len(ls)):  # Create Equivalence Table
        if (ls[k][0] in dic) and (ls[k][1] in dic):
            #if both labels are in dic, change the label to the smaller one
            #need to change all previous labels as well
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
        # if either one not in dic, add the same label to them
        if ls[k][0] in dic:
            dic[ls[k][1]] = dic.get(ls[k][0])
        if ls[k][1] in dic:
            dic[ls[k][0]] = dic.get(ls[k][1])
        #both not found, create new label
        else:
            group = group + 20
            dic[ls[k][0]] = group
            dic[ls[k][1]] = group
    row,col = a.shape
    pic = np.zeros([row,col])
    # give labels a specific value so they can be seen
    for i in range(0, row):
        for j in range(0, col):
            if(a[i,j]!=0):
                pic[i,j] = dic.get(a[i,j])
    return pic

###### test #######
# pic = p2('binaryImage.pgm')
# cv2.imshow('labeled image', pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.imshow(pic)
# plt.show()
# cv2.imwrite("newLabel.pgm", pic)