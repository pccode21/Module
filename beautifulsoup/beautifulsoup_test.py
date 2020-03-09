from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import random
"""
html = urlopen('https://morvanzhou.github.io/static/scraping/basic-structure.html').read().decode('utf-8')
# 为了正常显示中文, read() 完以后, 我们要对读出来的文字进行转换, decode() 成可以正常显示中文的形式.
print(html)
res = re.findall(r'<title>(.+?)</title>', html)
print('\nPage title is:', res[0])
res1 = re.findall(r'<h1>(.+?)</h1>', html)
print('\nPage h1 is:', res1[0])
res2 = re.findall(r'<p>(.+?)</p>', html, flags=re.DOTALL)
# 由于<p>里面掺杂了换行符和空格符，要使用 flags=re.DOTALL 过滤掉这些符号
print("\nPage paragraph is: ", res2[0])
res3 = re.findall(r'href="(.+?)"', html)
print('\nAll links:', res3[0:])
"""
"""
html = urlopen('https://morvanzhou.github.io/static/scraping/list.html').read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, features='lxml')
month = soup.find_all('li', {'class': 'month'})
for m in month:
    print(m.get_text())
jans = soup.find('ul', {'class': 'jan'})
jan = jans.find_all('li')
for j in jan:
    print(j.get_text())
"""
"""
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, features='lxml')
img_link = soup.find_all('img', {'src': re.compile('.*?\.jpg')})
for link in img_link:
    print(link['src'])
course_links = soup.find_all('a', {'href': re.compile('https://morvanzhou.*')})
for link in course_links:
    print(link['href'])
"""
html = urlopen('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711')
base_url = "https://baike.baidu.com"
his = ['/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711']
for _ in range(20):
    url = base_url + his[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(soup.find('h1').get_text(), ' url:', his[-1])
    sub_urls = soup.find_all("a", {'target': '_blank', 'href': re.compile('/item/(%.{2})+$')})
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])  # 在这些过滤后的网页中随机选一个
    else:  # 找不到有效的子链接
        his.pop()
    print(his)
