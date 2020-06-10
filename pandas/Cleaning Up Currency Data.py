
import pandas as pd
import os

os.chdir(r'.\Module\pandas')
df_orig = pd.read_excel('sales_cleanup.xlsx')
df = df_orig.copy()
df['Sales'].apply(type)
df['Sales'] = df['Sales'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df['Sales_Type'] = df['Sales'].apply(lambda x: type(x).__name__)
print(df)
