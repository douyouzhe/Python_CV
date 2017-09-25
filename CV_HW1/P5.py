import numpy as np
import cv2
import scipy.ndimage as nd
import matplotlib.pyplot as plt



def p5(image_in): #return edge_image_out

    image = cv2.imread(image_in, 0)
    row, col = image.shape
    for i in range(row):
        for j in range(col):
            print image[i,j]
    # out = np.zeros((row,col))
    # for y in range(row):
    #     Mr = image[y]
    #     Or = out[y]
    #     Or[0] = float(Mr[1]) - float(Mr[0])
    #     for x in range(1, col - 1):
    #         Or[x] = (float(Mr[x+1]) - float(Mr[x-1]))/2.0
    #     Or[col-1] = float(Mr[col-1]) - float(Mr[col-2])
    #print out
    sobelCol = np.array([[-1, -2, 0, 2, 1],
                   [-2, -3, 0, 3, 2],
                   [-3, -5, 0, 5, 3],
                   [-2, -3, 0, 3, 2],
                   [-1, -2, 0, 2, 1]])
    sobelRow = np.array([[1, 2, 3, 2, 1],
                   [2, 3, 5, 3, 2],
                   [0, 0, 0, 0, 0],
                   [-2, -3, -5, -3, -2],
                   [-1, -2, -3, -2, -1]])
    out1 = np.zeros((row,col))
    out2 = np.zeros((row, col))
    for i in range(2, row-2):
        for j in range(2, col-2):
            val = sobelCol*image[(i-2):(i+3),(j-2):(j+3)]
            out1[i,j] = min(255,max(0,val.sum()))
    for i in range(2, row-2):
        for j in range(2, col-2):
            val = sobelRow*image[(i-2):(i+3),(j-2):(j+3)]
            out2[i,j] = min(255,max(0,val.sum()))
    out1 = ndimage.sobel(image,0)
    out2 = ndimage.sobel(image, 1)
    mag = np.hypot(out1,out2)
    mag*=255.0/np.max(mag)

    # scipy.misc.imsave('111.jpg',mag);
    for i in range(row):
        for j in range(col):
            out1[i,j]=int(mag[i,j])
    return out1




###### test #######
pic = p5('hough_simple_2.pgm')
# cv2.imshow('image',pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#cv2.imwrite("111.pgm", pic)