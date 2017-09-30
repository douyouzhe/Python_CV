import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

im = cv2.imread("hough_image_3_result.pgm")
test = cv2.imread("edge_3_result.pgm", 0)
result = cv2.imread("hough_complex_1.pgm")
line = []

ret, thresh1 = cv2.threshold(test, 70, 255, cv2.THRESH_BINARY)

# cv2.imshow('testdsa',thresh1)
# cv2.waitKey(0)

for i in xrange(1, len(im) - 1):
    for j in xrange(1, len(im[0]) - 1):
        a = im[i, j, 0]
        # (int(im[i-1,j-1,0])+int(im[i-1,j,0])+int(im[i-1,j+1,0])+int(im[i,j-1,0])+int(im[i,j,0])+int(im[i,j+1,0])+int(im[i+1,j-1,0])+int(im[i+1,j,0])+int(im[i+1,j+1,0]))/9.0
        if a > 100:
            line.append((i, j))

#
# for i in range(1,len(line)):
#     if abs(line[i][0]-line[i-1][0])<10 and abs(line[i][1]-line[i-1][1])<13:
#         line[i]=line[i-1];

for i in line:
    rho = i[1]
    theta = np.pi * (i[0]) / 180
    # print rho,math.degrees(theta)



    if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):
        pt1 = (int(rho / np.cos(theta)), 0)
        pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0] - 1)
        for j in range(1, result.shape[0] - 1):
            pt_temp_1 = (int((rho - j * np.sin(theta)) / np.cos(theta)), j)
            pt_temp_2 = (int((rho - (j + 1) * np.sin(theta)) / np.cos(theta)), (j + 1))
            # print pt_temp_1,pt_temp_2
            # print  result.shape
            incre=2;
            val = thresh1[pt_temp_1[0]-incre:pt_temp_1[0]+incre,pt_temp_1[1]-incre:pt_temp_1[1]+incre].sum()
            if pt_temp_1[0] > 0 and pt_temp_1[0] < 474 and abs(thresh1[pt_temp_1] - thresh1[pt_temp_2]) < 40 and val >0:
                # print result[pt_temp_1[0]][pt_temp_1[1]][0]
                cv2.line(result, pt_temp_1, pt_temp_2, (255), 1)

    else:
        for j in range(1, result.shape[0] - 1):
            pt_temp_1 = (int((rho - j * np.sin(theta)) / np.cos(theta)), j)
            pt_temp_2 = (int((rho - (j + 1) * np.sin(theta)) / np.cos(theta)), (j + 1))
            incre=2;
            val = thresh1[pt_temp_1[0]-incre:pt_temp_1[0]+incre,pt_temp_1[1]-incre:pt_temp_1[1]+incre].sum()
            if pt_temp_1[0] > 0 and pt_temp_1[0] < 474 and abs(thresh1[pt_temp_1] - thresh1[pt_temp_2]) < 40 and val >0:
                cv2.line(result, pt_temp_1, pt_temp_2, (255), 1)
plt.imshow(result)
plt.show()