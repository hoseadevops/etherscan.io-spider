# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
# from scrapy.pipeline.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class MyfilesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        """
        重命名模块
        """
        path = os.path.join('D:\\result', ''.join( [request.url.replace('//', '_').replace('/', '_').replace(':', '_').replace('.', '_').replace('__','_'), '.zip']))
        return path
