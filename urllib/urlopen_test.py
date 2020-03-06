from urllib.request import urlopen
import re

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
