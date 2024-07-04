import scrapy

class NewsItem(scrapy.Item):
    url = scrapy.Field()  # URL da página
    html_content = scrapy.Field()  # Conteúdo HTML completo da página
    title = scrapy.Field()  # Título do artigo
    link = scrapy.Field()  # Link do artigo
    summary = scrapy.Field()  # Resumo do artigo
