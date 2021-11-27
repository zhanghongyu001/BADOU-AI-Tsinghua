import numpy as np
import cv2
def bil(img, out_dim):
    s_h, s_w, channel = img.shape
    d_h, d_w = out_dim[1], out_dim[0]
    print("s_h, s_w = ", s_h, s_w)
    print("d_h, d_w = ", d_h, d_w)
    if s_h == d_h and s_w == d_w:
        return img.copy()
    dst_img = np.zeros((d_h, d_w, 3),np.uint8)
    sca_x, sca_y = float(s_w) / d_w, float(s_h) / d_h
    for i in range(3):
        for d_y in range(d_h):
            for d_x in range(d_w):
                sr_x = (d_x + 0.5) * sca_x - 0.5
                sr_y = (d_y + 0.5) * sca_y - 0.5

                sr_x0 = int(np.floor(sr_x))
                sr_x1 = min(sr_x0 + 1, s_w - 1)
                sr_y0 = int(np.floor(sr_y))
                sr_y1 = min(sr_y0 + 1, s_h - 1)

                temp0 = (sr_x1 - sr_x) * img[sr_y0, sr_x0, i] + (sr_x - sr_x0) * img[sr_y0, sr_x1, i]
                temp1 = (sr_x1 - sr_x) * img[sr_y1, sr_x0, i] + (sr_x - sr_x0) * img[sr_y1, sr_x1, i]
                dst_img[d_y, d_x, i] = int((sr_y1 - sr_y) * temp0 + (sr_y - sr_y0) * temp1)

    return dst_img

img = cv2.imread('lenna.png')
dst = bil(img, (700, 700))
cv2.imshow('bil', dst)
cv2.waitKey()