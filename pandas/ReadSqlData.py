import pandas as pd
import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='Lxd05230708',
                       database='spider',
                       charset='utf8mb4')
sql = 'select * from football_player'
df = pd.read_sql(sql, conn)
print(df)
# print(df.head(5))  # 获取前5行
