"""
where(condition,x=None,y=None):
第一个参数：条件
第二个参数：条件满足的返回值
第三个参数：条件不满足的返回值

extract(condition,x=None)
第一个参数：条件
第二个参数：返回的值
"""
import numpy as np

s = np.array([1,2,3,4,3,2,1,2,2,4,6,7,2,4,8,4,5])
s1 = np.where(s > 3, s, -1)  # 大于3返回元素本身，不大于3返回-1
print(s1)
s2 = np.extract(s > 3, s)  # 筛选数组中值大于3的元素
print(s2)
