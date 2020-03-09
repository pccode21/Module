import requests


class Spider(object):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

    def get_one_page(self, n, start='2014-01-01', end='2020-02-25'):
        url = 'http://www.lottery.gov.cn/football/result_{}.jspx?f_league_id=28&f_league_name=%E8%8B%B1%E8%B6%85&startDate={}&endDate={}'.format(n, start, end)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        return None

    def parse_one_page(self, html):
        pass

    def main(self):
        pass


if __name__ == '__main__':
    spider = Spider()
    d = spider.get_one_page(247)
    print(d)
