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




#####
class DisjointSet(object):

    def __init__(self):
        self.leader = {} # maps a member to the group's leader
        self.group = {} # maps a group leader to the group (which is a set)

    def add(self, a, b):
        leadera = self.leader.get(a)
        leaderb = self.leader.get(b)
        if leadera is not None:
            if leaderb is not None:
                if leadera == leaderb: return # nothing to do
                groupa = self.group[leadera]
                groupb = self.group[leaderb]
                if len(groupa) < len(groupb):
                    a, leadera, groupa, b, leaderb, groupb = b, leaderb, groupb, a, leadera, groupa
                groupa |= groupb
                del self.group[leaderb]
                for k in groupb:
                    self.leader[k] = leadera
            else:
                self.group[leadera].add(b)
                self.leader[b] = leadera
        else:
            if leaderb is not None:
                self.group[leaderb].add(a)
                self.leader[a] = leaderb
            else:
                self.leader[a] = self.leader[b] = a
                self.group[a] = set([a, b])
#####

def p2(binary_in):  # return labels_out
    image = cv2.imread(binary_in, 0)
    shape = image.shape
    a = np.zeros(shape, int); # label matrix
    k = 1
    b = []
    c = []

    for i in range(shape[0]): # 1 is white o is background
        for j in range(shape[1]):
            if image[i,j] == 0: #background
                a[i,j] = 0;
            elif image[i,j] == 255 and a[i-1,j-1] != 0: #D is labeled
                a[i,j] = a[i-1,j-1];
            elif image[i,j] == 255 and a[i-1,j] == 0 and a[i,j-1] == 0: #B and C are not labeled
                a[i,j] = k;
                k+=1; #update label
            elif image[i,j] == 255 and a[i-1,j] !=0 and a[i,j-1] ==0: #B is labeled
                a[i,j] = a[i-1,j];
            elif image[i,j] == 255 and a[i,j-1] !=0 and a[i-1,j] ==0: #C is labeled
                a[i,j] = a[i,j-1];
            elif a[i,j-1] !=0 and a[i-1,j] !=0: #B and C are labeled
                if a[i,j-1] ==  a[i-1,j] :
                    a[i,j] = a[i,j-1];
                else:
                    a[i,j] = a[i,j-1];
                    b.append(a[i-1,j]);
                    c.append(a[i,j-1]);
    k=0; h=0
    b_t = np.array(b)

    dic = {}
    dic2 = {}
    group = 0
    ls=[]

    for k in range(len(b)):
        ls.append([b[k],c[k]])

    ls.sort()



    for k in range(len(ls)):  # Create Eq_Table
        if ls[k][0] in dic:
            dic[ls[k][1]] = dic.get(ls[k][0])
        elif ls[k][1] in dic:
            dic[ls[k][0]] = dic.get(ls[k][1])
        else:
            group = group + 1
            dic[ls[k][0]] = group
            dic[ls[k][1]] = group
            #print k

    # c.sort()
    # b.sort()
    # for k in range(len(b)):  # Create Eq_Table
    #     if b[k] in dic:
    #         dic[c[k]] = dic.get(b[k])
    #     elif c[k] in dic:
    #         dic[b[k]] = dic.get(c[k])
    #     else:
    #         group = group + 1
    #         dic[b[k]] = group
    #         dic[c[k]] = group

    # print b;
    # print c;
    # for i in dic.values():
    #     if i==3:
    #         print "a"
    #
    # print ls[103]
    # print ls[104]
    # print ls[105]

    #print dic.values()
    aa=[]
    for [m,n] in ls:
        if(dic.get(m)==1):
            aa.append(m)
        if(dic.get(n)==1):
            aa.append(n)

    print aa
    return a;

###### test p2 #######
pic = p2('binaryImage.pgm')
#cv2.imshow('',pic)
#cv2.waitKey(0)
#cv2.imwrite("newLabel.pgm", pic)
