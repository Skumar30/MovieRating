import scrapy

### Next Page to be done

class boxOfficeSpider(scrapy.Spider):
    name = 'boxOffice'
    start_urls = ['https://www.boxofficemojo.com/movies/alphabetical.htm?letter=A&p=.htm']

    def parse(self, response):
        counter = 0
        print ("its runnning")

        SET_SELECTOR = 'tr'

        for object in response.css(SET_SELECTOR):
            counter = counter + 1
            if (counter > 5):
                NAME_SELECTOR_1 = 'a ::text'
                yield{
                    'name': object.css(NAME_SELECTOR_1).extract_first().encode("utf-8"),
                    'boxOffice': object.xpath('td[3]//text()').extract_first().strip("$*").encode("utf-8"),
                    'date': object.xpath('td[7]//text()').extract_first().encode("utf-8")
                }
