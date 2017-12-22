# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib2
import uuid


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}


class DuowanPipeline(object):
    def process_item(self, item, spider):
        url = item['img_url']
        path = item['path']
        _request = urllib2.Request(url=url, headers=header)
        page = urllib2.urlopen(_request).read()
        uuid.uuid4()
        with open('img/' + path + '/' + str(uuid.uuid4()).replace('-', '') + '.' + url.split('.')[-1], 'wb') as f:
            f.write(page)
