import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import matplotlib.pyplot as plt

def p5(image_in): #return edge_image_out

    image = cv2.imread(image_in,0)
    row, col = image.shape
    out1 = np.zeros((row, col))
    out2 = np.zeros((row, col))
    out = np.zeros((row, col),np.uint8)

    sobelCol = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobelRow = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

    for i in range(1, row-1):
        for j in range(1, col-1):
            out1[i, j] = (sobelCol * image[(i - 1):(i + 2), (j - 1):(j + 2)]).sum()
            out2[i, j] = (sobelRow * image[(i - 1):(i + 2), (j - 1):(j + 2)]).sum()
            out[i, j] = abs(out1[i, j]) + abs(out2[i, j])


    # sobelCol = np.array([[-1, -2, 0, 2, 1],
    #                [-2, -3, 0, 3, 2],
    #                [-3, -5, 0, 5, 3],
    #                [-2, -3, 0, 3, 2],
    #                [-1, -2, 0, 2, 1]])
    # sobelRow = np.array([[1, 2, 3, 2, 1],
    #                [2, 3, 5, 3, 2],
    #                [0, 0, 0, 0, 0],
    #                [-2, -3, -5, -3, -2],
    #                [-1, -2, -3, -2, -1]])
    #
    # for i in range(2, row-2):
    #     for j in range(2, col-2):
    #         out1[i, j] = (sobelCol * image[(i - 2):(i + 3), (j - 2):(j + 3)]).sum()
    #         out2[i, j] = (sobelRow * image[(i - 2):(i + 3), (j - 2):(j + 3)]).sum()
    #         val = abs(out1[i, j]) + abs(out2[i, j])
    #         out[i, j] =[val,val,val]

    return out

