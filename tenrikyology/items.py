# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TenrikyologyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    entry_date = scrapy.Field()
    cat = scrapy.Field()
    tag = scrapy.Field()
    content = scrapy.Field()

