"""爬取「后浪」弹幕"""
import requests
import re
import wordcloud
import os
os.chdir(r'.\Module\requests\images')
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
res = requests.get("https://api.bilibili.com/x/player/pagelist?bvid=BV1FV411d7u7&jsonp=jsonp", headers=headers, verify=False)
cid = res.json()['data'][0]['cid']
print(cid)
danmu_url = f"https://api.bilibili.com/x/v1/dm/list.so?oid={cid}"
result = requests.get(danmu_url, headers=headers, verify=False).content.decode('utf-8')  # 如果不设置'verify=False',会引起 SSLError
pattern = re.compile('<d.*?>(.*?)</d>')
danmu_list = pattern.findall(result)
wordcloud = wordcloud.WordCloud(font_path='msyh.ttc', width=900, height=1600).generate("".join(danmu_list))
wordcloud.to_file('wordcloud.png')
