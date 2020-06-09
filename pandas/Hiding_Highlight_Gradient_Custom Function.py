# 1. 数据来源
import pandas as pd
import seaborn as sns
planets = sns.load_dataset('planets')
planets.head(10)
planets.head(10).style.hide_index()  # 隐藏索引
planets.head(10).style.hide_columns(['method', 'year'])  # 隐藏不需要的列
planets.head(10).style.highlight_max(color='yellow')  # 高亮最大值
planets.head(10).style.highlight_min(color='yellow')  # 高亮最小值
planets.head(10).style.highlight_min(color='yellow', axis=1)  # 高亮每一行的最小值
planets.head(10).style.highlight_min(color='yellow', axis=0)  # 高亮每一列的最小值
planets.head(10).style.highlight_null(null_color='red')  # 高亮空值
# Gradient Function 在显示数据时，用一种背景颜色来显示数据，以突出显示哪个数字在较低的区域，哪个数字在较高的区域。
planets.head(10).style.background_gradient(cmap='Blues')
planets.head(10).sort_values(by='year').style.bar(color='lightgreen')  # 使用条形图作为渐变背景色
# 设定一个函数，并以某种方式将我们的函数应用于DataFrame。列入我我们设定一个阈值，将小于20的任何数都应该被涂成红色。
def color_below_20_red(value):
    if type(value) == type(''):
        return 'color:black'
    else:
        color = 'red' if value <= 20 else 'black'
        return 'color:{}'.format(color)
planets.head(10).style.applymap(color_below_20_red)
