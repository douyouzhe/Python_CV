import numpy as np
import cv2

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

###### test #######
pic = p1('two_objects.pgm',125)
cv2.imshow('image',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite("binaryImage.pgm", pic)