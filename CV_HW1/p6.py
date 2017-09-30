import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math
import matplotlib.pyplot as plt


def p6(edge_image, edge_thresh): # return [edge_thresh_image, hough_image]

    image = cv2.imread(edge_image, 0)
    row, col = image.shape
    edge_thresh_out = np.zeros((row, col),np.uint8)

    for i in range(row):
        for j in range(col):
            if(image[i,j]<edge_thresh):
                edge_thresh_out[i, j]=0
            else:
                edge_thresh_out[i, j] = image[i, j]


    thetas = np.deg2rad(np.arange(-90.0, 90.0))
    diag_len = int(np.ceil(np.sqrt(row * row + col * col)))
    rhos = np.linspace(-diag_len, diag_len, diag_len * 2.0)
    cos_t = np.cos(thetas)
    sin_t = np.sin(thetas)
    num_thetas = len(thetas)

    accumulator = np.zeros((2*diag_len, num_thetas), dtype=np.float64)
    y_idxs, x_idxs = np.nonzero(edge_thresh_out)

    for i in range(len(x_idxs)):
        x = x_idxs[i]
        y = y_idxs[i]

        for t_idx in range(num_thetas):
            # Calculate rho. diag_len is added for a positive index
            rho = int(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len
            accumulator[rho, t_idx] += 1

    #return accumulator, thetas, rhos
    #print accumulator

    # rho = int(math.sqrt(row*row*1.0+col*col*1.0))
    # theta = 360
    # accumulator = np.zeros((theta,rho),np.float32)
    # out = np.zeros((theta, rho), np.uint8)
    # max = 0
    #
    # for i in range(row):
    #     for j in range(col):
    #         if edge_thresh_out[i,j,0]!= 0:
    #             for k in range(theta):
    #                 r = int(i*np.sin(np.pi*k/theta)+j*np.cos(np.pi*k/theta))
    #                 accumulator[k,r]+=1
    #                 if(accumulator[k,r]>max):
    #                     max = accumulator[k,r]
    #
    # for i in range(theta):
    #     for j in range(rho):
    #         out[i,j] = accumulator[i,j]/max*255
    #
    #
    # #for i in range(theta)

    print accumulator
    return edge_thresh_out, accumulator


###### test #######
pic, houghOut = p6('edge_2_result.pgm',120)
plt.imshow(houghOut)
plt.show()
# cv2.imshow('image',houghOut)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite("edge_thresh_2_result.pgm", pic)
cv2.imwrite("hough_image_2_result.pgm", houghOut)
