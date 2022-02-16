# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from pandas import DataFrame
# import pandas as pd
# import pymysql
# class Crawler51JobPipeline(object):
#     def __init__(self):
#         self.jobinfoAll=DataFrame()
#     def process_item(self, item, spider):
#         jobinfo=DataFrame([item['postion'],item['company'],item['place'],item['salary']]).T
#         jobinfo.columns=['职位名','公司名','地点','薪资']
#         self.jobinfoAll=pd.concat([self.jobinfoAll,jobinfo])
#         self.jobinfoAll.to_csv('jobInfo.csv',encoding='gbk')
#         return item
import pymysql
class Crawler51JobPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, database='mytest', user='root', password='123', charset='utf8')
        # 需要一个cursor对象
        self.cs1 = self.conn.cursor()
    def process_item(self, item, spider):
        # 往数据库中添加数据
        print(len(item['postion']))
        print(len(item['company']))
        print(len(item['place']))
        print(len(item['salary']))
        for i in range(len(item['postion'])):
            self.cs1.execute('insert into job(postion,company,place,salary) values("{}","{}","{}","{}")'.format(item['postion'][i],item['company'][i],item['place'][i],item['salary'][i]))
        # 提交事务
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cs1.close()
        self.conn.close()
