import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, NAME, START_URLS


class PepSpider(scrapy.Spider):
    name = NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        numerical_table = response.css('table.pep-zero-table')
        pep_links = numerical_table.css('a[href^="pep-"]')
        for pep in pep_links:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('h1.page-title::text').get().split(' – ')
        data = {
            'number': int(number.split(' ')[1]),
            'name': name,
            'status': response.css('dt:contains("Status")+dd abbr::text').get()
        }
        yield PepParseItem(data)
