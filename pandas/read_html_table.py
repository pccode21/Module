import pandas as pd
import os

os.chdir(r'.\Module\pandas')
data = pd.DataFrame()
# 带有table标签的URL
url_list = ['http://www.espn.com/nba/salaries/_/page/2']
for url in url_list:
    data = data.append(pd.read_html(url), ignore_index=True)
# startswith方法用于检查字符串是否是以指定子字符串开头
data = data[[x.startswith('$') for x in data[3]]]
data.to_csv('NAB_salaries.csv', header=['RK', 'NAME', 'TEAM', 'SALARY'], index=False)
