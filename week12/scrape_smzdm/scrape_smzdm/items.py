# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BrandItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_id = scrapy.Field()
    article_title = scrapy.Field()
    mall = scrapy.Field()
    category = scrapy.Field()
    brand = scrapy.Field()


class CommentItem(scrapy.Item):
    comment_id = scrapy.Field()
    article_id = scrapy.Field()
    username = scrapy.Field()
    datetime = scrapy.Field()
    content = scrapy.Field()
