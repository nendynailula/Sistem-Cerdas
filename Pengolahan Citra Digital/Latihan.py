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

rotasi = -5
rotasi_radian = 22/7 * rotasi / 180

new = np.zeros((jml_brs, jml_klm, 3))
cv_grey = np.zeros((jml_brs, jml_klm))
grey_brightness = np.zeros((jml_brs, jml_klm))
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
menajamkan = np.zeros((jml_brs, jml_klm))

pivot_brs = round(jml_brs / 2)
pivot_klm = round(jml_klm / 2)

for brs_b in range(jml_brs):
    for klm_b in range(jml_klm):
        brs = pivot_brs + (brs_b - pivot_brs) * np.cos(rotasi_radian) - \
            (klm_b - pivot_klm) * np.sin(rotasi_radian)
        klm = pivot_klm + (brs_b - pivot_brs) * np.sin(rotasi_radian) + \
            (klm_b - pivot_klm) * np.cos(rotasi_radian)

        brs = round(brs)
        klm = round(klm)
        if (brs < jml_brs and brs > 0):
            if (klm < jml_klm and klm > 0):
                new[brs_b, klm_b] = gambar[brs, klm]
new = new.astype(np.uint8)
# konversi greysclae
for i in range(jml_brs):
    for j in range(jml_klm):
        cv_grey[i, j] = round(
            0.114 * b[i, j] + 0.587 * g[i, j] + 0.299 * r[i, j])

cv_grey = cv_grey.astype(np.uint8)
# brightness
for i in range(jml_brs):
    for j in range(jml_klm):
        pxl = cv_grey[i, j] + 55
        if pxl > 255:
            grey_brightness[i, j] = 255
        else:
            grey_brightness[i, j] = pxl
grey_brightness = grey_brightness.astype(np.uint8)

# konvolusi
for brs in range(1, jml_brs-1):
    for klm in range(1, jml_klm-1):
        # baca dan kalikan matriks 3x3 dari gambar awal dengan kernel 3x3
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
        # hitung hasil konvolusi
        konvolusi = np.round((a + b + c + d + e + f + g + h + i) / jum_kernel)
        # perbaiki hasil konvolusi jika di luar rentang 0-255
        if (konvolusi < 0):
            konvolusi = 0
        if (konvolusi > 255):
            konvolusi = 255
        # isikan hasil konvolusi ke matriks_baru
        menajamkan[brs, klm] = konvolusi
menajamkan = menajamkan.astype(np.uint8)

cv2.imshow('lama', gambar)
cv2.imshow('rotasi', new)
cv2.imshow('grey', cv_grey)
cv2.imshow('brightness', grey_brightness)
cv2.imshow('menajamkan', menajamkan)
cv2.waitKey()
