# -*- coding: utf-8 -*-
import scrapy


class RatingsSpider(scrapy.Spider):
    name = 'ratings'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/']

    def parse(self, response):
        pass
