import pandas as pd
import numpy as np

d = {"customer": ["A", "B", "C", "D"], "sales":[1100, "950.5RMB", "$400", " $1250.75"]}
df = pd.DataFrame(d)
print(df)
df["sales"] = df["sales"].replace('[$, RMB]', '', regex=True).astype('float')
# 使用正则替换，将要替换的字符放到列表中 [$,RMB]，替换为空字符，即 "",最后使用 astype 转为 float
print(df)
s = pd.DataFrame(list('ascaazsd'))
print(s)
print(s.replace('a', 'new_a'))  # 替换单个
print(s.replace(['a', 's'], np.nan))  # 传入列表，替换多个
print(s.replace({'a': 'new_a', 's': 'new_s'}))  # 传入字典，分别替换
"""
  customer      sales
0        A       1100
1        B   950.5RMB
2        C       $400
3        D   $1250.75
  customer    sales
0        A  1100.00
1        B   950.50
2        C   400.00
3        D  1250.75
"""
