import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2

def p3(labeled_img):  #return [database_out, overlays_out]
    image = cv2.imread(labeled_img,0)
    vals = np.unique(image)
    row,col = image.shape
    outterDic = {}

    for k in range(len(vals)-1):
        area, xMean ,yMean = 0,0,0
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

    for k in range(len(vals)-1):

        a,b,c = 0,0,0
        iCenter = outterDic[k]['Position'][1]
        jCenter = outterDic[k]['Position'][0]

        for i in range(row):
            for j in range(col):
                if image[i,j]==vals[k+1]:
                    b+=2*(i-iCenter)*(j-jCenter)
                    c+=(i-iCenter)*(i-iCenter)
                    a+=(j-jCenter)*(j-jCenter)
        theta = np.arctan2(b,a-c)/2.0
        if ((a-c)*np.cos(2*theta)+b*np.sin(2*theta))<0:
            theta = theta + np.pi / 2


        thetaTmp = theta + np.pi / 2
        tmp1 = a * np.sin(theta) * np.sin(theta) - b * np.sin(theta) * np.cos(theta) + c * np.cos(theta) * np.cos(theta)
        tmp2 = a * np.sin(thetaTmp) * np.sin(thetaTmp) - b * np.sin(thetaTmp) * np.cos(thetaTmp) + c * np.cos(thetaTmp) * np.cos(thetaTmp)

        roundness = tmp1/tmp2
        outterDic[k]['Orientation'] = theta
        outterDic[k]['Roundness'] = roundness

    for i in range(len(outterDic)):
        cv2.circle(image, (outterDic[i]['Position'][0], outterDic[i]['Position'][1]), 10, (255, 255, 255))
        cv2.line(image, (outterDic[i]['Position'][0], outterDic[i]['Position'][1]),
                 (outterDic[i]['Position'][0] + 50, outterDic[i]['Position'][1] + int(np.tan(outterDic[i]['Orientation']) * 50)),
                 (255, 255, 255))
    # cv2.imshow('image', image)
    # cv2.waitKey(0)


    return outterDic, image
###### test #######
# pic = p3('newLabel.pgm')
# cv2.imshow('image',pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("binaryImage.pgm", pic)