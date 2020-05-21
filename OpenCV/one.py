import cv2 as cv
import os

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
print(img[20, 30])  # 读取像素可以通过行坐标和列坐标来进行访问，灰度图像直接返回灰度值，彩色图像则返回B、G、R三个分量
blue = img[20, 30, 0]  # 在获取彩色图片像素时的第二个参数 0|1|2 的含义是获取 BGR 三个通道的像素。
green = img[20, 30, 1]
red = img[20, 30, 2]
print(blue, green, red)
cv.imshow('demo', img)  # 显示图片,cv.imshow(窗口名, 图像名)
cv.waitKey(0)  # 等待输入，如果不等待输入，整个窗体将会一闪而过。
"""
cv.waitKey() 是一个键盘绑定函数。其参数是以毫秒为单位的时间。
该函数等待任何键盘事件指定的毫秒。如果您在这段时间内按下任何键，程序将继续运行。
如果 0 被传递，它将无限期地等待一次敲击键。
"""
cv.destroyAllWindows()  # 删除所有窗口，cv.destroyWindows() 删除指定的窗口
cv.imwrite('new_tower.jpg', img)  # 图片写入,cv.imwrite(文件地址, 文件名)
