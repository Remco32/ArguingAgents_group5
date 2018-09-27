##Run using Scrapy:
#scrapy runspider filename.py -o output.json

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "arguments_debatabase"
    start_urls = [
        'https://idebate.org/debatabase/culture-media/should-airbrushing-womens-bodies-be-banned'
    ]

    def parse(self, response):

        yield{
            'Title': response.css('div.debatabase-title::text').extract(),
        }


        for claim in response.css('.field.field-name-field-title-point-for.field-type-text.field-label-above'):
            yield {
                'Pro argument': claim.css('.field-items > .field-item.even::text').extract_first(),
            }

        for claimCounter in response.css('.field.field-name-field-title.field-type-text.field-label-above'):
            yield {
                'Con argument': claimCounter.css('.field-items > .field-item.even::text').extract_first(),
            }


        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)