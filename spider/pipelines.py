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
    project_dir = os.path.abspath(os.path.dirname(__file__))
    IMAGES_STORE = os.path.join(project_dir, 'images')

    def process_item(self, item, spider):
        folder = os.getcwd()[:-4] + 'code\\'
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.file = codecs.open(folder + item['name'] + '.sol', "w", encoding="utf-8")
        content = item['code']
        self.file.write(content)
        print("run here hosea")
        return item

    def close_spider(self):
        self.file.close()

    def mkdir(path):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
            print ("---  new folder...  ---")
