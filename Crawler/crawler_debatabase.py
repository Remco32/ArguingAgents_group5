##Run using Scrapy:
# scrapy runspider filename.py -o output.json
# i.e. scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\abortion.json
# Or for using a custom domain, run with -a domain="website.com"

import scrapy


# order of items gets messed up. Probably has to do with the for-loops. Parser doesn't mind about order though.
class QuotesSpider(scrapy.Spider):
    def __init__(self, domain='', *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.start_urls = [domain]  # overwrite start_urls with input argument

    name = "arguments_debatabase"
    start_urls = [
        # 'https://idebate.org/debatabase/culture-media/should-airbrushing-womens-bodies-be-banned'
        # 'https://idebate.org/debatabase/education/house-believes-single-sex-schools-are-good-education'
        # 'https://idebate.org/debatabase/environment-animals-philosophy-ethics-science-science-general/house-would-ban-animal'
        # 'https://idebate.org/debatabase/law-crime-policing-punishment-philosophy-ethics-life/house-supports-death-penalty',
        # 'https://idebate.org/debatabase/culture-culture-general-media-modern-culture-television/house-believes-reality-television'
        # 'https://idebate.org/debatabase/education-university-government/house-believes-university-education-should-be-free'
        # 'https://idebate.org/debatabase/health-disease-healthcare-philosophy-ethics-life/house-believes-assisted-suicide-should'
        # 'https://idebate.org/debatabase/health-addiction-health-general-society/house-believes-cannabis-should-be-legalised'
        # 'https://idebate.org/debatabase/health-health-general-weight/house-would-ban-junk-food-schools'
        'https://idebate.org/debatabase/society-gender-family/house-believes-homosexuals-should-be-able-adopt'
    ]

    def parse(self, response):

        yield {
            'Title': response.css('div.debatabase-title::text').extract(),
        }

        for claim in response.css(
                '.entity.entity-field-collection-item.field-collection-item-field-point-for.clearfix'):
            yield {
                'Pro argument': claim.css('.field-items > .field-item.even::text').extract_first(),
                'Point': claim.css(
                    '.field.field-name-field-point-point-for.field-type-text-long.field-label-above > .field-items > .field-item.even ::text').extract(),
                'Counterpoint': claim.css(
                    '.field.field-name-field-counterpoint-point-for.field-type-text-long.field-label-above > .field-items > .field-item.even ::text').extract(),
            }

        for claimCounter in response.css(
                '.entity.entity-field-collection-item.field-collection-item-field-point-against.clearfix'):
            yield {
                'Con argument': claimCounter.css('.field-items > .field-item.even::text').extract_first(),
                'Point': claimCounter.css(
                    '.field.field-name-field-point.field-type-text-long.field-label-above > .field-items > .field-item.even ::text').extract(),
                'Counterpoint': claimCounter.css(
                    '.field.field-name-field-counterpoint.field-type-text-long.field-label-above > .field-items > .field-item.even ::text').extract(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
