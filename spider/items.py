# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SmartContractItem(scrapy.Item):

    # 合约 token
    token = scrapy.Field()

    # token 标识
    name  = scrapy.Field()

    # 合约 名
    contract = scrapy.Field()

    # 合约 代码
    code  = scrapy.Field()
