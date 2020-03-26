import pandas as pd

df = pd.DataFrame({'a':[None,1,2,3],'b':[4,None,None,6],'c':[1,2,1,2],'d':[7,7,9,2]})
print (df)
print (df.isnull().sum())
data_without_NaN =df.dropna(axis=0)  # axis=1 按列删除，axis=0 按行删除
print (data_without_NaN)
