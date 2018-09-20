##Run using Scrapy:
#scrapy runspider crawler_procon_org.py -o output.json

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "arguments_marijuana"
    start_urls = [
        #'https://medicalmarijuana.procon.org/view.answers.php?questionID=001325',
        'https://gun-control.procon.org/'
    ]

    def parse(self, response):
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