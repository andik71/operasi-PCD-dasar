# Andika Dwiyanto_F55120119
import cv2 # Import Modul OpenCV

# Membaca Data Citra
img = cv2.imread('coronavirus.jpg', 0)
negatif = 255 - img  # Trasnformasi Citra Negatif

# Menampilkan Hasil Pengolahan Citra
cv2.imshow('Citra Asli', img)
cv2.imshow('Citra Negatif', negatif)

cv2.waitKey(0) # Stop Execution by pressing ESC
cv2.destroyAllWindows() # Force close all Windows that currently open
