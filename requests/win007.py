import requests
import webbrowser
from bs4 import BeautifulSoup

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
param = {'id': 1721956, 'companyid': 8, 'l': 0}
url = 'http://vip.win007.com/changeDetail/handicap.aspx'
html = requests.get(url, param, headers=headers).text
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', {'id': 'out'})
table = div.find('table')
span = table.find('span', {'id': 'odds'})
tr = span.find_all('tr')
print(tr)
