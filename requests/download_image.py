from bs4 import BeautifulSoup
import requests
import os

os.chdir(r'.\Module\requests\images')

url = 'http://www.ngchina.com.cn/animals/'
html = requests.get(url).text
# print(html)
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul', {'class': 'img_list'})
print(img_ul)
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name=url.split('/')[-1]
        with open('%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
