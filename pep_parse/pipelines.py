import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_summary = defaultdict(int)

    def process_item(self, item, spider):
        self.status_summary[item['status']] += 1
        return item

    def close_spider(self, spider):
        time = dt.now().strftime('%Y-%m-%dT%H-%M-%S')
        path = BASE_DIR / f'results/status_summary_{time}.csv'
        self.status_summary['Total'] = sum(self.status_summary.values())

        with open(path, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_summary.items())
