from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.geekdigging.com/')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.geekdigging.com', 'value': 'geekdigging'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
