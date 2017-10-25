import cv2
import numpy as np
import matplotlib.pyplot as plt

def ssift_descriptor(feature_coords,image):
    """
    Computer Vision 600.461/661 Assignment 2
    Args:
        feature_coords (list of tuples): list of (row,col) tuple feature coordinates from image
        image (numpy.ndarray): The input image to compute ssift descriptors on. Note: this is NOT the image name or image path.
    Returns:
        descriptors (dictionary{(row,col): 128 dimensional list}): the keys are the feature coordinates (row,col) tuple and
                                                                   the values are the 128 dimensional ssift feature descriptors.
    """
    descriptors = dict()
    eightElementList = []
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    sobelN = np.array([[1,2,1], [0,0,0], [-1,2,-1]])
    sobelNE = np.array([[0,1,2], [-1,0,-1], [2, -1, 0]])
    sobelE = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobelES = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])
    sobelS = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    sobelSW = np.array([[0, -1, 2], [1, 0, -1], [2, 1, 0]])
    sobelW = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    sobelWN = np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]])
    gradMat = cv2.filter2D(src=image, ddepth=cv2.CV_64F, kernel=sobelN)
    eightElementList.append(gradMat)
    gradMat = cv2.filter2D(src=image, ddepth=cv2.CV_64F, kernel=sobelNE)
    eightElementList.append(gradMat)
    gradMat = cv2.filter2D(src=image, ddepth=cv2.CV_64F, kernel=sobelE)
    eightElementList.append(gradMat)
    gradMat = cv2.filter2D(src=image, ddepth=cv2.CV_64F, kernel=sobelES)
    eightElementList.append(gradMat)
    gradMat = cv2.filter2D(src=image, ddepth=cv2.CV_64F, kernel=sobelS)
    eightElementList.append(gradMat)
    gradMat = cv2.filter2D(src=image, ddepth=cv2.CV_64F, kernel=sobelSW)
    eightElementList.append(gradMat)
    gradMat = cv2.filter2D(src=image, ddepth=cv2.CV_64F, kernel=sobelW)
    eightElementList.append(gradMat)
    gradMat = cv2.filter2D(src=image, ddepth=cv2.CV_64F, kernel=sobelWN)
    eightElementList.append(gradMat)


    for coord in feature_coords:
        windowSize = 20
        row, col = image.shape
        if (coord[0] + windowSize >= row) or (coord[0] - windowSize <= 0) or \
                         (coord[1]+windowSize>=col)or(coord[1]-windowSize<=0):continue
        y = coord[0] - 20
        x = coord[1] - 20
        window = np.zeros((41, 41), np.matrix)
        for i in range(41):
            for j in range(41):
                window[i,j] = y,x
                x+=1
            y+=1
            x=coord[1] - 20

        size = 10
        vec = np.zeros((4,4,8))
        for m in range(4):
            for n in range(4):
                grid = window[m*size:m*size+size,n*size:n*size+size]
                cnt = 0
                for i in eightElementList:
                    sum = 0
                    for j in grid:
                        for k in range(10):
                            sum+= i[j[k]]
                    vec[m,n,cnt] = sum
                    cnt += 1

        vec = np.resize(vec,(128,1))
        vec= vec/np.dot(vec.T,vec)
        for i in vec:
            if i > 0.2:
                i = 0.2

        vec = vec / np.dot(vec.T, vec)
        descriptors[coord] = vec
    return descriptors


# windowSize = 20+2
        # row,col = image.shape
        # if(coord[0]+windowSize>=row)or(coord[0]-windowSize<=0)or\
        #         (coord[1]+windowSize>=col)or(coord[1]-windowSize<=0):continue
        # y = coord[0] -20
        # x = coord[1] -20
        # window = np.zeros((41, 41), np.matrix)
        # for i in range(41):
        #     for j in range(41):
        #         window[i,j] = y,x
        #         x+=1
        #     y+=1
        #
        # count0 = -1
        # for i in window:
        #     for j in range(41):
        #         count0+=1
        #         print i[j]
        #         y = i[j][0]-2
        #         x = i[j][1]-2
        #         grid = np.zeros((4,4),np.matrix)
        #         for i in range(4):
        #             for j in range(4):
        #                 grid[i,j] = y,x
        #                 x+=1
        #             y+=1
        #         print grid

                #     count1 = 0
                #     for i in grid:
                #         for j in range(4):
                #             print i[j]
                #             for k in eightElementList:
                #                 # print count0
                #                 # print count1
                #                 # print k[i[j]]
                #                 #vec[count1,count0] =  k[i[j]]
                #                 count1+=1


    #print vec


        # row = coord[0]-2
        # col = coord[1]-2
        # grid = np.zeros((4,4),np.matrix)
        # for i in range(4):
        #     for j in range(4):
        #         grid[i,j] = row,col
        #         col+=1
        #     row+=1


        # vec = np.zeros((4*4*8,1))
        #
        # count = 0
        # for i in grid:
        #     for j in range(4):
        #         for k in eightElementList:
        #             vec[count] =  k[i[j]]
        #             count+=1
        # #print vec.shape
        #
        # descriptors[coord] = vec
