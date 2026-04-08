from scrapy import Spider


class SportsPipeline:

    def open_spider(self, spider: Spider):
        spider.logger.info('- Run spider: %s', spider.name)

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider: Spider):
        spider.logger.info('- Spider has been closed')
        pass