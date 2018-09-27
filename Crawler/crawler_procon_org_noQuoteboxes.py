##Run using Scrapy:
#scrapy runspider filename.py -o output.json

#For some reason arguments get mixed in the JSON file when crawling too many (>2?) pages. Simply crawling one page at a time is a workaround.

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "arguments_procon_org_noQuoteBoxes"
    start_urls = [
        #'https://gun-control.procon.org/',
        #'https://animal-testing.procon.org/',
        #'https://marijuana.procon.org/',
        #'https://school-uniforms.procon.org/',
        #'https://drinkingage.procon.org/',
        'https://socialnetworking.procon.org/'
    ]

    def parse(self, response):

        yield{
            'Title': response.css('title::text').extract_first()
        }
        for proArgument in response.css('div.newblue-pro-quote-box'):
            yield {
                'Pro argument': proArgument.css('.newblue-arguments-bolded-intro::text').extract(),
                'Pro argument text': proArgument.css('.newblue-pro-quote-box::text').extract(),
            }
        for conArgument in response.css('div.newblue-con-quote-box'):
            yield {
                'Con argument': conArgument.css('.newblue-arguments-bolded-intro::text').extract(),
                'Con argument text': conArgument.css('.newblue-con-quote-box::text').extract(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)