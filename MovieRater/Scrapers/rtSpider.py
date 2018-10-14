# -*- coding: utf-8 -*-
import scrapy
import unicodedata
pageCounter = 1
class rottenTomatoesSpider(scrapy.Spider):
    name = 'RT'
    start_urls = ['https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&certified&sortBy=release&type=dvd-streaming-all&page=1']
    def parse(self, response):

        text = response.xpath('/html/body//text()').extract()
        NEXT_PAGE = True
        #converts unicode to strings and stores in word
        for notStr in text:
            word = unicodedata.normalize('NFKD', notStr).encode('ascii', 'ignore')

            #to determine if there is a next page
            if(word.find('"count":') > 0):
                count = word
                count = count.split('"count":', 1)[1]
                counter = 0
                for char in count:
                    if(char == ','):
                        break
                    counter = counter + 1
                count = count[:counter]
                print("COUNT IS: ")
                print(count)
                if(count == "0"):
                    NEXT_PAGE = False
                    break

            #rest of code 
            while(word.find('popcornScore') > 0):
                #if text has title
                if(word.find('title') > 0):
                    #splits word to find title
                    title = word.split('title":"',1)[1]
                    word = title

                    #get all letters up to first quotation mark
                    charCounter = 0
                    for char in title:
                        if(char == '\"'):
                            break
                        charCounter = charCounter + 1
                    title = title[:charCounter]

                #if text has tomatoScore
                if(word.find('tomatoScore') > 0):
                    #splits word to find rt rating
                    rtRating = word.split('tomatoScore":', 1)[1]
                    word = rtRating
                    charCounter = 0
                    for char in rtRating:
                        if(char == ','):
                            break
                        charCounter = charCounter + 1
                    rtRating = rtRating[:charCounter]

                #if text has popcornScore
                if(word.find('popcornScore') > 0):
                    #splits word to find audience rating
                    audienceRating = word.split('popcornScore":', 1)[1]
                    word = audienceRating
                    charCounter = 0
                    for char in audienceRating:
                        if(char == ','):
                            break
                        charCounter = charCounter + 1
                    audienceRating = audienceRating[:charCounter]
          
                #yields data
                yield {
                    "name": title,
                    "rtRating": rtRating,
                    "audienceRating": audienceRating
                }

        #fetches next page
        global pageCounter
        pageCounter = pageCounter + 1
        baseUrl = 'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=amazon%3Bhbo_go%3Bitunes%3Bnetflix_iw%3Bvudu%3Bamazon_prime%3Bfandango_now&certified&sortBy=release&type=dvd-streaming-all&page='
        if NEXT_PAGE:
            yield scrapy.Request(

                    response.urljoin (baseUrl + (str) (pageCounter)),
                    callback=self.parse
                )


            








