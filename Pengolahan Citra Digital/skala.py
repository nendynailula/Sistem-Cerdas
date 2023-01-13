import cv2
import numpy as np
import matplotlib.pyplot as plt

gambar = cv2.imread('luffy.jpg')

jml_baris = len(gambar)
jml_kolom = len(gambar[0])

skala = 1.5

jml_baris_baru = round(jml_baris * skala)
jml_kolom_baru = round(jml_kolom * skala)
matriks_baru = np.zeros((jml_baris_baru, jml_kolom_baru, 3))

for brs_baru in range(jml_baris_baru):
    for klm_baru in range(jml_kolom_baru):
        brs = int(brs_baru / skala)
        klm = int(klm_baru / skala)

        matriks_baru[brs_baru, klm_baru] = gambar[brs, klm]
# konversi
matriks_baru = matriks_baru.astype(np.uint8)

cv2.imshow('gambar', gambar)
cv2.imshow('gambar baru', matriks_baru)
cv2.waitKey()
