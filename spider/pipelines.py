# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import os


class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class SolPipeLine(object):

    def process_item(self, item, spider):
        folder = os.getcwd() + '/../etherscan-audit/contracts-temp/'
        if not os.path.exists(folder):
            os.makedirs(folder)
            print('目录地址：' + folder);

        self.file = codecs.open(folder + '/' + item['name'] + '.sol', "w", encoding="utf-8")
        content = item['code']
        if content:
            content += '\n\n contract ETHToken is ' + item['contract'] +' {}';
            self.file.write(content)
            return item

    def close_spider(self):
        self.file.close()
