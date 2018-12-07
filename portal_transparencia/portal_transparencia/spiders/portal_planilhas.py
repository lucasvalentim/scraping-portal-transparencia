# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class PortalPlanilhasSpider(scrapy.Spider):
    name = 'portal_planilhas'
    allowed_domains = ['http://www.portaltransparencia.gov.br']
    start_urls = ['http://www.portaltransparencia.gov.br/download-de-dados']

    def parse(self, response):
        links_secoes = response.xpath(
            '//div[./@class[contains(., "box-tabela-principal")]]/div/table/'
            'tbody/tr/td[1]/a/@href').extract()
        # import ipdb; ipdb.set_trace()

        for link in links_secoes:
            yield Request(url=self.allowed_domains[0] + link,
                          callback=self.parse_links)

    def parse_links(self, response):
        import ipdb; ipdb.set_trace()