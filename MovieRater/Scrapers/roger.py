import scrapy

### Year, rating, next pages to be done

class rogerSpider(scrapy.Spider):
    name = 'roger'
    start_urls = ['https://www.rogerebert.com/movies/A']
    def parse(self, response):
        SET_SELECTOR = '.details'

        for object in response.css(SET_SELECTOR):
                NAME_SELECTOR = 'a ::text'
                yield{
                    'name': object.css(NAME_SELECTOR).extract_first(),
                    }
