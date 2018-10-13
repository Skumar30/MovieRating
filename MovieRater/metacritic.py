import scrapy
class metaSpider(scrapy.Spider):
    name = 'meta'
    start_urls = ['https://www.metacritic.com/browse/movies/title/dvd']
    def parse(self, response):
        print ("its runnning")

        SET_SELECTOR = '.title'
        flag = False

        for object in response.css(SET_SELECTOR):

            if flag :
                NAME_SELECTOR = 'a ::text'
                yield{
                    'name': object.css(NAME_SELECTOR).extract_first(),
                    }
            else :
                flag = True
'''
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.action',)),
        callback="parse_item",
        follow=True),)

    def parse_item(self, response):
        #print('Processing..' + response.url)
        #this is for parsing through links on webpages such as the next page
        print("running")
        item_links = response.css('.large > . detailsLink:attr(href)').extract()
                for a in item_links:
                    yield scrapy.Request(a, callback=self.parse_detail_page)

        #this is for parsing through scores on a given page,
        #i'm not sure where this one is supposed to go
        meta_scores = response.css('.metascore_w large movie mixed::text').extract()
                for a in meta_scores:
                    print("i think this works")
'''
