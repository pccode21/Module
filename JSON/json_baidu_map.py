import requests
import json
import os
import codecs  # 自然语言编码转换模块

os.chdir(r'.\Module\JSON\data')  # 创建工作路径


def baidu_map_search(key):
    AK = '6Sd2LVgli3wvf7fQWW9N6A15VvpVuO39'
    url = 'http://api.map.baidu.com/place/v2/search'
    params = {
        "query": key,
        "region": 259,  # 259是揭阳市的area_id
        "city_limit": "true",
        "output": "json",
        "ak": AK,
        "page_size": 20,
        "page_num": 0,  # 从第一页 0 开始
        "scope": 2}
    response = requests.get(url, params)
    result = response.json()
    status = result.get("status")
    message = result.get("message")
    if status != 0 and status != 2:
        raise Exception(message)
    data = result.get("results", {})
    print(data)
    new_data = []
    for i in data:
        loc = i.get("location", {})
        lat = str(loc["lat"])
        lng = str(loc["lng"])
        item = {
            "name": i.get("name", ""),
            "address": i.get("address", ""),
            "province": i.get("province", ""),
            "city": i.get("city", ""),
            "area": i.get("area", ""),
            "telephone": i.get("telephone", ""),
            "lat,lng": (eval(lat), eval(lng)),  # Python的内置函数eval()可以去掉字符串两端的引号
            "tag": i.get("detail_info", "").get("tag", "")}
        new_data.append(item)
        # 用codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode
        with codecs.open('search_result.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(new_data, ensure_ascii=False))  # 由于new_data里面包含有汉字，需要使用ensure_ascii=False
        for k, v in item.items():
            print("{}:{}".format(k, v))


if __name__ == '__main__':
    baidu_map_search("学校")
