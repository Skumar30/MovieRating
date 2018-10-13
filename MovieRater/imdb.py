import scrapy
### THIS FILE IS COMPLETE
counter = 0
class imdbSpider(scrapy.Spider):

    name = 'imdb'
    start_urls = ['https://www.imdb.com/search/title?title_type=feature&user_rating=1.0,10.0&sort=alpha,asc']

    def parse(self, response):

        SET_SELECTOR = '.lister-item-content'
        global counter
        for object in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a ::text'
            YEAR_SELECTOR = '.lister-item-year ::text'
            GENRE_SELECTOR = '.genre ::text'
            yield{

                 'name': object.css(NAME_SELECTOR).extract_first(),


                 'imdbRating': object.xpath(".//strong/text()").extract_first(),
                 'year': object.css(YEAR_SELECTOR).extract_first().strip("()"),
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
