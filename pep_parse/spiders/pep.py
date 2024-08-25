import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

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
