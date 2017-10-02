import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math
import matplotlib.pyplot as plt
from P5 import p5
from P6 import p6
from P7 import p7
from P8 import p8


pic = p5('hough_simple_1.pgm')
cv2.imwrite("hough_simple_1_edge.pgm", pic)
pic = p5('hough_simple_2.pgm')
cv2.imwrite("hough_simple_2_edge.pgm", pic)
pic = p5('hough_complex_1.pgm')
cv2.imwrite("hough_complex_1_edge.pgm", pic)

pic, houghOut = p6('hough_simple_1_edge.pgm',70)
cv2.imwrite("hough_simple_1_edge_threshed.pgm", pic)
cv2.imwrite("hough_image_1_result.pgm", houghOut)
pic, houghOut = p6('hough_simple_2_edge.pgm',50)
cv2.imwrite("hough_simple_2_edge_threshed.pgm", pic)
cv2.imwrite("hough_image_2_result.pgm", houghOut)
pic, houghOut = p6('hough_complex_1_edge.pgm',70)
cv2.imwrite("hough_complex_1_edge_threshed.pgm", pic)
cv2.imwrite("hough_complex_1_result.pgm", houghOut)

pic = p7('hough_simple_1.pgm','hough_image_1_result.pgm',250)
cv2.imwrite("hough_simple_1_lineImage.pgm", pic)
pic = p7('hough_simple_2.pgm','hough_image_2_result.pgm',250)
cv2.imwrite("hough_simple_2_lineImage.pgm", pic)
pic = p7('hough_complex_1.pgm','hough_complex_1_result.pgm',150)
cv2.imwrite("hough_complex_1_lineImage.pgm", pic)

pic = p8('hough_simple_1.pgm','hough_image_1_result.pgm','hough_simple_1_edge_threshed.pgm',150)
cv2.imwrite("hough_simple_1_croppedLineImage.pgm", pic)
pic = p8('hough_simple_2.pgm','hough_image_2_result.pgm','hough_simple_2_edge_threshed.pgm',140)
cv2.imwrite("hough_simple_2_croppedLineImage.pgm", pic)
pic = p8('hough_complex_1.pgm','hough_complex_1_result.pgm','hough_complex_1_edge_threshed.pgm',100)
cv2.imwrite("hough_complex_1_croppedLineImage.pgm", pic)