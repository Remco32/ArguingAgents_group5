##Run using Scrapy:
#scrapy runspider crawler_procon_org.py -o output.json

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "pro_arguments_marijuana"
    start_urls = [
        'https://medicalmarijuana.procon.org/view.answers.php?questionID=001325',
    ]

    def parse(self, response):
        for proArgument in response.css('.newblue-editortext'):
            yield {
                #'text': proArgument.css('div.newblue-editortext::text').extract_first(), //stops at first <tag> of any sort
                'text': proArgument.css('.newblue-editortext::text').extract(),
                #'author': proArgument.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)