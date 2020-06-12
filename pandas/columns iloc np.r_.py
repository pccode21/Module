import pandas as pd
import numpy as np

df = pd.read_csv('https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv?accessType=DOWNLOAD&bom=true&format=true')
col_mapping = [f"{c[0]}: {c[1]}" for c in enumerate(df.columns)]  # 这是一个简单的列表理解，可以建立所有列及其索引的参考列表。
col_mapping_dict = {c[0]:c[1] for c in enumerate(df.columns)}  # 如果您想重命名一堆列，则可以使用字典理解来创建数据的字典视图
col_mapping_dict
df.iloc[:, 0:3]
df.iloc[:, np.r_[0:3,15:19,24,25]]
