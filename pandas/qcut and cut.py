import pandas as pd
import numpy as np
import seaborn as sns
import os

os.chdir(r'.\Module\pandas')
sns.set_style('whitegrid')
raw_df = pd.read_excel('2018_Sales_Total.xlsx')
filename = '2018_Sales_Total'
df = raw_df.groupby(['account number', 'name'])['ext price'].sum().reset_index()
df['ext price']
df['ext price'].plot(kind='hist', title=f'{filename}')
