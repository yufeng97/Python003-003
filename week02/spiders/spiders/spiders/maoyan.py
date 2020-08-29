import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector
from urllib.parse import urljoin


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    BASE_URL = 'https://maoyan.com'

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        selector = Selector(response=response)
        links = selector.xpath('//div[@class="channel-detail movie-item-title"]/a/@href').getall()[:10]
        for link in links:
            url = urljoin(self.BASE_URL, link)
            yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        item = SpidersItem()
        selector = Selector(response=response)
        movie_brief = selector.xpath('//div[@class="movie-brief-container"]')
        title = movie_brief.xpath('./h1/text()').get()
        categories = movie_brief.xpath('.//a/text()').getall()
        categories = [category.strip() for category in categories]
        release_time = movie_brief.xpath('.//li[last()]/text()').get()
        item['title'] = title
        item['categories'] = categories
        item['release_time'] = release_time
        yield item