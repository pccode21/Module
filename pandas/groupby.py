import pandas as pd
import os

os.chdir(r'.\Module\pandas')
df = pd.read_excel('数据透视表.xlsx', sheet_name='原数据')
df['订购月份'] = df['订购日期'].apply(lambda x:x.month)
# df2 = df.groupby(['订购月份', '所属区域'])[['销售额', '成本']].agg('sum')
df2 = df.groupby(['订购月份', '所属区域'])[['数量', '销售额', '成本']].sum()
df2['利润'] = df2['销售额'] - df2['成本']
print(df2)
df2.to_excel('数据透视表结果.xlsx', sheet_name='计算结果')
