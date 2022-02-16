# -*- coding: utf-8 -*-
import scrapy


class Test51jobSpider(scrapy.Spider):
    name = 'test51job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,Java%2B%25E5%25BC%2580%25E5%258F%2591,2,1.html']

    def parse(self, response):
        postion = response.xpath('//p[@class="t1 "]/span/a/@title').extract()
        company= response.xpath('//span[@class="t2"]/a/@title').extract()
        print(postion)
        print(company)
