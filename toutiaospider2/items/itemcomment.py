import scrapy
from scrapy import Item


class CommentInfo(Item):
    comment = scrapy.Field()
    likes = scrapy.Field()
    time = scrapy.Field()
    reply_count = scrapy.Field()
    comment_id = scrapy.Field()
    reply_to_id = scrapy.Field()
    associate_article_title = scrapy.Field()
    associate_article_content = scrapy.Field()
    associate_article_keywords = scrapy.Field()
