import re
import scrapy
from enum import Enum
from scrapy.http.response import Response

from ..items import SportsItem
from ..comuns import change_date_format, clean_list_data
from ..enums_sports.enums_bettingtips_today import (
    ConfigBettingtipsToday, 
    ConfigBettingtipsTodayWithNave,
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


class BettingtipsTodaySpiderWithNave(scrapy.Spider):
    # scrapy crawl bettingtips_today_with_nave_spider
    name = ConfigBettingtipsTodayWithNave.SPIDER_NAME.value
    custom_settings = {
        "FEEDS": {
            ConfigBettingtipsTodayWithNave.generate_filename(): {
                "format": ConfigBettingtipsToday.FILE_FORMAT.value,
                "encoding": ConfigBettingtipsToday.FILE_ENCODING.value,
                "overwrite": ConfigBettingtipsToday.FILE_OVERWRITE.value,
                "fields": SportsItem.fields.keys(),
            }
        },
        "LOG_LEVEL": "INFO",
    }

    start_urls = ConfigBettingtipsTodayWithNave.START_URLS_WITH_NAVE.value

    def parse(self, response: Response):
        date_game = response.xpath(ConfigXpath.DATE.value).get()
        table_info = response.xpath(ConfigXpath.PIVOTE_TABLE.value)
        
        self.logger.info('URL: %s', response.url)

        if not table_info:
            self.logger.info('No hay partidos para la fecha: %s', date_game)
            return None
        
        aux_model = ''
        for modelo in ConfigBettingtipsToday.MODEL_TITLES.value:
            if re.search(modelo, response.url):
                aux_model = modelo
                break

        for select_game in table_info:
            for game in select_game.xpath(ConfigXpath.PIVOTE_ROW.value)[1::]:
                data_main_table = {
                    "date_game": date_game,
                    "country_and_liga": select_game.xpath(ConfigXpath.COUNTRY_AND_LIGA.value).getall(),
                    "time_game": game.xpath(ConfigXpath.TIME.value).get(),
                    "game": "vs ".join(game.xpath(ConfigXpath.GAME.value).getall()),
                    "results": f"'{(game.xpath(ConfigXpath.INFO_NAV_MENU.value).get())}'",
                }
                
                if data_main_table['country_and_liga'] == [] or data_main_table['game'] == '':
                    continue

                for key, value in data_main_table.items():
                    data_main_table[key] = clean_list_data(value)

                output_item = SportsItem()
                output_item['fecha_de_juego'] = change_date_format(data_main_table['date_game'], "%d/%B/%Y")
                output_item['pais_y_liga'] = data_main_table['country_and_liga']
                output_item['hora_de_juego'] = data_main_table['time_game']
                output_item['juego_entre'] = data_main_table['game']
                output_item['resultados'] = data_main_table['results']
                output_item['prediccion'] = aux_model
                
                yield output_item

