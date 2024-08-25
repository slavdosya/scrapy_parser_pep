# scrapy_parser_pep
## Описание проекта
Scrapy_parser_pep - это асинхронный парсер документов PEP, выполненный на фреймворке Scrapy
### Инструкция по пользованию.
1. Склонировать проект git clone git@github.com:slavdosya/scrapy_parser_pep.git
2. Создать виртуальное окружение python3 -m venv venv
3. Активировать виртуальное окружение . venv/bin/Activate
4. Установить зависимости pip install -r requirements.txt
5. Запустить парсер scrapy crawl pep

После парсинга в папке results появится файлы:
1. pep_дата - выводит номер, название и статус PEP документа.
2. status_summary_дата - выводит названия всех статусов, их количество и общее количество.