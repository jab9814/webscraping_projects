import scrapy


class SportsItem(scrapy.Item):
    fecha_de_juego = scrapy.Field()
    pais_y_liga = scrapy.Field()
    hora_de_juego = scrapy.Field()
    juego_entre = scrapy.Field()
    prediccion = scrapy.Field()
    resultados = scrapy.Field()
    analisis = scrapy.Field()
    anotacion = scrapy.Field()
    url = scrapy.Field()
