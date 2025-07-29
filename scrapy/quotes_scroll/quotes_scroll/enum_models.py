from enum import Enum


class ConfigGeneral(Enum):
    EXTRACTOR_DOCUMENT_NAME_PATH = 'data/quotes_scroll.json'
    REFINE_DOCUMENT_NAME_PATH = 'data/quotes_scroll_refine.csv'
    FORMAT = 'json'
    ENCODING = 'utf8'
    STORE_EMPTY = True
    OVERWRITE = True

class ConfigPage(Enum):
    BASE_URL = "https://quotes.toscrape.com/scroll"
    INIT_API_URL = 'https://quotes.toscrape.com/api/quotes?page=1'
    API_BASE_URL = 'https://quotes.toscrape.com/api/quotes?page='
    BASE_URL_GOODREADS = "https://www.goodreads.com"


class ConfigXpath(Enum):
    GOODREADS_NAME = "normalize-space(//span[@itemprop='name']/text())"
    GOODREADS_BORN_DATE = "normalize-space(//div[@itemprop='birthDate']/text())"
    GOODREADS_DEATH_DATE = "normalize-space(//div[@itemprop='deathDate']/text())"
    GOODREADS_BORN_LOCATION = "normalize-space(//div[@class='dataTitle'][text()='Born']/following-sibling::text()[1])"
    GOODREADS_DESCRIPTION = "//span[contains(@id, 'freeTextContainerauthor')]//text()"
