import scrapy

# XPath

# numberofcases = //div[@class="barbox tright"]//tr[@id="mw-customcollapsible-aug-l15"]//span[@class="cbs-ibr"]/text()').get()
# negative = //div[@id="gsNegDIV"]/text()
# suspicious = //div[@id="gsSosDIV"]/text()
# dead = //div[@id="gsDefDIV"]/text()
# recovery = //div[@id="gsRecDIV"]/text()
# active = //div[@id="gsActDIV"]/text()


class SpiderCIA(scrapy.Spider):
    name = 'covid'
    start_urls = [
        'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Mexico'
    ]
    custom_settings = {
        'FEED_URI': 'covid.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):

        cases = response.xpath('//div[@class="barbox tright"]//tr[@id="mw-customcollapsible-aug-l15"]//span[@class="cbs-ibr"]/text()').get()
        dead = response.xpath('//div[@class="barbox tright"]//tr[@id="mw-customcollapsible-aug-l15"]/td[last()]/span[@class="cbs-ibr"]/text()').get()


        yield {
            'cases': cases,
            'dead': dead
        }