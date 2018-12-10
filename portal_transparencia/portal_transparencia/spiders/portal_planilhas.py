# -*- coding: utf-8 -*-
import re
import json
import scrapy
from scrapy.http import Request


class PortalPlanilhasSpider(scrapy.Spider):
    name = 'portal_planilhas'
    allowed_domains = ['www.portaltransparencia.gov.br']
    start_urls = ['http://www.portaltransparencia.gov.br/download-de-dados']

    def parse(self, response):
        links_secoes = response.xpath(
            '//div[./@class[contains(., "box-tabela-principal")]]/div/table/'
            'tbody/tr/td[1]/a/@href').extract()

        for link in links_secoes:
            yield Request(
                url=f'http://www.portaltransparencia.gov.br{link}',
                callback=self.parse_links
            )

    def parse_links(self, response):
        script = response.xpath('/html/body/script')[-1].extract()
        results = re.findall(r'\{[^}]+\}', script)
        dates = [json.loads(result) for result in results]
        file_links = [response.url + '/' + date['ano'] + date['mes'] + date['dia'] for date in dates]

        yield {'file_urls': file_links}
