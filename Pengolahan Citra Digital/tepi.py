import cv2
import numpy as np
import matplotlib.pyplot as plt

gambar = cv2.imread("luffy.jpg")
gambar = cv2.resize(gambar, (640, 406))

b = gambar[:, :, 0]
g = gambar[:, :, 1]
r = gambar[:, :, 2]

jml_brs = len(gambar)
jml_klm = len(gambar[0])

new = np.zeros((jml_brs, jml_klm, 3))
cv_grey = np.zeros((jml_brs, jml_klm))
kernelx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernely = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
menajamkan = np.zeros((jml_brs, jml_klm))

# konversi greysclae
for i in range(jml_brs):
    for j in range(jml_klm):
        cv_grey[i, j] = round(
            0.114 * b[i, j] + 0.587 * g[i, j] + 0.299 * r[i, j])

cv_grey = cv_grey.astype(np.uint8)

# temp_konvolusi
for brs in range(1, jml_brs-1):
    for klm in range(1, jml_klm-1):
        konvolusi = 0

        for i in range(2):
            if (i == 0):
                kernel = kernelx
            else:
                kernel = kernely

            a = cv_grey[brs-1, klm-1] * kernel[0, 0]  # kiri atas
            b = cv_grey[brs-1, klm] * kernel[0, 1]  # tengah atas
            c = cv_grey[brs-1, klm+1] * kernel[0, 2]  # kanan atas
            d = cv_grey[brs, klm-1] * kernel[1, 0]  # kiri
            e = cv_grey[brs, klm] * kernel[1, 1]  # tengah matriks
            f = cv_grey[brs, klm+1] * kernel[1, 2]  # kanan
            g = cv_grey[brs+1, klm-1] * kernel[2, 0]  # kiri bawah
            h = cv_grey[brs+1, klm] * kernel[2, 1]  # tengah bawah
            i = cv_grey[brs+1, klm+1] * kernel[2, 2]  # kanan bawah

        # hitung total nilai dalam kernel
        jum_kernel = np.sum(kernel)
        if (jum_kernel == 0):
            jum_kernel = 1
        # hitung hasil temp_konvolusi
        temp_konvolusi = np.round(
            (a + b + c + d + e + f + g + h + i) / jum_kernel)
        # perbaiki hasil temp_konvolusi jika di luar rentang 0-255
        if (temp_konvolusi < 0):
            temp_konvolusi = 0
        if (temp_konvolusi > 255):
            temp_konvolusi = 255
        # isikan hasil temp_konvolusi ke matriks_baru
        menajamkan[brs, klm] = temp_konvolusi + konvolusi
menajamkan = menajamkan.astype(np.uint8)

cv2.imshow('grey', cv_grey)
cv2.imshow('menajamkan', menajamkan)
cv2.waitKey()
