from skimage.color import rgb2gray
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lenna.png")
h, w = img.shape[:2]
img_g = np.zeros([h, w], img.dtype)
for i in range(h):
    for j in range(w):
        m = img[i, j]
        img_g[i, j] = int(m[0] * 0.11 + m[1] * 0.59 + m[2] * 0.3)
print(img_g)
print("show gray: %s" % img_g)
cv2.imshow("gray", img_g)

plt.subplot(221)
img = plt.imread("lenna.png")
plt.imshow(img)
print("image lenna")
print(img)


img_gr = rgb2gray(img)
plt.subplot(222)
plt.imshow(img_gr, cmap='gray')
print("image gray")
print(img_gr)

img_binary = np.where(img_gr >= 0.5, 1, 0)
print("imge_bin")
print(img_binary)
print(img_binary.shape)

plt.subplot(223)
plt.imshow(img_binary, cmap='gray')
plt.show()