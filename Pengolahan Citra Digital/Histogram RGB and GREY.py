from cgitb import grey
import cv2
import numpy as np
import matplotlib.pyplot as plt

# membaca citra digital dari komputer
gmb = cv2.imread("luffy.jpg")
grey = cv2.cvtColor(gmb, cv2.COLOR_BGR2GRAY)
# split channel dengan manual
b = gmb[:, :, 0]
g = gmb[:, :, 1]
r = gmb[:, :, 2]

# split channel otomatis
b, g, r = cv2.split(gmb)

jml_baris = len(gmb)
jml_kolom = len(gmb[0])

histogram_b = np.zeros(256)
histogram_g = np.zeros(256)
histogram_r = np.zeros(256)
histogram_grey = np.zeros(256)

print(len(b))
print(len(b[0]))

for i in range(jml_baris):
    for j in range(jml_kolom):
        pixel1 = b[i, j]
        # menampilkan channel blue
        histogram_b[pixel1] += 1 / (jml_baris*jml_kolom)

        pixel2 = g[i, j]
        # menampilkan channel green
        histogram_g[pixel2] += 1 / (jml_baris*jml_kolom)

        pixel3 = r[i, j]
        # menampilkan channel red
        histogram_r[pixel3] += 1 / (jml_baris*jml_kolom)

        pixel4 = grey[i, j]
        histogram_grey[pixel4] += 1 / (jml_baris*jml_kolom)
# memunculkan histogram
print(histogram_b)
print(histogram_g)
print(histogram_r)
print(histogram_grey)

plt.plot(histogram_b)
plt.plot(histogram_g)
plt.plot(histogram_r)
plt.plot(histogram_grey)
plt.show()
cv2.imshow('lihat gambar', gmb)
cv2.waitKey()
