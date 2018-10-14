# -*- coding: utf-8 -*-
import scrapy


# class rogerSpider(scrapy.Spider):
#     name = 'roger'
#     start_urls = ['https://www.rogerebert.com/movies/A']
#     def parse(self, response):
#         myTitles = []
#         myRatings = []
#         SET_SELECTOR = '.details'
#         for object in response.css(SET_SELECTOR):
#                 NAME_SELECTOR = 'a ::text'
#                 yield{
#                     'name': object.css(NAME_SELECTOR).extract_first(),
#                 }

#######################
# class metaSpider(scrapy.Spider):
#     name = 'meta'
#     start_urls = ['https://www.metacritic.com/browse/movies/title/dvd']
    
#     def parse(self, response):
#         print ("its runnning")
#         counter = 0
#         SET_SELECTOR = '.summary_row'

#         for object in response.css(SET_SELECTOR):
#             counter = counter + 1
#             if(counter > 1):
#                 yield{
#                     'name': object.xpath('td[2]//div//a//text()').extract_first().encode("utf-8"),
#                     'metaRating': object.xpath('td[1]//a//div//text()').extract_first().encode("utf-8"),
#                     'year': object.xpath('td[4]//span[1]//text()').extract_first().encode("utf-8")[-4:]
#                     }

# class rogerSpider(scrapy.Spider):
#     name = 'roger'
#     start_urls = ['https://www.rogerebert.com/movies/A']
#     def parse(self, response):
#         SET_SELECTOR = '.details'

#         for object in response.css(SET_SELECTOR):
#                 NAME_SELECTOR = 'a ::text'
#                 yield{
#                     'name': object.css(NAME_SELECTOR).extract_first().encode("utf-8"),
#                     }
class boxOfficeSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.boxofficemojo.com/movies/alphabetical.htm?letter=A&p=.htm']

    def parse(self, response):
        counter = 0
        print ("its runnning")

        SET_SELECTOR = 'tr'

        # for object in response.css(SET_SELECTOR):
        #     counter = counter + 1
        #     if (counter > 5):
        #         NAME_SELECTOR_1 = 'a ::text'
        #         yield{
        #             'name': object.css(NAME_SELECTOR_1).extract_first().encode("utf-8"),
        #             'boxOffice': object.xpath('td[3]//text()').extract_first().strip("$*").encode("utf-8"),
        #             'year': object.xpath('td[7]//text()').extract_first().encode("utf-8")[-4:],
                    
        #         }
# //*[@id="body"]/div/table/tbody/tr/td/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[3]/font
# //*[@id="body"]/div/table/tbody/tr/td/table/tbody/tr[2]/td/div[1]/font/b[2]/a
# //*[@id="body"]/div/table/tbody/tr/td/table/tbody/tr[2]/td/div[1]/font/b[5]/a
        NEXT_PAGE_SELECTOR = 'tr'
        for object in response.css(NEXT_PAGE_SELECTOR):
             # NAME_SELECTOR_ALPHA = 'a ::text'
             yield{'pages':object.xpath('div[1]/font//text()').extract_first()
             }
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse
        #      )c








# class boxOfficeSpider(scrapy.Spider):
#     name = 'imdb'
#     start_urls = ['https://www.boxofficemojo.com/movies/alphabetical.htm?letter=A&p=.htm']

#     def parse(self, response):
#         counter = 0
#         print ("its runnning")

#         SET_SELECTOR = 'tr'

#         for object in response.css(SET_SELECTOR):
#             counter = counter + 1
#             if (counter > 5):
#                 NAME_SELECTOR_1 = 'a ::text'
#                 yield{
#                     'name': object.css(NAME_SELECTOR_1).extract_first().encode("utf-8"),
#                     'boxOffice': object.xpath('td[3]//text()').extract_first().strip("$*").encode("utf-8"),
#                     'date': object.xpath('td[7]//text()').extract_first().encode("utf-8")
#                 }
                # if (tdCounter == 3):
                #     RTG_SELECTOR = 'font ::text'
                #     yield{'boxOffice': object.css(RTG_SELECTOR).extract_first()}
                # tdCounter = tdCounter + 1