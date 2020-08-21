# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanmoviePipeline:
    def open_spider(self, spider):
        self.file = open("maoyan_movie.csv", "w", encoding="utf8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        title = item['title']
        categories = item['categories']
        release_time = item['release_time']
        line = "{},{},{}\n".format(title, categories, release_time)
        self.file.write(line)
        return item
