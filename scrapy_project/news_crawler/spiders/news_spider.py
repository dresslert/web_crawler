import scrapy
import logging
from news_crawler.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = [
        'https://g1.globo.com',  
    ]

    def parse(self, response):
        logging.info(f"Parsing response from {response.url}")
        
        item = NewsItem()
        item['url'] = response.url
        item['html_content'] = response.text  

        for article in response.css('div.feed-post-body'):
            article_item = NewsItem()
            article_item['title'] = article.css('a.feed-post-link::text').get()
            article_item['link'] = article.css('a.feed-post-link::attr(href)').get()
            article_item['summary'] = article.css('div.feed-post-body-resumo::text').get()
            yield article_item
        
        next_page = response.css('a.load-more-link::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

        yield item
