import cv2
import numpy as np
pic1 = cv2.imread('bikes1.png')

m = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
n=  np.matrix([m.item(1), m.item(2), 1])
print n.item(2)