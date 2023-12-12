import scrapy
import re
import json

class ScheduleSpider(scrapy.Spider):
    name = "schedule"
    allowed_domains = ["debconf.org"]
    start_urls = [
        "https://debconf23.debconf.org/schedule/"
    ]

    def parse(self, response):
        days = response.xpath('//table/tr/td/a')

        for day in days:
            link = day.re('.?block=\d+')
            if link:
                link = link[0]
                url = f"https://debconf23.debconf.org/schedule/{link}"
                yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        regex_pattern = re.compile(r'\((\d{2}[^)]*)\)')
        all_events = []
        for line in response.xpath('//table/tr'):
            hours = line.xpath('//td[@class="scheduleslot"]/text()').re('(\d{2}:\d{2})')
            all_events = line.xpath('//td/a/text()').extract()
        day = regex_pattern.sub('', all_events.pop(0))
        day = day.strip()

        return self.create_dict(day, all_events, hours)

    def create_dict(self, day, all_events, hours):
        schedule = {}
        max_hour = len(hours)
        hour_cont = 0
        
        for event in all_events:
            if day not in schedule:
                schedule[day] = []

            if hour_cont < max_hour:
                schedule[day].append({
                    'titulo': event,
                    'horario_inicio': hours[hour_cont],
                    'horario_fim': hours[hour_cont+1],
                    'tipo': 'Other'
                })
                hour_cont = hour_cont +2
        return self.save_json(schedule)

    def save_json(self, schedule):
        file_path = '../schedule.json'
        try:
            with open(file_path, 'r') as fp:
                existing_data = json.load(fp)
        except (json.JSONDecodeError, FileNotFoundError):
            existing_data = {}

        existing_data.update(schedule)

        with open(file_path, 'w') as fp:
            json.dump(existing_data, fp, indent=4)