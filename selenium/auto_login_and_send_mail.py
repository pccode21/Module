from selenium import webdriver
import time


def login():
    driver = webdriver.Chrome()
    driver.get('https://mail.qq.com/')  # 打开登陆qq邮箱的网页
    driver.maximize_window()  # 将浏览器窗口最大化
    time.sleep(3)  # 休息五分钟等待网页加载完毕
    driver.switch_to.frame('login_frame')  # 找到邮箱账号登录框对应的iframe
    email = driver.find_element_by_name('u')  # 找到邮箱账号输入框
    email.send_keys('邮箱地址')  # 将自己的邮箱地址输入到邮箱账号框中
    password = driver.find_element_by_name('p')  # 找到密码输入框
    password.send_keys('邮箱密码')  # 输入自己的邮箱密码
    login_btn = driver.find_element_by_id('login_button')  # 找到登陆按钮
    login_btn.click()  # 点击登陆按钮
    print("登录成功")
    time.sleep(5)  # 等待10秒看是否登陆成功
    driver.switch_to.default_content()  # 离开login_frame
    time.sleep(1)
    w_mail_btn = driver.find_element_by_id('composebtn')  # 定位写信按钮
    w_mail_btn.click()
    driver.switch_to.frame('mainFrame')  # 切换到mainFrame
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('收件人邮箱')  # 定位收件人，并输入
    driver.find_element_by_id('subject').send_keys('来着16007005@qq.com的自动发送邮件')  # 定位主题，并输入
    driver.switch_to.frame(driver.find_element_by_class_name('qmEditorIfrmEditArea'))  # 定位邮件正文，先进入到iframe
    driver.find_element_by_xpath('/html/body').click()  # 必须先点击正文，再send_keys
    driver.find_element_by_xpath('/html/body').send_keys('您好！来着16007005的问候！','\n数能工作室')
    driver.switch_to.parent_frame()  # 返回到mainframe
    driver.find_element_by_name('sendbtn').click()  # 定位发送按钮
    time.sleep(5)


if __name__ == '__main__':
    login()
