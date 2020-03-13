import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import matplotlib.pyplot as plt

os.chdir(r'.\Module\beautifulsoup')

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
param = {'id': 1721956, 'companyid': 8, 'l': 0}
url = 'http://vip.win007.com/changeDetail/handicap.aspx'
html = requests.get(url, param, headers=headers).text
soup = BeautifulSoup(html, 'lxml')
tr_list = soup.find('div', {'id': 'out'}).find('table').find('span', {'id': 'odds'}).find_all('tr', title=True)
print(tr_list)
soup.font.decompose()  # Tag.decompose() 方法将当前节点移除文档树并完全销毁，在这里是移除<font color="blue">(初盘)</font>
print(tr_list)
date_time = []  # 全部时间
let_ball = []  # 全部让球盘
water_level = []  # 全部水位
change_let_ball = []  # 变化让球盘
change_time = []  # 变化时间点
change_water_level = []  # 变化水位点
for tr in tr_list:
    tm = tr.find('td', {'class': re.compile('^tm')})  # 'class'内容包括 tm 和 tm1
    tm1 = tr.find('td', {'class': 'tm1'})
    pk = tr.find('td', {'class', 'pk'})
    level = tr.find('td', class_=False)

    """按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.
    从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag"""
    water_level.append(level.text.replace('\xa0', ''))  # \xa0 是不间断空白符 &nbsp;要使用replace替换掉
    if tm is not None:
        date_time.append(tm.text)
    if pk is not None:
        let_ball.append(pk.text)
    if tm1 is not None:
        change_pk = tm1.next_sibling  # 在文档树中,使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点:
        change_level = change_pk.next_sibling
        change_let_ball.append(change_pk.text)
        change_water_level.append(change_level.text.replace('\xa0', ''))
        change_time.append(tm1.text)
water_level = list(map(float, water_level))  # 将列表中的字符串转为数字
change_water_level = list(map(float, change_water_level))
water_level = water_level[::-1]  # 反转列表使用[::-1]
# water_level = ['0.95' if w=='0.95(初盘)' else w for w in water_level]  # 将'0.95(初盘)'替换成'0.95'
date_time = date_time[::-1]
let_ball = let_ball[::-1]
change_time = change_time[::-1]
change_let_ball = change_let_ball[::-1]
change_water_level = change_water_level[::-1]
ball_c = ['三球', '两球半/三球', '两球半', '两球/两球半', '两球', '球半/两球', '球半', '一球/球半', '一球', '半球/一球', '半球', '平半/半球', '平手',
            '受让平手/半球', '受让半球', '受让半球/一球','受让一球']
ball_n = [3, 2.75, 2.5, 2.25, 2, 1.75, 1.5, 1.25, 1, 0.75, 0.5, 0.25, 0, -0.25, -0.5, -0.75, -1]
let_ball_n = []
for i in range(0, len(let_ball)):  # 将 let_ball 中的中文字符串（'半球/一球'等）转换为数字（0.75等）
    for j in range(0, len(ball_c)):
        if let_ball[i] == ball_c[j]:
            let_ball_n.append(ball_n[j])
change_let_ball_n = []
for i in range(0, len(change_let_ball)):  # 将 change_let_ball 中的中文字符串（'半球/一球'等）转换为数字（0.75等）
    for j in range(0, len(ball_c)):
        if change_let_ball[i] == ball_c[j]:
            change_let_ball_n.append(ball_n[j])
change_water_level_s = list(set(change_water_level))  # 列出原有列表中的不同值
change_water_level_s = sorted(change_water_level_s, key=float)
# 对列表中的数字进行排序，key参数需要一个函数，该函数将在使用转换值进行排序之前转换值，但保留原始值
let_ball_n = list(map(float, let_ball_n))
change_let_ball_n = list(map(float, change_let_ball_n))
print(water_level)
print(date_time)
print(let_ball)
print(let_ball_n)
print(change_time)
print(change_let_ball)
print(change_water_level)
print(change_let_ball_n)
print(change_water_level_s)
data_dict = {
            'date_time': date_time,
            'let_ball': let_ball,
            'let_ball_n': let_ball_n,
            'water_level': water_level
            }
change_data_dict = {
                    'change_time': change_time,
                    'change_let_ball': change_let_ball,
                    'change_let_ball_n': change_let_ball_n,
                    'change_water_level': change_water_level
                    }
datas = pd.DataFrame(data_dict)
change_datas = pd.DataFrame(change_data_dict)
print(change_datas)
datas.to_csv('2019-2020切尔西vs埃弗顿29.csv')
change_datas.to_csv('2019-2020切尔西vs埃弗顿29（盘口变化）.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(num=1, figsize=(12, 8))
plt.plot(change_time, change_water_level, marker='o', markersize=3, color='gray', alpha=0.5, markeredgecolor='black', markerfacecolor='red')
plt.yticks(ticks=change_water_level_s, fontproperties='Times New Roman', size=9)  # 设置y轴显示的内容
for t, w, b in zip(change_time, change_water_level, change_let_ball_n):
        plt.annotate('%s' % b, xy=(t, w), xytext=(-4, -8), textcoords = 'offset points', fontsize=6, color='r')
ax = plt.gca()  # 使用plt.gca获取当前坐标轴信息
ax.spines['right'].set_color('none')  # 使用.spines设置边框
ax.spines['top'].set_color('none')
# ax.yaxis.set_major_locator(plt.LinearLocator(len(change_water_level_s)))  # 设置y轴显示多少个数字刻度
ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%1.2f'))  # 设置y轴标签文本的格式
ax.xaxis.set_major_locator(plt.LinearLocator(20))  # 设置x轴显示多少个日期刻度
# ax.xaxis.set_major_locator(plt.MultipleLocator(140))  # 设定坐标轴的显示的刻度间隔
plt.gcf().autofmt_xdate(rotation=45)  # 防止x轴上的数据重叠，自动调整,并且45度倾斜
# 当前的图表和子图可以使用plt.gcf()和plt.gca()获得，分别表示Get Current Figure和Get Current Axes。
plt.xticks(fontproperties='Times New Roman', size=9)  # 设置X轴刻度字体和大小
plt.xlabel('日期-时间', fontsize=10)
plt.ylabel('让球水位', fontsize=10)
plt.grid(linestyle='dotted')
# linestyle values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
# plt.axhline(y=max(water_level), color='green', linestyle='dotted', lw=1)  # 添加水平参考线
# plt.text(max(date_time), max(water_level), r'▼半一 ▲半球', fontdict={'size': 9, 'color': 'red'})
plt.title("2019-2020赛季 切尔西vs埃弗顿 29轮 赛前盘口走势图", fontsize=14, loc='center')  # 设置标题
plt.savefig('2019-2020切尔西vs埃弗顿29.png')
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap('LOGO.ico')
thismanager.canvas.set_window_title('数能工作室制作')
plt.show()
