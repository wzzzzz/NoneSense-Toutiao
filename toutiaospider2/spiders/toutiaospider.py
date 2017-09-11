import json
import urllib
from urllib import parse
from scrapy.loader import ItemLoader
from scrapy.spider import Spider, Request
from toutiaospider2.items.itemcomment import CommentInfo


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
        resp_json = json.loads(response.body_as_unicode())
        request_url = response.request.url
        if resp_json['message'] == 'success':
            new_max_hot_time = resp_json['next']['max_behot_time']
            follow_up_request = request_url[0:request_url.find('=') + 1] + str(new_max_hot_time) + request_url[
                                                                                                   request_url.find(
                                                                                                       '&'):]
            if 'data' in resp_json:
                if resp_json['data'] is not None:
                    for article in resp_json['data']:
                        if 'comments_count' not in article:
                            continue
                        article_request = {
                            'group_id': article['group_id'],
                            'item_id': article['group_id'],
                            'offset': 0,
                            'count': article['comments_count']
                        }
                        article_base_url = 'http://www.toutiao.com/api/comment/list/?'
                        article_url = article_base_url + urllib.parse.urlencode(article_request)
                        request = Request(article_url, callback=self.parse_comment, method='GET')
                        request.meta['associate_article_title'] = (article['title'] if 'title' in article else '')
                        request.meta['associate_article_content'] = (article['abstract'] if 'bastract' in article else '')
                        request.meta['associate_article_keywords'] = (article['label'] if 'label' in article else '')
                        request.meta['article_url'] = (article['source_url'] if 'source_url' in article else '')
                        request.meta['reply_to_id'] = ''
                        yield request
                        # yield Request(follow_up_request, callback=self.parse, method='GET')
        else:
            return

    def parse_comment(self, response):
        comments_json = json.loads(response.body_as_unicode())
        if comments_json['message'] == 'success':
            comments = comments_json['data']['comments']
            if len(comments) > 0:
                items = []
                for comment in comments:
                    item = CommentInfo(
                        {'comment': comment['text'], 'likes': comment['digg_count'], 'time': comment['create_time'],
                         'comment_id': comment['id']})
                    self.copy_article_info(response.meta, item)

                    if comment['reply_count'] > 0:
                        reply_to_comment_url = 'http://www.toutiao.com/api/comment/get_reply/?comment_id=' + str(comment['id']) + '&dongtai_id=' + str(comment['dongtai_id']) + '&offset=0&count=' + str(comment['reply_count'])
                        reply_request = Request(reply_to_comment_url, callback=self.parse_reply, method='GET')
                        self.copy_article_info(response.meta, reply_request.meta)
                        reply_request.meta['reply_to_id'] = comment['id']
                        yield reply_request

                    items.append(item)
                return items
        else:
            return


    def parse_reply(self, response):
        replies_json = json.loads(response.body_as_unicode())
        if replies_json['message'] == 'success':
            replies = replies_json['data']['data']
            if len(replies) > 0:
                items = []
                for reply in replies:
                    item = CommentInfo({
                        'comment': reply['text'], 'likes': reply['digg_count'], 'time': reply['create_time'],
                        'comment_id': reply['id']})
                    self.copy_article_info(response.meta, item)
                    items.append(item)
                return items
        else:
            return


    def copy_article_info(self, source, destination):

        destination.setdefault('reply_to_id', source['reply_to_id'])
        destination.setdefault('associate_article_title', source['associate_article_title'])
        destination.setdefault('associate_article_content', source['associate_article_content'])
        destination.setdefault('associate_article_keywords', source['associate_article_keywords'])

