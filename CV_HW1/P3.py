import numpy as np
import cv2

def p3(labeled_img):  #return [database_out, overlays_out]
    image = cv2.imread(labeled_img, 0)
    vals = np.unique(image)
    row,col = image.shape
    outterDic = {}

    for k in range(len(vals)-1): #position of the object
        area = 0
        xMean = 0
        yMean = 0
        innerDic ={}
        for i in range(row):
            for j in range(col):
                if image[i,j]==vals[k+1]:
                    area+=1
                    yMean+=i
                    xMean+=j
        innerDic['Area'] = area
        innerDic['Position'] = [xMean/area,yMean/area]
        outterDic[k] = innerDic


    for k in range(len(vals)-1): #orientation of the object
        b = 0
        a = 0
        c = 0
        iCenter = outterDic[k]['Position'][0]
        jCenter = outterDic[k]['Position'][1]
        for i in range(row):
            for j in range(col):
                if image[i,j]==vals[k+1]:
                    b+=2*(i-iCenter)*(j-jCenter)
                    c+=(i-iCenter)*(i-iCenter)
                    a+=(j-jCenter)*(j-jCenter)
        theta=np.arctan(float(b/(a-c)))/2
        if ((a-c)*np.cos(2*theta)+b*np.sin(2*theta))<0:
            theta = theta + np.pi / 2
        outterDic[k]['Orientation'] = theta


    for k in range(len(vals)-1):
        min_i=0
        min_j=0
        max_i=0
        max_j=0
        for i in range(row):
            for j in range(col):
               if image[i,j] == vals[k+1] and j==int((i-outterDic[k]['Position'][0])*np.tan(outterDic[k]['Orientation'])+outterDic[k]['Position'][0]):
                    if min_i==0:
                        min_i=i
                        min_j=j
                        max_i=i
                        max_j=j
                    else:
                        if min_i>=i:
                            min_i=i
                        if min_j>=j:
                            min_j=j
                        if max_i<=i:
                            max_i=i
                        if max_j<=j:
                            max_j=j

        outterDic[k]['Template_size'] = [min_i,min_j,max_i,max_j]

    print outterDic




    # print dicts;
    # cv2.circle(labeled_img, (dicts[0]['position'][0], dicts[0]['position'][1]), 10, (0, 0, 255))
    # cv2.circle(labeled_img, (dicts[1]['position'][0],dicts[1]['position'][1]), 10,(0,0,255))
    # cv2.line(labeled_img,(dicts[0]['position'][0],dicts[0]['position'][1]),(dicts[0]['position'][0]+50,dicts[0]['position'][1]+int(np.tan(dicts[0]['orientation'])*50)),(0, 0, 255))
    # cv2.line(labeled_img,(dicts[1]['position'][0],dicts[1]['position'][1]),(dicts[1]['position'][0]+50,dicts[1]['position'][1]+int(np.tan(dicts[1]['orientation'])*50)),(0, 0, 255))
    # cv2.imshow('test',labeled_img)
    # cv2.waitKey(0)

    return outterDic
###### test #######
pic = p3('newLabel.pgm')
# cv2.imshow('image',pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("binaryImage.pgm", pic)