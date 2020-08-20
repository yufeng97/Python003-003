# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        title = item['title']
        categories = item['categories']
        release_time = item['release_time']
        print("#######################3")
        print(title)
        print(categories)
        print(release_time)

        # df = pd.DataFrame({
        #     # 'title': title,
        #     # 'categories': categories,
        #     # 'release_time': release_time

        # })
        df = pd.DataFrame(item)
        df.to_csv("./movie.csv", mode="a+", encoding="utf-8", header=False, index=False)
        return item
