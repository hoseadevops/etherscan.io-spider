# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item
# -*- coding: utf-8 -*-


class MypjtPipeline(object):
    def __init__(self):
        self.file = codecs.open("D:/Kangbb/data1.txt", "w", encoding="utf-8")
    def process_item(self, item, spider):
        l = str(item['title'])+'\n'
        self.file.write(l)
        return item
    def close_spider(self):
        self.file.close()