import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math
import matplotlib.pyplot as plt
from P1 import p1
from P2 import p2
from P3 import p3

# manyObj1Binary = p1("many_objects_1.pgm", 125)
# cv2.imwrite("manyObj1Binary.pgm", manyObj1Binary)
# manyObj1BinaryLabel = p2('manyObj1Binary.pgm')
# cv2.imwrite("manyObj1BinaryLabel.pgm", manyObj1BinaryLabel)
# dataBaseP3 = p3("newLabel.pgm")
# dataBaseP4 = p3("manyObj1BinaryLabel.pgm")


def p4(labels_in, database_in): # return overlays_out
    dataBaseP3 = database_in
    image = cv2.imread(labels_in, 0)
    dataBaseP4 ,pic = p3(labels_in)
    roundnessP3 = []
    roundnessP4 = []
    for i in range(len(dataBaseP4)):
        roundnessP4.append(dataBaseP4[i]['Roundness'])
    for i in range(len(dataBaseP3)):
        roundnessP3.append(dataBaseP3[i]['Roundness'])
    found = []
    for i in range(len(roundnessP3)):
        for j in range(len(roundnessP4)):
            if abs(roundnessP3[i] - roundnessP4[j])< 0.03:
                found.append(j)

    for i in range(len(found)):
        i = found[i]
        cv2.circle(image, (dataBaseP4[i]['Position'][0], dataBaseP4[i]['Position'][1]), 10, (255, 255, 255))
        cv2.line(image, (dataBaseP4[i]['Position'][0], dataBaseP4[i]['Position'][1]),
                 (dataBaseP4[i]['Position'][0] + 50, dataBaseP4[i]['Position'][1] + int(np.tan(dataBaseP4[i]['Orientation']) * 50)),
                 (255, 255, 255))




    return image

