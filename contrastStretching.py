# Andika Dwiyanto_F55120119
# Package Numpy | Package Matplotlip | Module Copy | Package Pillow
import numpy; import matplotlib.pyplot as plt; from copy import deepcopy; from PIL import Image

# Mendefinisikan fungsi dengan parameter (rgb)
def getGrayColor(rgb):
    return rgb[0] # Tipe Data Array

# Mendefinisikan fungsi dengan parameter (color)
def setGrayColor(color):
    return [color, color, color] # Tipe data Array dengan 3 indeks

# Membaca data dengan menggunakan operator Pillow
img = Image.open('coronavirus.jpg')
img = numpy.asarray(img) # Mendefiniskan bentuk citra sebagai array

# Daftar dari Copy tidak mendefinisikan sebagai referensi
ct = deepcopy(img)

# Deklarasi variabel dengan nilai sebagai berikut:
r1 = 100
s1 = 50
r2 = 150
s2 = 200

# Operator Contrast Stretching
for i in range(len(img)): # Data Citra dibaca dan dihitung panjang objeknya
    for j in range(len(img[i])):
        x = getGrayColor(img[i][j]) # Mendefinisikan nilai variabel X dengan fungsi dari getGrayColor
        if(0 <= x and x <= r1):     # Kondisi if-elseif
            ct[i][j] = setGrayColor(s1/r1 * x)
        elif(r1 < x and x <= r2):
            ct[i][j] = setGrayColor(((s2 - s1) / (r2 - r1)) * (x - r1) + s1)
        elif(r2 < x and x <= 255):
            ct[i][j] = setGrayColor(((255 - s2) / (255 - r2)) * (x - r2) + s2)

# Mendefinisikan Multiplot dengan nilai mengikuti objek yang nantinya akan ditampilkan dari kiri ke kanan
plt.subplot(2, 2, 1); plt.title('Citra Asli'); plt.imshow(img)
plt.subplot(2, 2, 2); plt.title('Hasil Contrast Stretching'); plt.imshow(ct)
plt.show() # Menampilkan plot
