from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.implicitly_wait(10)  # 隐式等待10秒
browser.get('https://www.jd.com/')
"""
input_key = browser.find_element_by_id('key')
print(input_key)
lis = browser.find_elements_by_css_selector('.JS_navCtn li')  #使用('.cate_menu li')等同效果
print(lis)
try:
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'key')))  # 显式等待 WebDriverWait
finally:
    browser.quit()
input_key.send_keys('IPad')
time.sleep(1)
input_key.clear()
input_key.send_keys('Surface Pro')
button = browser.find_element_by_class_name('button').click()

browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# 执行 JavaScript，用到的方法是 execute_script() ，比如我们在淘宝首页将滚动条滑到底部
"""
