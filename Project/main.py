import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import os
import lane_detection



test_images = [lane_detection.read_image('test_images/' + i) for i in os.listdir('test_images/')]
print test_images
lane_detection.draw_lane_lines(test_images[4])