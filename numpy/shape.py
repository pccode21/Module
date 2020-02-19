# numpy.naarray.shape 返回一个元组（a,b） a是读取数组的第一维度（行）的长度，b是读取数组的第二维度（列）的长度
# numpy.naarray.shape[i]  i=0表示读取数组的第一维度（行）的长度，i=1表示读取数组的第二维度（列）的长度
import numpy as np

a = ([2, 3, 1], [4, 5, 2])  # 元组用() 元组不可以转为字典
print(a)
print(type(a))
print(list(a))  # 元组转换为列表，列表用[]
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
([2, 3, 1], [4, 5, 2])
<class 'tuple'>
[[2, 3, 1], [4, 5, 2]]
<class 'list'>
{2: 4, 3: 5, 1: 2}
<class 'dict'>
[[2 3 1]
 [4 5 2]]
<class 'numpy.ndarray'>
2
3
(2, 3)
[[2 4]
 [3 5]
 [1 2]]
3
2
(3, 2)
"""
print(np.array([1650, 3]))
