import scrapy
from scrapy.http import Response
from quotes.items import QuotesItem
from quotes.enum_models import UserConfig, XpathConfig


class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes_spider"

    def start_requests(self):
        url = UserConfig.MAIN_URL.value
        return [scrapy.Request(url=url, callback=self._parse)]

    
    def _parse(self, response: Response):
        """ Ubicacion en la pagina principal """
        return scrapy.Request(
            url=UserConfig.LOGIN.value,
            callback=self._parse_login
        )


    def _parse_login(self, response: Response):
        """ Ubicacion en la etapa de iniciar sesion """

        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'csrf_token': response.xpath(UserConfig.TOKEN.value).get(),
                'username': UserConfig.NAME.value,
                'password': UserConfig.PASSWORD.value,
            },
            dont_filter=True,
            callback=self.parse_check_login,
        )
    
    def parse_check_login(self, response: Response):
        if response.status == 200:
            return scrapy.Request(
                url=UserConfig.MAIN_URL.value,
                callback=self._parse_all_quotes,
                dont_filter=True,
            )
        self.logger.warning('No se logro el login')
        return None
        

    def _parse_all_quotes(self, response: Response):
        """ Ubicarse en la pagina principal pero con una cuenta de usuario """

        all_quotes = response.xpath(XpathConfig.ALL_QUOTES.value)
        
        if not all_quotes:
            self.logger.warning('No se encuentra en la pagina la lista de "Citas"')
            return None

        for index, quote_response in enumerate(all_quotes):
            main_info_quote = {
                XpathConfig.QUOTE.name: quote_response.xpath(XpathConfig.QUOTE.value).get(),
                XpathConfig.QUOTE_BY.name: quote_response.xpath(XpathConfig.QUOTE_BY.value).get(),
                XpathConfig.TAGS.name: quote_response.xpath(XpathConfig.TAGS.value).getall(),
                XpathConfig.SOURCE_URL.name: quote_response.xpath(XpathConfig.SOURCE_URL.value).get(default=''),
            }

            item = QuotesItem()
            item['quote'] = main_info_quote.get(XpathConfig.QUOTE.name)
            item['quote_by'] = main_info_quote.get(XpathConfig.QUOTE_BY.name)
            item['tags'] = main_info_quote.get(XpathConfig.TAGS.name)
    
            if main_info_quote[XpathConfig.SOURCE_URL.name] is None:
                self.logger.warning(
                    '%s - La cita %s no cuenta con una url', 
                    index, main_info_quote[XpathConfig.QUOTE_BY.name]
                )
                yield item
                continue

            source_url = UserConfig.MAIN_URL.value + main_info_quote[XpathConfig.SOURCE_URL.name]
            yield scrapy.Request(
                source_url,
                callback=self._parse_quote,
                dont_filter=True,
                meta={'info_quote': item},
            )

        next_page = response.xpath(XpathConfig.NEXT_PAGE.value).get()
        if next_page is None:
            return None
        next_page = UserConfig.MAIN_URL.value + next_page
        yield scrapy.Request(
            next_page,
            callback=self._parse_all_quotes,
            dont_filter=True
        )

    def _parse_quote(self, response: Response):
        
        info_quote = response.meta.get('info_quote')

        if response.status != 200:
            self.logger.warning('Problemas con la fuente: %s', response.url)
            yield info_quote
            return None

        page_info_quote = self._get_info_quote(response)
        info_quote['born'] = page_info_quote.get(XpathConfig.BORN.name)
        info_quote['location'] = page_info_quote.get(XpathConfig.LOCATION.name)
        info_quote['description'] = page_info_quote.get(XpathConfig.DESCRIPTION.name)
        info_quote['sourcel_url'] = response.url
        yield info_quote


    def _get_info_quote(self, response_page: Response) -> dict[str, str]:
        return {
            XpathConfig.BORN.name: response_page.xpath(XpathConfig.BORN.value).get(),
            XpathConfig.LOCATION.name: response_page.xpath(XpathConfig.LOCATION.value).get(),
            XpathConfig.DESCRIPTION.name: response_page.xpath(XpathConfig.DESCRIPTION.value).get(),
        }
    