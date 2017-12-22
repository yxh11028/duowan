# -*- coding: utf-8 -*-
import scrapy
import json
from duowan.items import DuowanItem
import os


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['duowan.com']
    _url = 'http://tu.duowan.com/m/meinv?offset='
    offset = 330
    start_urls = [_url + str(offset)]
    os.mkdir('img')

    def parse(self, response):
        url_list = response.xpath('//em/a/@href').extract()
        for url in url_list:
            url_offset = url.split('/')[-1].split('.')[0]
            os.mkdir('img/' + url_offset)
            url_request = 'http://tu.duowan.com/index.php?r=show/getByGallery/&gid=' + url_offset
            # print url
            yield scrapy.Request(url=url_request, meta={'url': url_offset}, callback=self.parse_item)

        if self.offset < 2550:  # 2550
            self.offset += 30
        yield scrapy.Request(self._url + str(self.offset), callback=self.parse)

    def parse_item(self, response):
        sites = json.loads(response.body_as_unicode())
        for site in sites['picInfo']:
            item = DuowanItem()
            item['img_url'] = site['url']
            item['path'] = response.meta['url']
            yield item
