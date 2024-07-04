
BOT_NAME = 'news_crawler'

SPIDER_MODULES = ['news_crawler.spiders']
NEWSPIDER_MODULE = 'news_crawler.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'news_crawler.pipelines.MongoPipeline': 300,
}

MONGO_URI = 'mongodb://mongo:27017'
MONGO_DATABASE = 'news_database'
