# numpy.naarray.shape 返回一个元组（a,b） a是读取数组的第一维度（行）的长度，b是读取数组的第二维度（列）的长度
# numpy.naarray.shape[i]  i=0表示读取数组的第一维度（行）的长度，i=1表示读取数组的第二维度（列）的长度
import numpy as np

a = ([4, 2, 3], [5, 1, 2])  # 元组用() 元组不可以转为字典
b = np.array(a, dtype=np.int)  # 将a转换成数组，np.int 指定数据类型
b1 = np.sort(b)  # 默认将数组b按行排序
b2 = np.sort(b, axis=None)  # axis=None表示将数组展平，并排序
b3 = np.sort(b, axis=0)  # 将数组b按列排序
b4 = b.flatten()  # 将数组b展平，flatten()是一个展开性质的函数，将多维的数组进行展开成1行的一维数组
b5 = ['saw', 'small', 'He', 'foxes', 'six']
b5.sort(key=len)  # 二级排序key，可以用这个key进行排序，按长度对字符串进行排序
c = np.zeros((3, 4))  # 数据全为0，3行4列的数组
d = np.ones((3, 4), dtype=np.float)  # 数据全为1，3行4列的数组
e = np.arange(10, 20, 2)  # 用 arange 创建连续数组:10-19 的数据，2步长
f = np.arange(0, 12).reshape((3, 4))  # 使用 reshape 改变数组的形状：3行4列，0到11
print(f)
print('sum=', np.sum(f, axis=0))  # 当axis的值为0的时候，将会以列作为查找单元，求数组f中各列的和
print('min=', np.min(f, axis=1))  # 当axis的值为1的时候，将会以行作为查找单元，求数组f中各行的最小值
print('max=', np.max(f, axis=1))  # 当axis的值为1的时候，将会以行作为查找单元，求数组f中各行的最大值
g = np.linspace(1, 10, 20)  # 用 linspace 创建线段型数组:# 开始端1，结束端10，且分割成20个数据，生成线段
h = np.linspace(1, 10, 20).reshape((5, 4))   # 使用 reshape 改变数组的形状：5行4列，开始端1，结束端10，且分割成20个数据，生成线段，开始端1，结束端10，且分割成20个数据，生成线段
i = np.linspace(1, 10, 20).reshape(-1, 1)  # 使用 reshape 改变数组的形状：1列
print(c)
print(d)
print(e)
print(g)
print(h)
print(i)
print(a)
print(type(a))
print(list(a))  # 元组转换为列表，列表用[]
print(b)  # 输出数组，矩阵是数组的分支
print(b1)
print(b2)
print(b3)
print(b4)
print(b5)
print(b.ndim)  # 输出数组的维度
print(b.size)  # 输出数组的元素个数
print(type(list(a)))
print(dict(zip(list(a)[0], list(a)[1])))  # 列表转换为字典，字典用{}
print(type(dict(zip(list(a)[0], list(a)[1]))))
print(np.array(a))
print(type(np.array(a)))
print(np.array(a).shape[0])
print(np.array(a).shape[1])
print(np.array(a).shape)
print(np.array(a).T)
print(np.array(a).T.shape[0])
print(np.array(a).T.shape[1])
print(np.array(a).T.shape)
"""
结果输出：
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
sum= [12 15 18 21]
min= [0 4 8]
max= [ 3  7 11]
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
[10 12 14 16 18]
[ 1.          1.47368421  1.94736842  2.42105263  2.89473684  3.36842105
  3.84210526  4.31578947  4.78947368  5.26315789  5.73684211  6.21052632
  6.68421053  7.15789474  7.63157895  8.10526316  8.57894737  9.05263158
  9.52631579 10.        ]
[[ 1.          1.47368421  1.94736842  2.42105263]
 [ 2.89473684  3.36842105  3.84210526  4.31578947]
 [ 4.78947368  5.26315789  5.73684211  6.21052632]
 [ 6.68421053  7.15789474  7.63157895  8.10526316]
 [ 8.57894737  9.05263158  9.52631579 10.        ]]
[[ 1.        ]
 [ 1.47368421]
 [ 1.94736842]
 [ 2.42105263]
 [ 2.89473684]
 [ 3.36842105]
 [ 3.84210526]
 [ 4.31578947]
 [ 4.78947368]
 [ 5.26315789]
 [ 5.73684211]
 [ 6.21052632]
 [ 6.68421053]
 [ 7.15789474]
 [ 7.63157895]
 [ 8.10526316]
 [ 8.57894737]
 [ 9.05263158]
 [ 9.52631579]
 [10.        ]]
([4, 2, 3], [5, 1, 2])
<class 'tuple'>
[[4, 2, 3], [5, 1, 2]]
[[4 2 3]
 [5 1 2]]
[[2 3 4]
 [1 2 5]]
[1 2 2 3 4 5]
[[4 1 2]
 [5 2 3]]
[4 2 3 5 1 2]
['He', 'saw', 'six', 'small', 'foxes']
2
6
<class 'list'>
{4: 5, 2: 1, 3: 2}
<class 'dict'>
[[4 2 3]
 [5 1 2]]
<class 'numpy.ndarray'>
2
3
(2, 3)
[[4 5]
 [2 1]
 [3 2]]
3
2
(3, 2)
"""
print(np.array([1650, 3]))
