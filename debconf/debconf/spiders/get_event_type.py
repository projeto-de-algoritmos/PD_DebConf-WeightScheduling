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
            url = f"https://debconf23.debconf.org{link}"
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def create_dict(self, title, event_type):
        event_catalogue = {
            'titulo': title,
            'tipo': event_type,
        }
        return self.save_json(event_catalogue)

    def save_json(self, catalogue):
        file_path = '../events.json'
        try:
            with open(file_path, 'r') as fp:
                existing_data = json.load(fp)
        except (json.JSONDecodeError, FileNotFoundError):
            existing_data = {}
        existing_data.update(catalogue)
        with open(file_path, 'a') as fp:
            json.dump(existing_data, fp, indent=4)

    def parse_dir_contents(self, response):
        title = response.xpath('//h1/text()').extract()
        title = title[0].strip()

        event_type = response.xpath('//div/p/text()').re('Type:\s*(.+)')
        event_type = event_type[0]
        
        return self.create_dict(title, event_type)
