import scrapy
import json
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
letterCounter = 1
class rogerSpider(scrapy.Spider):
    os.remove("output.json")
    name = 'roger'
    start_urls = ['https://www.rogerebert.com/movies/A']
    def parse(self, response):

        #to dump into json file
        data = []

        #one for every rating
        RTG_SELECTOR = '.details'

        #starts at 1 due to xpath
        ratingCounter = 1

        #parts of the xpath
        xpathPart1 = "//*[@id='filmography']/li["
        xpathPart2 = "]/span/span/i"

        #goes through every rating on the webpage
        for object in response.css(RTG_SELECTOR):

            #more specific selector to get name of every movie
            NAME_SELECTOR = 'a ::text'

            #both reset at beginning of every movie
            starCounter = 1
            starRating = 0

            #stores name and year
            testName = object.css(NAME_SELECTOR).extract_first()[:-7] #good print statement
            testYear = object.css(NAME_SELECTOR).extract_first()[-5:-1] # good print statement

            #goes through and collects ratings for all movies
            for object in response.xpath(xpathPart1 + (str) (ratingCounter) + xpathPart2):
                starValue = object.xpath(xpathPart1 + (str) (ratingCounter) + xpathPart2 + "[" + (str) (starCounter) + "]/@class").extract_first()

                #if star is full adds 1 to rating
                if(starValue == 'icon-star-full'):
                    starRating = starRating + 1

                #else adds 0.5
                else:
                    starRating = starRating + 0.5
                starCounter = starCounter + 1

            #moves to next movie
            ratingCounter = ratingCounter + 1
            data.append({
                'name': testName,
                'year': testYear,
                'rogerRating': (str) (starRating)
            })

        #appends to output file
        with open('output.json', 'a') as outfile:
            json.dump(data, outfile)

        #gets url for next page
        next_page = response.xpath("//li[contains(@class, 'next_page')]/a/@href").extract_first()

        #sets baseUrl for roger ebert webpages
        baseUrl = "https://www.rogerebert.com"
        print("baseUrl is: " + baseUrl)
        print("next page url is: " + (str)(next_page))

        #if a next page exists then scrape the next page
        if next_page:
            yield scrapy.Request(
                response.urljoin((str)(baseUrl + next_page)),
                callback=self.parse
            )
        else :
            global letterCounter
            letterCounter = letterCounter + 1
            next_letter = response.xpath("/html/body/div[1]/ul[1]/li[" + (str)(letterCounter) + "]/a/@href").extract_first()
            if next_letter:
                yield scrapy.Request(
                    response.urljoin((str)(baseUrl + next_letter)),
                    callback=self.parse
                )
