import pandas as pd
import numpy as np

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()  # 取出列表中的唯一值，并组成新列表
print(uniques)
print(dict(obj.value_counts()))  # 以列表的值为健，以列表中同一个值的数量为值创建字典
mask = obj.isin(['b', 'c'])
print(list(obj[mask]))  # 在原有列表中筛选出包含['b', 'c']的新列表
obj1 = pd.Series(range(6), index=['a', 'a', 'b', 'b', 'a', 'c'])
print(obj1['b'])  # 'b'在列表中的位置
print(obj1.loc['a'])  # 'a'在列表中的位置
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                     'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 2, 4, 4]})
# 以DataFrame中的值为index,以DataFrame中的健为columns，以值在各健中出现的次数为值，将0填充NaN创建新的DataFrame
result = data.apply(pd.value_counts).fillna(0)
print(result)
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
print(pd.Index(unique_vals).get_indexer(to_match))  # 表示，to_match 中的字符，在 unoque_vals 中的位置索引
"""
['c' 'a' 'd' 'b']
{'a': 3, 'c': 3, 'b': 2, 'd': 1}
['c', 'b', 'b', 'c', 'c']
b    2
b    3
dtype: int64
a    0
a    1
a    4
dtype: int64
   Qu1  Qu2  Qu3
1  1.0  1.0  1.0
2  0.0  2.0  1.0
3  2.0  2.0  0.0
4  2.0  0.0  2.0
5  0.0  0.0  1.0
[0 2 1 1 0 2]
"""
