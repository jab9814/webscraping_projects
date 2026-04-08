import scrapy
from enum import Enum
from scrapy.http.response import Response

from ..items import SportsItem
from ..comuns import change_date_format, clean_list_data
from ..enums_sports.enums_bettingtips_today import (
    ConfigBettingtipsToday, 
    ConfigBettingtipsTodayWithouNave,
)


class ConfigXpath(Enum):
    # MAIN TABLE
    DATE = "//div[@class='fixedbar']//span/text()"
    PIVOTE_TABLE = "//ul[@id='myUL']/li"
    PIVOTE_ROW = "./div"
    COUNTRY_AND_LIGA = ".//span[@class='leagueslinks']/text()"
    TIME = ".//div[@class='divtime']//text()"
    GAME = ".//div[contains(@class, 'teamsdivide')]//text()"

    # 
    INFO = ".//a/@href"
    # NAV_MENU
    INFO_NAV_MENU = ".//span[contains(@class, 'spantipresult')]/text()"

    # INFO GAME
    PREDICT_INFO_1 = "//p[@class='predictextp'][1]//text()"
    PREDICT_INFO_2 = "//p[@class='predictextp'][2]//text()"
    PREDICT_INFO_3 = "//p[@class='predictextp'][3]//text()"
    PREDICT_INFO_4 = "//p[@class='predictextp'][4]//text()"


class BettingtipsTodaySpiderWithouNave(scrapy.Spider):
    # scrapy crawl bettingtips_today_without_nave_spider
    name = ConfigBettingtipsTodayWithouNave.SPIDER_NAME.value
    custom_settings = {
        "FEEDS": {
            ConfigBettingtipsTodayWithouNave.generate_filename(): {
                "format": ConfigBettingtipsToday.FILE_FORMAT.value,
                "encoding": ConfigBettingtipsToday.FILE_ENCODING.value,
                "overwrite": ConfigBettingtipsToday.FILE_OVERWRITE.value,
                "fields": SportsItem.fields.keys(),
            }
        },
        "LOG_LEVEL": "INFO",
    }

    start_urls = ConfigBettingtipsTodayWithouNave.START_URLS_WITHOUT_NAVE.value

    def parse(self, response):

        date_game = response.xpath(ConfigXpath.DATE.value).get()
        table_info = response.xpath(ConfigXpath.PIVOTE_TABLE.value)
        
        self.logger.info('URL: %s', response.url)
        
        if not table_info:
            self.logger.info('No hay partidos para la fecha: %s', date_game)
            return None
        
        for select_game in table_info:
            for game in select_game.xpath(ConfigXpath.PIVOTE_ROW.value)[1::]:
                data_main_table = {
                    "date_game": date_game,
                    "country_and_liga": select_game.xpath(ConfigXpath.COUNTRY_AND_LIGA.value).getall(),
                    "time_game": game.xpath(ConfigXpath.TIME.value).get(),
                    "game": "vs ".join(game.xpath(ConfigXpath.GAME.value).getall()),
                    "url_info_game": game.xpath(ConfigXpath.INFO.value).get(),
                }
                if data_main_table['url_info_game'] is None:
                    continue

                yield scrapy.Request(
                    data_main_table['url_info_game'],
                    meta={"data_main_table": data_main_table},
                    callback=self.parse_game,
                    dont_filter=True,
                )

    def parse_game(self, response: Response):
        data_main_table = response.meta.get('data_main_table')
        output_item = SportsItem()
        output_item['fecha_de_juego'] = change_date_format(data_main_table['date_game'], "%d/%B/%Y")
        output_item['pais_y_liga'] = data_main_table['country_and_liga']
        output_item['hora_de_juego'] = data_main_table['time_game']
        output_item['juego_entre'] = data_main_table['game']
        output_item['prediccion'] = response.xpath(ConfigXpath.PREDICT_INFO_1.value).getall()
        output_item['resultados'] = response.xpath(ConfigXpath.PREDICT_INFO_2.value).getall()
        output_item['analisis'] = response.xpath(ConfigXpath.PREDICT_INFO_3.value).getall()
        output_item['anotacion'] = response.xpath(ConfigXpath.PREDICT_INFO_4.value).getall()
        output_item['url'] = response.url
        
        for key, value in output_item.items():
            output_item[key] = clean_list_data(value)
        yield output_item
