from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
input = browser.find_element_by_id('kw')
input.send_keys('数能工作室')
input.send_keys(Keys.ENTER)
print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
