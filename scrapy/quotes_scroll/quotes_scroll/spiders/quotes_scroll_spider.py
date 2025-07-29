import scrapy
from scrapy.http import Response
from quotes_scroll.items import QuotesScrollItem
from quotes_scroll.enum_models import ConfigPage, ConfigXpath


class QuotesScrollSpiderSpider(scrapy.Spider):
    name = "quotes_scroll_spider"
    start_urls = [ConfigPage.BASE_URL.value]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):

        # Para por consola con el fin de refinar cuando la data esta en local
        # Con el fin de no realizar el webscraping de nuevo
        refine = int(kwargs.get('refine', 2))
        if refine == 1:
            # Deshabilitar FEEDS completamente en modo refinado
            crawler.settings.set('FEEDS', {})
        
        # Crear spider normalmente
        spider = super().from_crawler(crawler, *args, **kwargs)
        spider.refine = refine
        return spider

    def parse(self, response: Response):
        """ Pagina principal """

        if self.refine == 1:
            self.logger.info('Ejecucion de proceso de refinado')
            return None

        if response.status != 200:
            self.logger.warning('No se logra acceder a la pagina: %s', [response.url])
            return None

        yield scrapy.Request(
            ConfigPage.INIT_API_URL.value,
            callback=self._parse_api_info,
            dont_filter=True,
        )        

    def _parse_api_info(self, response: Response):
        """ Obtener informacion desde la API ofrecida en quotes """
        
        if response.status != 200:
            self.logger.warning('No se logra obtener respuesta de la API: %s', [response.url])
            return None
        
        api_info: dict[str, bool | int | list[dict] | None] = response.json()

        if not api_info.get('quotes', None):
            self.logger.warning('No se logra obtener la informacion de las citas')
            return None

        # Recorrer todas las citas desde la api
        for quote in api_info.get('quotes', []):
            quote_info = self._get_quote_info(quote)
            if quote_info['quotes_author_goodreads_link'] == '':
                continue
            # Extraer informacion extra desde la pagina goodreads
            yield scrapy.Request(
                quote_info['quotes_author_goodreads_link'],
                meta={'quote_info': quote_info},
                callback=self._parse_author_info,
                dont_filter=True,
            )

        # Obtener la siguiente informacion del scroll desde la siguiente API
        if api_info.get('has_next', False) and api_info.get('page', None):
            next_page = f"{ConfigPage.API_BASE_URL.value}{api_info.get('page') + 1}"
            yield scrapy.Request(
                next_page,
                callback=self._parse_api_info,
                dont_filter=True,
            )

    def _parse_author_info(self, response: Response):
        """ Obtener informacion desde la pagina https://www.goodreads.com/ segun el autor de la cita """

        if response.status != 200:
            self.logger.warning('No se logra obtener respuesta desde la pagina: %s', [response.url])
            return None

        author_info: dict = self._get_author_info(response)
        quote_info: dict = response.meta.get('quote_info', {})
        quote_info.update(author_info)

        item = self._create_scrapy_item(quote_info)
        yield item

    def _get_quote_info(self, data: dict[str, dict[str, str] | list[str] | str]) -> dict:
        """ Obtener la informacion desde la api """
        return {
            'quotes_author_name': data.get('author', {}).get('name') or '',
            'quotes_author_slug': data.get('author', {}).get('slug') or '',
            'quotes_author_goodreads_link': self._get_goodreads_link(data.get('author', {}).get('goodreads_link') or ''),
            'quotes_tags': data.get('tags') or '',
            'quotes_text': data.get('text') or '',
        }

    def _get_goodreads_link(self, path_info: str) -> str:
        """ Generar la url para la pagina GOODREADS """
        return (
            f"{ConfigPage.BASE_URL_GOODREADS.value}{path_info}" 
            if path_info 
            else ''
        )
    
    def _get_author_info(self, response: Response) -> dict:
        """ Obtener la informacion desde la pagina goodreads"""
        return {
            'goodreads_name': response.xpath(ConfigXpath.GOODREADS_NAME.value).get() or '',
            'goodreads_born_date': response.xpath(ConfigXpath.GOODREADS_BORN_DATE.value).get() or '',
            'goodreads_death_date': response.xpath(ConfigXpath.GOODREADS_DEATH_DATE.value).get() or '',
            'goodreads_born_location': response.xpath(ConfigXpath.GOODREADS_BORN_LOCATION.value).get() or '',
            'goodreads_description': self._get_description(response.xpath(ConfigXpath.GOODREADS_DESCRIPTION.value).getall()),
        }
    
    def _get_description(self, all_text: list[str]) -> str:
        """ Obtener un unico texto para la descripcion"""
        if not all_text:
            return ''
        return "".join(all_text)

    def _create_scrapy_item(self, data: dict) -> QuotesScrollItem:
        """ Crear un item para el scrapy """
        return QuotesScrollItem(
            quotes_author_name=data.get('quotes_author_name', ''),
            quotes_author_slug=data.get('quotes_author_slug', ''),
            quotes_author_goodreads_link=data.get('quotes_author_goodreads_link', ''),
            quotes_tags=data.get('quotes_tags', ''),
            quotes_text=data.get('quotes_text', ''),
            goodreads_name=data.get('goodreads_name', ''),
            goodreads_born_date=data.get('goodreads_born_date', ''),
            goodreads_death_date=data.get('goodreads_death_date', ''),
            goodreads_born_location=data.get('goodreads_born_location', ''),
            goodreads_description=data.get('goodreads_description', ''),
        )