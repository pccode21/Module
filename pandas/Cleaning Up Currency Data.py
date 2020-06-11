import pandas as pd
import os

os.chdir(r'.\Module\pandas')
df_orig = pd.read_excel('sales_cleanup.xlsx')
# df_orig = pd.read_excel('sales_cleanup.xlsx',dtype={'Sales':str})  # 首先我们读入数据并将dtype参数用于read_excel以强制将原始数据列存储为字符串
df = df_orig.copy()
df['Sales'].apply(type)
# df['Sales'] = df['Sales'].str.replace('$', '').str.replace(',', '').astype(float)  # 然后将列转换为字符串并安全地使用str.replace
"""
# 以下函数将检查提供的值是否为字符串，如果为字符串，则将删除我们不需要的所有字符。如果不是字符串，则将返回原始值
def clean_currency(x):
    if isinstance(x, str):
        return x.replace('$', '').replace(',', '')
    return x
df['Sales'] = df['Sales'].apply(clean_currency).astype(float)
"""
# df['Sales'] = df['Sales'].replace({'\$': '', ',': ''}, regex=True).astype(float)  # 使用正则表达式从字符串中删除非数字字符
df['Sales'] = df['Sales'].apply(lambda x:x.replace('$', '').replace(',', '') if isinstance(x, str) else x).astype(float)  # lambda函数是清理和转换值的更紧凑的方式
df['Sales_Type'] = df['Sales'].apply(lambda x: type(x).__name__)
print(df)
