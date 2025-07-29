# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesScrollItem(scrapy.Item):
    quotes_author_name = scrapy.Field()
    quotes_author_slug = scrapy.Field()
    quotes_author_goodreads_link = scrapy.Field()
    quotes_tags = scrapy.Field()
    quotes_text = scrapy.Field()
    goodreads_name = scrapy.Field()
    goodreads_born_date = scrapy.Field()
    goodreads_death_date = scrapy.Field()
    goodreads_born_location = scrapy.Field()
    goodreads_description = scrapy.Field()