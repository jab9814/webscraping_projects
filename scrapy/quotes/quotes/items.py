import scrapy


class QuotesItem(scrapy.Item):
    quote = scrapy.Field()
    quote_by = scrapy.Field()
    tags = scrapy.Field()
    born = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()
    sourcel_url = scrapy.Field()
