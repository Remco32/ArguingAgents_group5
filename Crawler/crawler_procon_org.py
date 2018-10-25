##Run using Scrapy:
# scrapy runspider crawler_procon_org.py -o output.json

import scrapy


class QuotesSpider(scrapy.Spider):
    def __init__(self, domain='', *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.start_urls = [domain]  # overwrite start_urls with input argument

    name = "arguments_procon_org"
    start_urls = [
        # 'https://medicalmarijuana.procon.org/view.answers.php?questionID=001325',
        # 'https://euthanasia.procon.org/view.answers.php?questionID=001320',
        # 'https://immigration.procon.org/view.answers.php?questionID=001362'
        'https://prostitution.procon.org/view.answers.php?questionID=001315'
    ]

    def parse(self, response):
        yield {
            'Title': response.css('title::text').extract_first()
        }
        for proArgument in response.css('div.newblue-pro-quote-box > div.newblue-quote-indent'):
            yield {
                'Pro argument': proArgument.css('.newblue-editortext::text').extract(),
            }
        for conArgument in response.css('div.newblue-con-quote-box > div.newblue-quote-indent'):
            yield {
                'Con argument': conArgument.css('.newblue-editortext::text').extract(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
