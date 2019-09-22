# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo

from spider_rank.settings import monge_db_collection, mongo_name, mongo_host, mongo_port

# monge db数据存储
class SpiderRankPipeline(object):
    def __init__(self):
        # host=mongo_host
        # port=mongo_port
        # dbname= mongo_name
        # sheetname=monge_db_collection
        # client=pymongo.MongoClient(host=host,port=port)
        # mydb=client[dbname]
        # self.port=mydb[sheetname]

       client = pymongo.MongoClient('mongodb://localhost:27017/')
       db = client.test
       self.collection = db.item

    def process_item(self, item, spider):
        # data    =   dict(item)
        # self.port.insert(data)
        # data2=json.dumps(data)
        # print("chowen %s" %data2)

        data = dict(item)
        data2 = json.dumps(data)
        print("chowen %s" % data2)
        # result = self.collection.insert(data)
        # print(result)
        return item
