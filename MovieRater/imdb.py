import scrapy
import os
### THIS FILE IS COMPLETE
counter = 0
numPages = 200
class imdbSpider(scrapy.Spider):
    
    def stringGen():
        toReturn = []
        minUserrtg = 1.0
        maxUserrtg = 1.1
        BASE_STRING = 'https://www.imdb.com/search/title?title_type=feature&user_rating='
        REST_OF_STRING = '&count=250&sort=alpha,asc'

        while minUserrtg <10.1:

            maxUserrtg = min(maxUserrtg, 10)
            toReturn.append(BASE_STRING +(str)(minUserrtg) + ',' + (str)(maxUserrtg) + REST_OF_STRING)
            minUserrtg += 0.2
            maxUserrtg += 0.2

        return toReturn

    name = 'imdb'
    start_urls = stringGen()
                
    handle_httpstatus_list = [404]

    def parse(self, response):

        SET_SELECTOR = '.lister-item-content'
        global counter
        for object in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a ::text'
            YEAR_SELECTOR = '.lister-item-year ::text'
            GENRE_SELECTOR = '.genre ::text'
            yield{

                 'name': object.css(NAME_SELECTOR).extract_first().encode('utf-8'),


                 'imdbRating': object.xpath(".//strong/text()").extract_first().encode('utf-8'),
                 'year': object.css(YEAR_SELECTOR).extract_first().strip("()").encode('utf-8'),
                 'genre': [x.strip() for x in object.css(GENRE_SELECTOR).extract()]
            }

        NEXT_PAGE_SELECTOR = 'a ::attr(href)'
        if(counter == 0):
            print("if")
            next_page = response.xpath("//*[@id='main']/div/div/div[4]/div/a/@href").extract_first()
        else:
            print("entered else")
            next_page = response.xpath("//*[@id='main']/div/div/div[4]/div/a[2]/@href").extract_first()
        counter = counter + 1
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

