import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_H = 800
IMAGE_W = 600

src = np.float32([[1167,0], [19,521], [850,1021], [1831,0]])
dst = np.float32([[0,0], [0,IMAGE_H], [IMAGE_W,IMAGE_H], [IMAGE_W, 0]])
M = cv2.getPerspectiveTransform(src, dst) 
Minv = cv2.getPerspectiveTransform(dst, src) 

img = cv2.imread('tst.png')
warped_img = cv2.warpPerspective(img, M, (IMAGE_W, IMAGE_H))
# cv2.imshow('tst',warped_img)
plt.imshow(warped_img)
plt.show()