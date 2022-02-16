# -*- coding: utf-8 -*-
import scrapy
from crawler51job.items  import Crawler51JobItem
from scrapy.http import Request
import re
class Spider51jobSpider(scrapy.Spider):
    name = 'spider51job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,Java%2B%25E5%25BC%2580%25E5%258F%2591,2,1.html']

    def parse(self, response):
        item=Crawler51JobItem()
        data=response.body.decode('gbk')
        item['postion']=response.xpath('//p[@class="t1 "]/span/a/@title').extract()
        item['company']=response.xpath('//span[@class="t2"]/a/@title').extract()
        place_pat = '<div class="el">.*?<span class="t3">(.*?)</span>.*?</div>'
        sa_pat = '<div class="el">.*?<span class="t4">(.*?)</span>.*?</div>'

        item['place'] = re.findall(place_pat,data,re.S)

        item['salary'] = re.findall(sa_pat,data,re.S)
        yield item
        for i in range(2,5):
            url="https://search.51job.com/list/000000,000000,0000,00,9,99,Java%2B%25E5%25BC%2580%25E5%258F%2591,2,"+str(i)+".html"
            yield Request(url,callback=self.parse)
