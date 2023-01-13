from re import I
import cv2
import numpy as np

ctr = cv2.imread("luffy.jpg")

b = ctr[:, :, 0]
g = ctr[:, :, 1]
r = ctr[:, :, 2]

b, g, r = cv2.split(ctr)

gray = cv2.cvtColor(ctr, cv2.COLOR_BGR2GRAY)

hp = np.zeros((len(gray), len(gray[0])))
traceholder = 157
for b in range(len(gray)):
    for k in range(len(gray[0])):
        if gray[b, k] <= 200:
            hp[b, k] = 0
        else:
            hp[b, k] = 1


cv2.imshow("citra", hp)
cv2.waitKey()
