import scrapy
import os
### THIS FILE IS COMPLETE
counter = 0
urls = ""
class imdbSpider(scrapy.Spider):

    def stringGen():
        toReturn = []
        minUserrtg = 1.0
        maxUserrtg = 1.0
        BASE_STRING = 'https://www.imdb.com/search/title?title_type=feature&user_rating='
        REST_OF_STRING = '&count=10000&sort=alpha,asc'

        while minUserrtg <=10:

            maxUserrtg = min(maxUserrtg, 10)
            minUserrtg = min(minUserrtg, 10)
            toReturn.append(BASE_STRING +(str)(minUserrtg) + ',' + (str)(maxUserrtg) + REST_OF_STRING)
            minUserrtg += 0.1
            maxUserrtg += 0.1

        return toReturn
    global counter
    name = 'imdb'
    global urls 
    urls = stringGen()
    start_urls = {'https://www.imdb.com/search/title?title_type=feature&user_rating=1.0&count=10000&sort=alpha,asc'}
    handle_httpstatus_list = [404]

    def parse(self, response):

        SET_SELECTOR = '.lister-item-content'
        global counter
        for object in response.css(SET_SELECTOR):

            yield {

            'imdbRating': object.xpath("..//strong/text()").extract_first().encode('utf-8'),

            'titles': response.css("#main > div > div > div:nth-child(1) > div.desc ::text").extract_first()
            }

            break
        global counter
        counter+=1
        global urls
        next_page = urls[counter]

        if(counter < 100):
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
