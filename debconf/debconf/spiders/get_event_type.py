import scrapy
import re
import json

class EventTypeSpider(scrapy.Spider):
    name = "event_type"
    allowed_domains = ["debconf.org"]
    start_urls = [
        "https://debconf23.debconf.org/talks/"
    ]

    def parse(self, response):
        all = response.xpath('//div/table/tr/td/a')
        i = 0
        for a in all:
            find_links = a.xpath('//@href').re('^\/talks/\d.*$')
            if find_links and i == 0:
                i = i + 1
        
        for link in find_links:
            print(link)
            print("----")
            url = f"https://debconf23.debconf.org{link}"
            return scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        title = response.xpath('//h1/text()').extract()
        title = title[0].strip()

        event_type = response.xpath('//div/p/text()').re('Type:\s*(.+)')
        event_type = event_type[0]