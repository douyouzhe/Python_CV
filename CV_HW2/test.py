import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
H = np.zeros((2,2),np.float64)
H[0, 0] = 1
H[0, 1] = 2
H[1, 0] = 3
H[1, 1] = 4
print H**2
