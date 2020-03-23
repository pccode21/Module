from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  # 实例化一个启动参数对象
chrome_options.add_argument('--window-size=1366, 768')  # 设置浏览器窗口大小
driver = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://www.geekdigging.com/'
driver.get(url)
title = driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/a')
print(title)
print(title.get_attribute('href'))  # 获取属性信息
print(title.text)  # 获取文本信息
print(title.location)  # 获取位置
print(title.size)  # 获取大小
img = driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/a/img')
print(img.get_attribute('src'))
