from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def main():
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")       # define headles
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()
    url = 'https://v.taobao.com/v/content/live?catetype=704&from=taonvlang'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for img_tag in soup.select('img[src]'):
        print(img_tag.attrs['src'])


if __name__ == '__main__':
    main()
