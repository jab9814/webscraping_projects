from enum import Enum


class UserConfig(Enum):
    
    MAIN_URL = "https://quotes.toscrape.com/"
    LOGIN = "https://quotes.toscrape.com/login"
    TOKEN = "//input[@name='csrf_token']/@value"
    NAME = 'juancho'          # Lo recomendable es utilizar variables de entorno 
    PASSWORD = 'Juancho321'   # Lo recomendable es utilizar variables de entorno 


class XpathConfig(Enum):
    ALL_QUOTES = "//div[@class='quote']"
    NEXT_PAGE = "//li[@class='next']/a/@href"
    QUOTE = "./*[@class='text']/text()"
    QUOTE_BY = ".//*[@itemprop='author']/text()"
    TAGS = ".//*[@class='tag']/text()"
    SOURCE_URL = ".//a[text()='(about)']/@href"
    BORN = "//span[@class='author-born-date']/text()"
    LOCATION = "//span[@class='author-born-location']/text()"
    DESCRIPTION = "normalize-space(//div[@class='author-description']/text())"