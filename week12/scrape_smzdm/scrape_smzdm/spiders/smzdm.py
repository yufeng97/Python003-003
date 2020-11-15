import datetime
import re
import scrapy
from scrapy import Selector
from urllib.parse import urljoin, urlparse
from ..items import BrandItem, CommentItem


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    def parse(self, response):
        selector = Selector(response)
        article_tags = selector.xpath('//h5[position()<5]/a')
        for article in article_tags:
            item = {}
            item['article_title'] = article.xpath('./text()').get()
            item['article_url'] = article.xpath('./@href').get()
            yield scrapy.Request(item['article_url'], meta=item, callback=self.parse_detail)
        
    def parse_detail(self, response):
        selector = Selector(response)
        title = selector.xpath('//h1/text()').get()
        article_title = title.split("：")[-1].strip()
        print(article_title)        

        brand_item = BrandItem()
        tags = selector.xpath('//ul[@class="z-clearfix"]/li[position()<4]//span/@data-type').getall()
        aa = selector.xpath('//ul[@class="z-clearfix"]/li[position()<4]/div')
        for a in aa:
            data_type = a.xpath('.//span/@data-type').get()
            type_value = a.xpath('./a').xpath('string(.)').get().strip()
            brand_item[data_type] = type_value

        brand_item['article_title'] = article_title
        article_id = int(urlparse(response.url).path.split("/")[2])
        brand_item['article_id'] = article_id
        yield brand_item

        comment_list = selector.xpath('//ul[@class="comment_listBox"]/li')
        for comment_box in comment_list:
            temp = []
            comment_item = CommentItem()

            comment_id = comment_box.xpath('./@id').get()
            comment_id = comment_id.rsplit('_', 1)[-1]
            temp.append(comment_id)
            comment_item['comment_id'] = comment_id

            user = comment_box.xpath('.//span[@itemprop="author"]/text()').get()
            temp.append(user)
            comment_item['username'] = user

            comment_time = comment_box.xpath('.//div[@class="time"]/text()').get()
            delta = None
            pattern = re.compile("\d*")
            try:
                num = int(pattern.match(comment_time).group())
                if "分钟" in comment_time:
                    delta = datetime.timedelta(minutes=num)
                elif "小时" in comment_time:
                    delta = datetime.timedelta(hours=num)
                comment_time = datetime.datetime.today() - datetime.timedelta()
                comment_time = comment_time.strftime("%Y-%m-%d %H:%M:%S")            
                temp.append(comment_time)
                comment_item['datetime'] = comment_time
            except Exception:
                continue
            comment_content = comment_box.xpath('./div[@class="comment_conBox"]/div[@class="comment_conWrap"]/div[1]//span/text()').get()
            temp.append(comment_content)
            comment_item['content'] = comment_content

            comment_item['article_id'] = article_id

            # print(temp)
            yield comment_item
        
        pagedown = selector.xpath('//li[@class="pagedown"]/a/@href').get()
        if pagedown:
            yield scrapy.Request(pagedown, callback=self.parse_comment)

    def parse_comment(self, response):
        selector = Selector(response)
        comment_list = selector.xpath('//ul[@class="comment_listBox"]/li')
        article_id = int(urlparse(response.url).path.split("/")[2])
        for comment_box in comment_list:
            temp = []
            comment_item = CommentItem()

            comment_id = comment_box.xpath('./@id').get()
            comment_id = comment_id.rsplit('_', 1)[-1]
            temp.append(comment_id)
            comment_item['comment_id'] = comment_id

            user = comment_box.xpath('.//span[@itemprop="author"]/text()').get()
            temp.append(user)
            comment_item['username'] = user

            comment_time = comment_box.xpath('.//div[@class="time"]/text()').get()
            delta = None
            pattern = re.compile("\d*")
            num = int(pattern.match(comment_time).group())
            if "分钟" in comment_time:
                delta = datetime.timedelta(minutes=num)
            elif "小时" in comment_time:
                delta = datetime.timedelta(hours=num)
            comment_time = datetime.datetime.today() - datetime.timedelta()
            comment_time = comment_time.strftime("%Y-%m-%d %H:%M:%S")            
            temp.append(comment_time)
            comment_item['datetime'] = comment_time

            comment_content = comment_box.xpath('./div[@class="comment_conBox"]/div[@class="comment_conWrap"]/div[1]//span/text()').get()
            temp.append(comment_content)
            comment_item['content'] = comment_content
            comment_item['article_id'] = article_id

            # print(temp)
            yield comment_item

        pagedown = selector.xpath('//li[@class="pagedown"]/a/@href').get()
        if pagedown:
            yield scrapy.Request(pagedown, callback=self.parse_comment)
