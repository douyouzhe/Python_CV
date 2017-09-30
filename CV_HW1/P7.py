import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math
import matplotlib.pyplot as plt

def p7(image, hough_image, hough_thresh):#return line_image
    image = cv2.imread(image)
    hough_image = cv2.imread(hough_image)



    return out

###### test #######
pic = p7('hough_simple_2.pgm','hough_image_2_result.pgm',40)
# cv2.imshow('image',houghOut)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("edge_thresh_2_result.pgm", pic)
# cv2.imwrite("hough_image_2_result.pgm", houghOut)
