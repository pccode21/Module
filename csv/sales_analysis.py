import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决负号无法正常显示的问题
plt.rcParams['axes.unicode_minus'] = False

os.chdir(r'.\Module\csv')

data = pd.read_csv('order-14.3.csv', encoding='gb2312', parse_dates=['成交时间'])
'''
哪些类别的商品比较畅销
要看哪些类别的商品比较畅销,只要将订单表中的数据按照类别ID进行分组,
然后对分组后的销量求和,就会得到每一类在一段时间内的销量
'''
# 得到所有类别在一段时间内对应的销量
c_s = data.groupby('类别ID')['销量'].sum().reset_index()
# 使用数据分组获取销量前10的商品类别
best_10 = data.groupby('类别ID')['销量'].sum().reset_index().sort_values(by='销量', ascending=False).head(10)
'''
哪些商品比较畅销
'''
# 使用数据透视表获取销量前10的商品
b_10 = pd.pivot_table(data, index='商品ID', values='销量', aggfunc='sum').reset_index().sort_values(by='销量', ascending=False).head(10)
'''
不同门店的销售额占比
商品的畅销程度直接用销量来表示,销售=销量*单价,订单表中没有销售额字段,需要新增一个销售额字段,按照门店编号进行分组
对分组后的营业额求和运算,最后计算不同门店的销售额占比
'''
data['销售额'] = data['销量'] * data['单价']
# 计算门店的总销售额
store_turnover = data.groupby('门店编号')['销售额'].sum()
# 门店销售额占比,绘图
proportion_of_stores = (data.groupby('门店编号')['销售额'].sum() / data['销售额'].sum()).plot.pie()
plt.show()
'''
哪些时间段是超市的客流高峰期
要找出高峰期,就要知道每个时间段对应的客流量
但是订单表中的成交时间既有日期又有时间,我们要从中提取处小时数
这里依然使用订单ID去重计数代表客流量
'''
# 利用自定义时间格式函数strftime提取小时数
data['小时'] = data['成交时间'].map(lambda x: int(x.strftime('%H')))
# 对小时和订单去重
traffic = data[['小时', '订单ID']].drop_duplicates()
# 求每小时客流量
volume_of_commuters = traffic.groupby('小时')['订单ID'].count().plot()
plt.show()
