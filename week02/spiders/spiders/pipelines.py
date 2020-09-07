# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class SpidersPipeline:
    def open_spider(self, spider):
        dbInfo = {}
        with open("spiders/dbinfo.cfg", "r") as f:
            for line in f.readlines():
                key, val = line.strip('\n').split('=')
                dbInfo[key] = val
        self.conn = pymysql.connect(
            host=dbInfo['host'],
            port=int(dbInfo['port']),
            user=dbInfo['user'],
            db=dbInfo['db'],
            password=dbInfo['password']
        )

    def process_item(self, item, spider):
        title = item['title']
        categories = ', '.join(item['categories'])
        release_time = item['release_time']
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO maoyan_movie (name, category, release_time) VALUES (%s, %s， %s);"
            cursor.execute(sql, (title, categories, release_time))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            cursor.close()
        return item

    def close_spider(self, spider):
        self.conn.close()
