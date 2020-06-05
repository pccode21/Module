import pandas as pd
import numpy as np
import os

os.chdir(r'.\Module\pandas')
df = pd.read_excel('2018_Sales_Total.xlsx')
df = df.groupby('name')['ext price'].agg(['mean', 'sum'])
df['mean'] = df['mean'].map('${0:,.2f}'.format)
df['sum'] = df['sum'].map('${0:,.2f}'.format)
print(df)
