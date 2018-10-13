import scrapy



class imdbSpider(scrapy.Spider):

    name = 'imdb'
    start_urls = ['https://www.imdb.com/search/title?title_type=feature&user_rating=1.0,10.0&sort=alpha,asc']

    def parse(self, response):
        print ("its runnning")

        SET_SELECTOR = '.lister-item-content'

        for object in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a ::text'
            YEAR_SELECTOR = 'lister-item-year ::text'
            yield{

                 'name': object.css(NAME_SELECTOR).extract_first(),


                 'imdbRating': object.xpath(".//strong/text()").extract_first(),
                 'year': object.css(YEAR_SELECTOR).extract_first(),


            }
