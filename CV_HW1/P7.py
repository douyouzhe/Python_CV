import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math
import matplotlib.pyplot as plt

def p7(image, hough_image, hough_thresh):#return line_image
    image = cv2.imread(image)
    hough_image = cv2.imread(hough_image)
    lines = []
    for i in range(len(hough_image)):
        for j in range(len(hough_image[0])):
            val = hough_image[i, j, 0]
            if val > hough_thresh:
                lines.append((i, j))
    for rho, theta in lines:
        rho -=800
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)

    return image




###### test #######
pic = p7('hough_simple_2.pgm','hough_image_2_result.pgm',150)
cv2.imshow('image',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite("edge_thresh_2_result.pgm", pic)
# cv2.imwrite("hough_image_2_result.pgm", houghOut)
