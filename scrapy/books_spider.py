import scrapy
from os import path
from enum import Enum
from scrapy import Selector
from scrapy.http import Response
from scrapy.crawler import CrawlerProcess


class ConfigXpath(Enum):

    # xpath desde la pagina principal de los libros
    PAGE_PRODUCTS = '//article[@class="product_pod"]'
    PAGE_IMAGE = './/img/@src'
    PAGE_TITLE = './/h3//text()'
    PAGE_URL_INFO = './/h3//@href'
    PAGE_PRICE = './/div[@class="product_price"]/p[1]/text()'
    PAGE_STATUS = './/div[@class="product_price"]/p[2]/text()[2]'
    PAGE_NEXT_PAGE ='//a[contains(@href, "catalogue/page")]/@href|//li[@class="next"]//@href'

    # xpath desde la pagina de informacion del libro
    BOOK_NAME = '//h1/text()'
    BOOK_PRICE = '//p[@class="price_color"]/text()'
    BOOK_STATUS_AND_COUNT = '//p[@class="instock availability"]/text()[2]'
    BOOK_IMAGE = '//img/@src'
    BOOK_DESCRIPTION = '//div[@id="product_description"]/../p/text()'
    BOOK_TAX = '//th[contains(text(), "Tax")]/../td/text()'


class BooksSpider(scrapy.Spider):
    name = "books_spider"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response: Response):

        # Extraer los productos de la pagina principal

        all_products =  response.xpath(ConfigXpath.PAGE_PRODUCTS.value)
        if not all_products:
            self.logger.warning('No se encontraron productos en la pagina: %s', response.url)
            return None
        
        self.logger.info('Existen productos en la pagina: %s', response.url)

        for product in all_products:
            book_data = get_book_data(product, self.start_urls[0])
            yield scrapy.Request(
                book_data[ConfigXpath.PAGE_URL_INFO.name],
                callback=self.parse_info_book,
                meta={"book_data": book_data},
                dont_filter=True
            )

        next_page = response.xpath(ConfigXpath.PAGE_NEXT_PAGE.value).get()
        if next_page is None:
            self.logger.warning('Finalizado el salto de paginas')
            return None
        yield response.follow(next_page, callback=self.parse)


    def parse_info_book(self, response: Response):

        # Extraer la informacion del libro desde la pagina de detalles

        book_data = response.meta.get("book_data", {})
        book_info = get_book_info(response, self.start_urls[0])
        output_data = book_data | book_info
        yield output_data


def get_book_data(product: Selector, base_url: str) -> dict[str, str]:
    book_data = {
        ConfigXpath.PAGE_IMAGE.name: product.xpath(ConfigXpath.PAGE_IMAGE.value).get(default='').strip(),
        ConfigXpath.PAGE_TITLE.name: product.xpath(ConfigXpath.PAGE_TITLE.value).get(default='').strip(),
        ConfigXpath.PAGE_URL_INFO.name: product.xpath(ConfigXpath.PAGE_URL_INFO.value).get(default='').strip().replace("catalogue/", ''),
        ConfigXpath.PAGE_PRICE.name: product.xpath(ConfigXpath.PAGE_PRICE.value).get(default='').strip(),
        ConfigXpath.PAGE_STATUS.name: product.xpath(ConfigXpath.PAGE_STATUS.value).get(default='').strip(),
    }
    
    book_data[ConfigXpath.PAGE_URL_INFO.name] = get_path_url(base_url, "catalogue", book_data[ConfigXpath.PAGE_URL_INFO.name])
    book_data[ConfigXpath.PAGE_IMAGE.name] = get_path_url(base_url, book_data[ConfigXpath.PAGE_IMAGE.name])
    return book_data


def get_book_info(response: Selector, base_url: str) -> dict[str, str]:

    book_info = {
        ConfigXpath.BOOK_NAME.name: response.xpath(ConfigXpath.BOOK_NAME.value).get(default='').strip(),
        ConfigXpath.BOOK_PRICE.name: response.xpath(ConfigXpath.BOOK_PRICE.value).get(default='').strip(),
        ConfigXpath.BOOK_STATUS_AND_COUNT.name: response.xpath(ConfigXpath.BOOK_STATUS_AND_COUNT.value).get(default='').strip(),
        ConfigXpath.BOOK_IMAGE.name: response.xpath(ConfigXpath.BOOK_IMAGE.value).get(default='').strip(),
        ConfigXpath.BOOK_DESCRIPTION.name: response.xpath(ConfigXpath.BOOK_DESCRIPTION.value).get(default='').strip(),
        ConfigXpath.BOOK_TAX.name: response.xpath(ConfigXpath.BOOK_TAX.value).get(default='').strip(),
    }

    book_info[ConfigXpath.BOOK_IMAGE.name] = get_path_url(base_url, book_info[ConfigXpath.BOOK_IMAGE.name])

    return book_info


def get_path_url(*args: str) -> str:
    return path.join(*args).replace("\\", "/").replace("../", '')


def run_spider():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "data/books.json": {"format": "json", "encoding": "utf-8", "indent": 4, "overwrite": True},
        },
        "ROBOTSTXT_OBEY": False,
        "CONCURRENT_REQUESTS": 4,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2,
        "HTTPCACHE_ENABLED": True,
        "HTTPCACHE_EXPIRATION_SECS": 3600,
        "LOG_LEVEL": "INFO",
    })
    process.crawl(BooksSpider)
    process.start()


if __name__ == "__main__":
    run_spider()
