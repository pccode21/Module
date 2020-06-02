import cv2 as cv
import os
from matplotlib import pyplot as plt

os.chdir(r'.\Module\OpenCV')
print('OpenCV的当前版本：', cv.getVersionString())  # 查看版本信息
img = cv.imread('tower.jpg', 1)  # 读取图片
"""
img = cv.imread(文件名,[,参数])
第二个参数是一个标志，它指定了读取图像的方式。
cv.IMREAD_COLOR： 加载彩色图像，任何图像的透明度都会被忽视，如果不传参数，这个值是默认值。
cv.IMREAD_GRAYSCALE：以灰度模式加载图像。
cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
注意：这三个标志可以简化为 1 、 0 、 -1 。
"""
"""
print(img[20, 30])  # 读取像素可以通过行坐标和列坐标来进行访问，灰度图像直接返回灰度值，彩色图像则返回B、G、R三个分量
blue = img[20, 30, 0]  # 在获取彩色图片像素时的第二个参数 0|1|2 的含义是获取 BGR 三个通道的像素。
green = img[20, 30, 1]
red = img[20, 30, 2]
print(blue, green, red)
# 像素依次赋值
img[20, 30, 0] = 255
img[20, 30, 1] = 255
img[20, 30, 2] = 255
print(img[20, 30])
# 也可以通过数组直接对像素点一次赋值：
img[20, 30] = [0, 0, 0]
print(img[20, 30])
img[0:200, 50:100] = [255, 255, 255]  # 对一个区域的像素进行赋值,全都赋值成为白色
"""
# 以下使用使用 Numpy 操作
# 读取像素，调用方式：返回值 = 图像.item(位置参数)
gray_img = cv.imread("tower.jpg", 0)
print(gray_img.item(20, 30))
blue = img.item(20, 30, 0)
green = img.item(20, 30, 1)
red = img.item(20, 30, 2)
print(blue, green, red)
# 修改像素，调用方式：图像.itemset(位置, 新值)
img.itemset((20, 30, 0), 255)
img.itemset((20, 30, 1), 255)
img.itemset((20, 30, 2), 255)
print(img[20, 30])
img[0:200, 50:100] = [255, 255, 255]  # 对一个区域的像素进行赋值,全都赋值成为白色
# cv.imshow('demo', img)  # 显示图片,cv.imshow(窗口名, 图像名)
# cv.waitKey(0)  # 等待输入，如果不等待输入，整个窗体将会一闪而过。
"""
cv.waitKey() 是一个键盘绑定函数。其参数是以毫秒为单位的时间。
该函数等待任何键盘事件指定的毫秒。如果您在这段时间内按下任何键，程序将继续运行。
如果 0 被传递，它将无限期地等待一次敲击键。
"""
# cv.destroyAllWindows()  # 删除所有窗口，cv.destroyWindows() 删除指定的窗口
# cv.imwrite('new_tower.jpg', img)  # 图片写入,cv.imwrite(文件地址, 文件名)
# 以下使用使用Matplotlib 显示图像
# 直接使用 Matplotlib 来显示 OpenCV 读入的图像，会得到下面这个蓝色图片
# 这是因为对于 OpenCV 的像素是 BGR 顺序，然而 Matplotlib 所遵循的是 RGB 顺序。
# 有三种方法可以完成 BGR 至 RGB 的转换
b, g, r = cv.split(img)
img2 = cv.merge([r, g, b])
"""
还有以下两种方式可以修改：
img3=img[:,:,::-1]
img4=cv.cvtColor(img, cv.COLOR_BGR2RGB)
"""
plt.imshow(img2)
plt.axis("off")
plt.savefig('new_tower.png', dpi=400)
plt.show()
