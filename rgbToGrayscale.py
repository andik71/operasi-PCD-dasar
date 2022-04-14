# Andika Dwiyanto_F55120119
# Import modul cv2.resize() | OpenCv-Python | Numpy | Matplotlib
import cv2; import numpy as np; import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread('painting.jpg', cv2.IMREAD_UNCHANGED)
print('Original Dimensions : ', img.shape) # Citra memiliki dimensi 1200 x 1510 piksel

# Proses Scalling Downscale
scale_percent = 60  # percent of original size
width = int(img.shape[1] * scale_percent / 130)
height = int(img.shape[0] * scale_percent / 130)

# Dimensi gambar diperkecil dimensinya sebanyak 130% dari dimensi aslinya
dim = (width, height)

# Resize Operator
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
print('Resized Dimensions : ', resized.shape)

# Grayscale Operator
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Menampilkan Hasil
cv2.imshow("Citra Asli", img); cv2.imshow("Citra Scalling", resized); cv2.imshow("Citra Grayscale", gray)

cv2.waitKey(0) # Stop Execution by pressing ESC
cv2.destroyAllWindows() # Force close all Windows that currently open