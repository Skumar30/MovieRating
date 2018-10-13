# -*- coding: utf-8 -*-
import scrapy


class MetacriticSpider(scrapy.Spider):
    name = 'metacritic'
    allowed_domains = ['metacritic.com']
    start_urls = ['http://metacritic.com/']

    def parse(self, response):
        pass
