import requests
import webbrowser
from bs4 import BeautifulSoup

param = {'id': 1721956, 'companyid': 8, 'l': 0}
url = 'http://vip.win007.com/changeDetail/handicap.aspx'
html = requests.get(url, param).text
soup = BeautifulSoup(html, 'lxml')
ul = soup.find('ul', {'class': 'hg_nav'})
print(ul)
