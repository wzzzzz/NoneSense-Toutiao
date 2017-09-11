# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from toutiaospider2.items.itemcomment import CommentInfo


class Toutiaospider2Pipeline(object):
    def process_item(self, item, spider):
        return item


class CommentJsonPipeline(object):

    def open_spider(self, spider):
        self.file = open('comment.result', 'ab')

    def process_item(self, item, spider):
        if isinstance(item, CommentInfo):
            item_json = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(item_json.encode())

    def close_spider(self,spider):
        self.file.close()