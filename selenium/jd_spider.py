from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery
import time
"""
# Chrome 开启无窗口模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
"""
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐式等待10秒
driver.set_window_size(1280, 800)  # 控制打开操作界面大小


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', str(page), '页数据')
    try:
        url = 'https://search.jd.com/Search?keyword=iPhone&ev=exbrand_Apple'
        driver.get(url)
        if page > 1:
            input = driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/input')
            button = driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/a')
            input.clear()
            input.send_keys(page)
            button.click()
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    """
    使用 JavaScript 来模拟滚动条滚动，先将所有的图片加载出来，然后再进行数据的获取
    中间那段 js 就是模拟滚动条向下滚动的代码，这里小编做了一个定时任务，这个定时任务将整个页面的长度分成了 100 份，
    每 20 ms 就向下滚动 1% ，共计应该总共 2s 可以滚到最下面，这里下面做了 3s 的睡眠，保证这个页面的图片都能加载出来，
    最后再获取页面上的数据。
    """
    js = '''
    timer = setInterval(function(){
       var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;
       var ispeed=Math.floor(document.body.scrollHeight / 100);
       if(scrollTop > document.body.scrollHeight * 90 / 100){
           clearInterval(timer);
       }
       console.log('scrollTop:'+scrollTop)
       console.log('scrollHeight:'+document.body.scrollHeight)
       window.scrollTo(0, scrollTop+ispeed)
    }, 20)
    '''
    driver.execute_script(js)
    time.sleep(3)
    html = driver.page_source
    doc = PyQuery(html)
    items = doc('#J_goodsList .gl-item .gl-i-wrap').items()
    i = 0
    for item in items:
        insert_data = {
                        'image': item.find('.p-img a img').attr('src'),
                        'price': item.find('.p-price i').text(),
                        'name': item.find('.p-name em').text(),
                        'commit': item.find('.p-commit a').text(),
                        'shop': item.find('.p-shop a').text(),
                        'icons': item.find('.p-icons .goods-icons').text()
        }
        i += 1
        print('当前第', str(i), '条数据，内容为：', insert_data)


def main():
    for i in range(1, 4):
        index_page(i)


if __name__ == '__main__':
    main()
