import requests
import webbrowser
import os

os.chdir(r'.\Module\myqr')

data = {'firstname': '心', 'lastname': '境'}
url1 = 'http://pythonscraping.com/pages/files/processing.php'
r = requests.post(url=url1, data=data)
print(r.text)

file = {'uploadFile': open('football.gif', 'rb')}
# rb主要是为了读取二进制文件而创立的字段
# 如果我们读取人工书写的数据那么就使用r,如果我们读取非人工书写的数据那么我们就是使用rb，图片就是一种非常典型的非人工书写数据
url2 = 'http://pythonscraping.com/pages/files/processing2.php'
r = requests.post(url=url2, files=file)
print(r.text)

session = requests.Session()
playload = {'username': 'morvan', 'password':'password'}
url3 = 'http://pythonscraping.com/pages/cookies/welcome.php'
r = session.post(url=url3, data=playload)
print(r.cookies.get_dict())

url4 = 'http://pythonscraping.com/pages/cookies/profile.php'
r = session.get(url=url4)
print(r.text)

os.chdir(r'.\Module\requests')

os.makedirs('./images/', exist_ok='True')
# exist_ok：是否在目录存在时触发异常。如果exist_ok为False（默认值），则在目标目录已存在的情况下触发FileExistsError异常；
# 如果exist_ok为True，则在目标目录已存在的情况下不会触发FileExistsError异常。
IMAGE_URL = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
r= requests.get(url=IMAGE_URL)
with open('./images/image.png', 'wb') as f:   # 'wb'以二进制格式打开一个文件只用于写入
    # f.write(r.content)
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
# 使用 r.iter_content(chunk_size) 来控制每个 chunk 的大小, 然后在文件中写入这个 chunk 大小的数据.
