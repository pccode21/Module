"""
交叉表（简写为crosstab）是数据透视表的一个特殊情况，计算的是分组中的频率
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, 2, 2, 2],
                   'B': [3, 3, 4, 4, 4],
                   'C': [1, 1, np.nan, 1, 1]})
print(df, '\n')
print(pd.crosstab(df['A'], df['B']), '\n')  # 在默认情况下，当只以两个series为参数时，它会以A列的唯一值为索引，统计B列中唯一值分别出现的频率
# 当前使用了默认的normalize=False参数
print(pd.crosstab(df['A'],df['B'], normalize=True), '\n')  # 指定normalize=True,输出的是占总频数的百分比
# 当传入values参数时和aggfunc参数时，会根据所传数值和聚合函数来进行聚合，相当于只使用A和B列界定分组，计算values聚合值：
print(pd.crosstab(df['A'], df['B'], values=df['C'], aggfunc=np.sum), '\n')  # 默认margins=False
print(pd.crosstab(df['A'], df['B'], values=df['C'], aggfunc=np.sum, margins=True))  # 使用margins=True参数时,会添加行/列边距
"""
   A  B    C
0  1  3  1.0
1  2  3  1.0
2  2  4  NaN
3  2  4  1.0
4  2  4  1.0

B  3  4
A
1  1  0
2  1  3

B    3    4
A
1  0.2  0.0
2  0.2  0.6

B    3    4
A
1  1.0  NaN
2  1.0  2.0

B      3    4  All
A
1    1.0  NaN  1.0
2    1.0  2.0  3.0
All  2.0  2.0  4.0
"""
