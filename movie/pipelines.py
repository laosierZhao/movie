# -*- coding: utf-8 -*-
from idlelib.iomenu import encoding

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def process_item(self, item, spider):
        #return item
        with open("my_meiju.txt",'a',encoding='utf-8') as fp:
            fp.write(item['name'] + " " + item['subType']  +'\n')
            print('Item:' + item['name'] + '\n')
