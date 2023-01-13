import cv2
import numpy as np
import matplotlib.pyplot as plt

gambar = cv2.imread('luffy.jpg')

jml_baris = len(gambar)
jml_kolom = len(gambar[0])

flip_vt = 1
flip_hz = 0

matriks_baru = np.zeros((jml_baris, jml_kolom, 3))

for brs in range(jml_baris):
    for klm in range(jml_kolom):
        if (flip_hz == 1):
            brs_baru = jml_baris - klm - 1
        else:
            klm_baru = klm

        if (flip_vt == 1):
            brs_baru = jml_baris - brs - 1

        else:
            brs_baru = brs

        matriks_baru[brs_baru, klm_baru] = gambar[brs, klm]
# konversi citra translasi menjadi uint8
matriks_baru = matriks_baru.astype(np.uint8)

cv2.imshow('gambar', matriks_baru)
cv2.waitKey()
