import pymongo
import logging

class MongoPipeline:
    def open_spider(self, spider):
        logging.info("Opening MongoDB connection")
        self.client = pymongo.MongoClient('mongo', 27017)
        self.db = self.client['news_db']
        self.collection = self.db['news']

    def close_spider(self, spider):
        logging.info("Closing MongoDB connection")
        self.client.close()

    def process_item(self, item, spider):
        logging.info(f"Inserting item into MongoDB: {item}")
        self.collection.insert_one(dict(item))
        return item
