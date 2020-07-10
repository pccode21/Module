html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')
"""
使用css选择器的语法，应该使用select方法。
"""
#通过标签名查找：
print(soup.select('a'))

#通过类名查找：
#通过类名，则应该在类的前面加一个.。
#比如要查找class=sister的标签。示例代码如下：
print(soup.select('.sister'))

#通过id查找：
#通过id查找，应该在id的名字前面加一个＃号。示例代码如下：
print(soup.select("#link1"))

#组合查找：
#组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，
#例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开：
print(soup.select("p #link1"))

#直接子标签查找，则使用 > 分隔：
print(soup.select("head > title"))

#通过属性查找：

#查找时还可以加入属性元素，属性需要用中括号括起来，
#注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
print(soup.select('a[href="http://example.com/elsie"]'))

#获取内容
#以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容。
print(type(soup.select('title')))
print(soup.select('title')[0].get_text())
for title in soup.select('title'):
    print(title.get_text())
