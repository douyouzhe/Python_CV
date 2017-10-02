import numpy as np
np.set_printoptions(threshold=np.nan)
import cv2
import math
import matplotlib.pyplot as plt
from P1 import p1
from P2 import p2
from P3 import p3
from P4 import p4

pic = p1('two_objects.pgm',125)
cv2.imwrite("twoObjBinaryImage.pgm", pic)

pic = p2('twoObjBinaryImage.pgm')
cv2.imwrite("twoObjLabeled.pgm", pic)

outterDicForTwo, pic = p3('twoObjLabeled.pgm')
cv2.imwrite("twoObjOverlayOut.pgm", pic)

manyObj1Binary = p1("many_objects_1.pgm", 125)
cv2.imwrite("manyObj1Binary.pgm", manyObj1Binary)
manyObj1BinaryLabel = p2('manyObj1Binary.pgm')
cv2.imwrite("manyObj1BinaryLabel.pgm", manyObj1BinaryLabel)
outImage = p4("manyObj1BinaryLabel.pgm",outterDicForTwo)
cv2.imwrite("recognizedObjs1.pgm", outImage)

manyObj2Binary = p1("many_objects_2.pgm", 125)
cv2.imwrite("manyObj2Binary.pgm", manyObj2Binary)
manyObj2BinaryLabel = p2('manyObj2Binary.pgm')
cv2.imwrite("manyObj2BinaryLabel.pgm", manyObj2BinaryLabel)
outImage = p4("manyObj2BinaryLabel.pgm",outterDicForTwo)
cv2.imwrite("recognizedObjs2.pgm", outImage)