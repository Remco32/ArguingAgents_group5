##Run using Scrapy:
#scrapy runspider filename.py -o output.json

import scrapy

#TODO order of items gets messed up. Probably has to do with the for-loops
class QuotesSpider(scrapy.Spider):
    name = "arguments_debatabase"
    start_urls = [
        'https://idebate.org/debatabase/culture-media/should-airbrushing-womens-bodies-be-banned'
    ]

    def parse(self, response):

        yield{
            'Title': response.css('div.debatabase-title::text').extract(),
        }


        for claim in response.css('.entity.entity-field-collection-item.field-collection-item-field-point-for.clearfix'):
            yield {
                'Pro argument': claim.css('.field-items > .field-item.even::text').extract_first(),
                'Point': claim.css('.field.field-name-field-point-point-for.field-type-text-long.field-label-above > .field-items > .field-item.even > p::text').extract(), #TODO remove sources from mined text
                'Counterpoint': claim.css('.field.field-name-field-counterpoint-point-for.field-type-text-long.field-label-above > .field-items > .field-item.even > p::text').extract(),

            }

        for claimCounter in response.css('.field.field-name-field-title.field-type-text.field-label-above'):
            yield {
                'Con argument': claimCounter.css('.field-items > .field-item.even::text').extract_first(),
                #'Point': claim.css('.field.field-name-field-point-point-for.field-type-text-long.field-label-above > .field-items > .field-item.even > p::text').extract(), #TODO remove sources from mined text
                #'Counterpoint': claim.css('.field.field-name-field-counterpoint-point-for.field-type-text-long.field-label-above > .field-items > .field-item.even > p::text').extract(),
            }


        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)