# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class movie:
    name = ''
    imdbRating = -1
    boxOffice = -1
    meta = -1
    rogerRating = -1
    googleRating = -1
    genreTags = []
    starCast = []
    releaseYr = -1

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)










### new code
import scrapy
class imdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/search/title?title_type=feature&user_rating=1.0,10.0&sort=alpha,asc']

    def parse(self, response):
        print ("its runnning")

        SET_SELECTOR = '.lister-item-header'

        for object in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a ::text'
            yield{
                'name': object.css(NAME_SELECTOR).extract_first(),
            }


### BIG PENISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS







class boxOfficeSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.boxofficemojo.com/movies/alphabetical.htm?letter=A&p=.htm']

    def parse(self, response):
    	counter = 0
        print ("its runnning")

        SET_SELECTOR = 'tr'

        for object in response.css(SET_SELECTOR):
        	counter = counter + 1
        	if (counter > 5):
	            NAME_SELECTOR = 'a ::text'
	            yield{
	                'name': object.css(NAME_SELECTOR).extract_first(),
	            }

















from html.parser import HTMLParser
from html.entities import name2codepoint
import requests

r = requests.get('https://www.metacritic.com/browse/movies/title/dvd')

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)




#######################
import scrapy
class metaSpider(scrapy.Spider):
    name = 'meta'
    start_urls = ['https://www.metacritic.com/browse/movies/title/dvd']
    flag = False
    def parse(self, response):
        print ("its runnning")

        SET_SELECTOR = '.title'

        for object in response.css(SET_SELECTOR):

            if flag :
                NAME_SELECTOR = 'a ::text'
                yield{
                    'name': object.css(NAME_SELECTOR).extract_first(),
                    }
            else :
                flag = True

######################



class rogerSpider(CrawlSpider):
    name = 'Roger Ebert'
    allowed_domains = ['www.rogerebert.com']
    start_urls = [
          'https://www.rogerebert.com/movies/A'
          'https://www.rogerebert.com/movies/B'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.next_page')),
                callback="parse_item",
                follow=True),
    )

    def parse(self, response):
        #print('Processing..' + response.url)
        item_links = response.css('.large' > /detailsLink::attr(href)').extract')
