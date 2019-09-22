# -*- coding: utf-8 -*-
import scrapy
from spider_rank.items import SpiderRankItem


class JianshuSpiderSpider(scrapy.Spider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    # start_urls = ['https://www.jianshu.com/recommendations/users']
    start_urls = ['https://www.jianshu.com/mobile/books?category_id=284']

    def parse(self, response):
        # print(response.text)
        # 简书排行
        # response_c  =   response.xpath("//div[@class='row']//div[@class='col-xs-8']")
        # for item in response_c:
        #     i_rankitem = SpiderRankItem()
        #     i_rankitem['img'] = item.xpath(".//div[@class='wrap']/a//img[@class='avatar']/@src/text()").extract_first()
        #     i_rankitem['name'] = item.xpath(".//div[@class='wrap']/a//h4[@class='name']/text()").extract()[0]
        #     i_rankitem['description'] = item.xpath(".//div[@class='wrap']/a//p[@class='description']/text()").extract_first()
        #     print(i_rankitem['name'])
        #     yield i_rankitem

        response_s = response.xpath("//div[@class='clearfix']//div[@class='book-wrap']")
        for item in response_s:
            i_rankitem = SpiderRankItem()
            i_rankitem['title'] = item.xpath(".//div[@class='book']//div[@class='info']//p[@class='title']/text()").extract_first()
            i_rankitem['readit'] = item.xpath(
                ".//div[@class='book']//div[@class='info']//div[@class='user-panel']/span/text()").extract_first()
            i_rankitem['nick_name'] = item.xpath(
                ".//div[@class='book']//div[@class='info']//div[@class='user-panel']//span[@class='nickname oneline']/text()").extract_first()
            print(i_rankitem['nick_name'])
            yield i_rankitem


