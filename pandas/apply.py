"""
https://blog.csdn.net/stone0823/article/details/100008619
"""
import pandas as pd
import numpy as np
import datetime as dt

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
df = pd.DataFrame(matrix, index=list('abc'), columns=list('xyz'))
df1 = df.apply(np.square)  # 所有的元素都执行平方运算
print(df1)
df2 = df.apply(lambda x: np.square(x) if x.name == 'x' else x)  # 将 x 列进行平方运算
print(df2)
df3 = df.apply(lambda x: np.square(x) if x.name in ['x', 'y'] else x)  # 对 x 和 y 列进行平方运算
print(df3)
df4 = df.apply(lambda x: np.square(x) if x.name == 'a' else x, axis=1)  # 对第一行 （a 标签所在行）进行平方运算，默认情况下 axis=0 表示按列，axis=1 表示按行。
print(df4)
wbs = {
    "wbs": ["job1", "job2", "job3", "job4"],
    "date_from": ["2019-04-01", "2019-04-07", "2019-05-16","2019-05-20"],
    "date_to": ["2019-05-01", "2019-05-17", "2019-05-31", "2019-06-11"]
    }
df5 = pd.DataFrame(wbs)
elapsed= df5['date_to'].apply(pd.to_datetime) - df5['date_from'].apply(pd.to_datetime)
df5['elapsed'] = elapsed.apply(lambda x : x.days)
print(df5)
