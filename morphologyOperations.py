# Andika Dwiyanto_F55120119
# Modul yang digunakan: OpenCV | Numpy
import cv2 as cv; import numpy as np; import sys

img = cv.imread('j.png', 0)
cv.imshow('Citra Asli', img)

kernel = np.ones((5, 5), np.uint8)

erosion = cv.erode(img, kernel, iterations = 1)
cv.imshow('Erosion', erosion)

dilation = cv.dilate(img, kernel, iterations = 1)
cv.imshow('Dilasi', dilation)

kernel1 = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel1)
cv.imshow('Opening', opening)

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow('Closing', closing)

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('Gradient', gradient)

sys.exit('Program has stopped')
