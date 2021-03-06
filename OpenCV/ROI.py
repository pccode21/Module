import cv2 as cv
import os
import numpy as np

os.chdir(r'.\Module\OpenCV')
color_img = cv.imread('tower.jpg', 1)
print(color_img.shape)  # 图像的形状可以通过 shape 关键字进行获取，使用 shape 关键的后，获取的信息包括行数、列数、通道数的元组。
gray_img = cv.imread('tower.jpg', 0)
print(gray_img.shape)  # 如果是灰度图片，只会返回图像的行数和列数
print(color_img.size)  # 图像的像素数量可以通过关键字 size 进行获取
print(gray_img.size)  # 灰度图片的像素数量是要小于彩色图片的，具体的关系是 1/3
print(color_img.dtype, gray_img.dtype)  # 图像类型是通过关键字 dtype 获取的，通常返回 uint8,这个属性在彩色图片和灰度图片中是保持一致的
img = cv.imread('tower.jpg', -1)
top = img[260:660, 350:750]  # 通过像素矩阵可以直接得到 ROI 区域
img[0:400, 0:400] = top  # 要把这两张图像合成一张图像，可以对图像进行区域赋值，指定的区域要和 ROI 的区域一样大，否则会报一个 ValueError 的错误
"""
# b, g, r = cv.split(img)  # 使用 split() 函数获取图像通道
# 注意： split() 函数是一项耗时的操作（就时间而言）。因此，仅在必要时才这样做。否则请进行Numpy索引。
# 还可以通过索引进行获取，代码如下：
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
img[:, :, 2] = 0  # 将所有红色像素都设置为零，无需先拆分通道，索引更快
cv.imshow('B', b)
cv.imshow('G', g)
cv.imshow('R', r)
# cv.imshow('demo', img)
"""
rows, cols, chn = img.shape
b = img[:, :, 0]  # 提取 B 颜色通道
g = np.zeros((rows, cols), dtype=img.dtype)  # G 通道全部设置为 0
r = np.zeros((rows, cols), dtype=img.dtype)  # R 通道全部设置为 0
m = cv.merge([b, g, r])
cv.imshow('merge', m)
cv.waitKey(0)
cv.destroyAllWindows()
