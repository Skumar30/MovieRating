import scrapy

### TODO: Next page

class metaSpider(scrapy.Spider):
    name = 'meta'
    start_urls = ['https://www.metacritic.com/browse/movies/title/dvd']

    def parse(self, response):
        print ("its runnning")
        counter = 0
        SET_SELECTOR = '.summary_row'

        for object in response.css(SET_SELECTOR):
            counter = counter + 1
            if(counter > 1):
                yield{
                    'name': object.xpath('td[2]//div//a//text()').extract_first().encode("utf-8"),
                    'metaRating': object.xpath('td[1]//a//div//text()').extract_first().encode("utf-8"),
                    'year': object.xpath('td[4]//span[1]//text()').extract_first().encode("utf-8")[-4:]
                    }
