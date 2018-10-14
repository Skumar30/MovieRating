import scrapy
import os
### THIS FILE IS COMPLETE
counter = 0
class imdbSpider(scrapy.Spider):
    
    def stringGen():
        toReturn = []
        minUserrtg = 1.0
        maxUserrtg = 1.0
        BASE_STRING = 'https://www.imdb.com/search/title?title_type=feature&user_rating='
        REST_OF_STRING = '&count=10000&sort=alpha,asc'

        while minUserrtg <4:

            maxUserrtg = min(maxUserrtg, 10)
            minUserrtg = min(minUserrtg, 10)
            toReturn.append(BASE_STRING +(str)(minUserrtg) + ',' + (str)(maxUserrtg) + REST_OF_STRING)
            minUserrtg += 0.1
            maxUserrtg += 0.1

        return toReturn

    name = 'imdb'
    start_urls = stringGen()
    print(start_urls)                
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
                 'genre': [x.strip() for x in object.css(GENRE_SELECTOR).extract()],
                 'BoxOffice': object.xpath('//span[5]/@data-value').extract_first().strip(",")    
            }

        NEXT_PAGE_SELECTOR = 'a ::attr(href)'
        if(counter == 0):
            next_page = response.xpath("//*[@id='main']/div/div/div[4]/div/a/@href").extract_first()
        else:
            next_page = response.xpath("//*[@id='main']/div/div/div[4]/div/a[2]/@href").extract_first()
        counter = counter + 1
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

