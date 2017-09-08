import urllib

import scrapy
from scrapy.spider import Spider


class TouTiaoSpider(Spider):
    name = 'toutiaocomment'
    start_urls = []

    def __init__(self):
        super(Spider, self).__init__()
        self.base_url = 'http://www.toutiao.com/api/pc/feed/?'
        self.payload = {'max_behot_time': 0, 'category': '', 'utm_source': 'toutiao', 'widen': 1, 'tadrequire': 'true'}
        self.categories = (
        'news_hot', 'news_society', '%E7%BB%84%E5%9B%BE', 'news_sports', 'news_entertainment', 'news_game',
        'news_sports', 'news_car',
        'news_finance', 'funny', 'essay_joke', 'news_world', 'news_travel', 'news_baby', 'news_essay', 'news_food',
        'news_history', 'news_military', 'news_fashion', 'news_discovery', 'news_regimen', 'news_tech')

        for cate in self.categories:
            self.payload['category'] = cate
            url = urllib.parse.urlencode(self.payload)
            self.start_urls.append(self.base_url + url)

    def parse(self, response):
        print(response.url)

