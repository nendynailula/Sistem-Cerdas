import cv2
import numpy as np

gambar = cv2.imread('luffy.jpg')

b = gambar[:, :, 0]
g = gambar[:, :, 1]
r = gambar[:, :, 2]

b, g, r = cv2.split(gambar)

row = len(gambar)
col = len(gambar[0])

cv_grey = np.zeros((row, col))

for rw in range(row):
    for cl in range(col):
        # print(r[row,col])
        cv_grey[rw, cl] = round(
            0.114 * b[rw, cl] + 0.587 * g[rw, cl] + 0.299 * r[rw, cl])

cv_grey = cv_grey.astype(np.uint8)

cv2.imshow('blue', b)
cv2.imshow('green', r)
cv2.imshow('red', r)
# cv2.imshow('greyscale', cv_grey)
cv2.waitKey()
