# Proyecto Scrapy quotes

✨📝 [Quotes](https://quotes.toscrape.com/)  es el sitio web con citas populares de diferentes autores sobre diversos temas. ¿A quién no le gusta escuchar citas? A todos nos gusta escucharlas porque nos permiten conectar con sentimientos como el miedo, la tristeza, la motivación, la ciencia, el arte, entre otras...

𓇼 Mediante el uso del framework Scrapy en el siguiente proyecto, se realiza la extracción de la página las citas de ciertos autores, obteniendo una salida en formato json para ser manipula su información de acuerdo a sus necesidades. 

## Indice

- [Proyecto Scrapy quotes](#proyecto-scrapy-quotes)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Comando de ejecución de la araña](#comando-de-ejecucion-de-la-araña)
- [Ejemplo de la información extraída](#ejemplo-de-la-información-extraída)

## Estructura del proyecto

🏗️ Al ser un proyecto Scrapy, cuenta con multiples módulos útiles para modificar ciertas acciones o procesos internos antes, durante y después del webscraping de la araña.

```bash
.
├── README.md
├── data                # La carpeta y el archivo se crean al ejecutar la arana
│   └── prueba.json     
├── quotes
│   ├── __init__.py
│   ├── enum_models.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── quotes_spider.py
└── scrapy.cfg
```

Además, es posible integrar nuevos módulos para mejorar la estructura del código, como lo es el [modulo enum_models.py](quotes/enum_models.py), el cual se pueden configurar constantes de forma general.

## Modificaciones realizadas al proyecto Scrapy

En la siguiente lista se pueden observar los módulos a los cuales se les realizó modificaciones al proyecto creado con startproject

- [settings](quotes/settings.py)
- [pipelines](quotes/pipelines.py)
- [items](quotes/items.py)
- [enum_models](quotes/enum_models.py)
- [quotes_spider](quotes/spiders/quotes_spider.py)

## Comando de ejecucion de la araña

🕷️ Para la ejeción de la araña es necesario contar con el entorno virtual activado (nota: revisar los [requirements](/scrapy/requirements.txt) necesarios), y ejecutar el siguiente comando desde el nivel del proyecto [quotes](/scrapy/quotes/)

```bash
scrapy crawl quotes_spider
```

Una vez ejecutada la araña y finalizado el proceso de extracción, se creará una carpeta en la siguiente ruta [data](data/), donde contará con un archivo json con las citas extraídas

## Ejemplo de la información extraída

Desde la pagina de se observa la extraccion en formato .json la siguiente cita:

- *[Cita de Steve Martin](http://quotes.toscrape.com/author/Steve-Martin/)*

```json
[
    {
        "quote": "“A day without sunshine is like, you know, night.”",
        "quote_by": "Steve Martin",
        "tags": [
            "humor",
            "obvious",
            "simile"
        ],
        "born": "August 14, 1945",
        "location": "in Waco, Texas, The United States",
        "description": "Stephen Glenn \"Steve\" Martin is an American actor, comedian, writer, playwright, producer, musician, and composer. He was raised in Southern California in a Baptist family, where his early influences were working at Disneyland and Knott's Berry Farm and working magic and comedy acts at these and other smaller venues in the area. His ascent to fame picked up when he became a writer for the Smothers Brothers Comedy Hour, and later became a frequent guest on the Tonight Show.In the 1970s, Martin performed his offbeat, absurdist comedy routines before packed houses on national tours. In the 1980s, having branched away from stand-up comedy, he became a successful actor, playwright, and juggler, and eventually earned Emmy, Grammy, and American Comedy awards.",
        "sourcel_url": "http://quotes.toscrape.com/author/Steve-Martin/"
    },
    ...
]
```
