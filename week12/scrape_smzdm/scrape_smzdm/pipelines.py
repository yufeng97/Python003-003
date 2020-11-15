# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from .items import BrandItem, CommentItem


class ScrapeSmzdmPipeline:

    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'geekbang')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '')
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd)

    def process_item(self, item, spider):
        if isinstance(item, BrandItem):
            self.insert_brand(item)
        elif isinstance(item, CommentItem):
            self.insert_comment(item)
        return item

    def insert_brand(self, item):
        article_id = item['article_id']
        article_title = item['article_title']
        mall = item['mall']
        category = item['category']
        brand = item['brand']
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO zdm_phone (id, article_title, brand) VALUES (%s, %s, %s);"
            cursor.execute(sql, (article_id, brand, article_title))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            cursor.close()

    def insert_comment(self, item):
        comment_id = item['comment_id']
        article_id = item['article_id']
        username = item['username']
        datetime = item['datetime']
        content = item['content']
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO phone_comment (id, article_id, username, comment, datetime) VALUES (%s, %s, %s, %s, %s);"
            cursor.execute(sql, (comment_id, article_id, username, content, datetime))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            cursor.close()

    def close_spider(self, spider):
        self.conn.close()
