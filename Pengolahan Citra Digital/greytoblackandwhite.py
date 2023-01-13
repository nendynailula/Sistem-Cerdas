from cgitb import grey
import cv2
import os

citra = cv2.imread("luffy.jpg")
grey = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)
ret, biner = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('gambar', biner)
cv2.waitKey()
