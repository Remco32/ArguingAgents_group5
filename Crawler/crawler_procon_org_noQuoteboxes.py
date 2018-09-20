##Run using Scrapy:
#scrapy runspider filename.py -o output.json

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "arguments_gun-control"
    start_urls = [
        #'https://medicalmarijuana.procon.org/view.answers.php?questionID=001325',
        'https://gun-control.procon.org/'
    ]

    def parse(self, response):
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