import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

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
date_time = []
ball = []
water_level = []
for tr in tr_list:
    tm = tr.find('td', {'class': re.compile('^tm')})  # 'class'内容包括 tm 和 tm1
    pk = tr.find('td', {'class', 'pk'})
    level = tr.find('td', class_=False)
    """按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.
    从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag"""
    water_level.append(level.text.replace('\xa0', ''))  # \xa0 是不间断空白符 &nbsp;要使用replace替换掉
    if tm != None:
        date_time.append(tm.text)
    if pk != None:
        ball.append(pk.text)
water_level = water_level[::-1]  # 反转列表使用[::-1]
water_level = ['0.95' if w=='0.95(初盘)' else w for w in water_level]  # 将'0.95(初盘)'替换成'0.95'
date_time = date_time[::-1]
ball = ball[::-1]
print(water_level)
print(date_time)
print(ball)
data_dict = {
            'date_time': date_time,
            'ball': ball,
            'water_level': water_level
            }
datas = pd.DataFrame(data_dict)
print(datas)
datas.to_csv('2019-2020切尔西vs埃弗顿29.csv')
