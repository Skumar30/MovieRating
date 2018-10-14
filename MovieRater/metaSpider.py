import scrapy

### TODO: Next page

class metaSpider(scrapy.Spider):
    name = 'meta'

    start_urls = ['https://www.metacritic.com/browse/movies/title/dvd']
                  # 'https://www.metacritic.com/browse/movies/title/dvd/a',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/b',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/c',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/d',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/e',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/f',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/g',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/h',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/i',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/j',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/k',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/l',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/m',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/n',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/o',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/p',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/q',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/r',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/s',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/t',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/u',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/v',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/w',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/x',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/y',
                  # 'https://www.metacritic.com/browse/movies/title/dvd/z',]

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

        next_page = response.xpath("//*[@id='mantle_skin']/div[4]/div[5]/div[1]/div[2]/div/div/div[1]/span[2]/a/@href").extract_first()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                 callback=self.parse
            )
