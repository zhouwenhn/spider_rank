# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderRankItem(scrapy.Item):
    # define the fields for your item here like:
    # img = scrapy.Field()
    # name = scrapy.Field()
    # description = scrapy.Field()
    title = scrapy.Field()
    readit = scrapy.Field()
    nick_name   =   scrapy.Field()
