# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SmartContractItem(scrapy.Item):
    
    # 合约token
    token = scrapy.Field()
    # 合约name
    name  = scrapy.Field()
    # 合约代码
    code  = scrapy.Field()
