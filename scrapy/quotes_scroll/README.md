# Proyecto Scrapy quotes scroll

✨📝 [Quotes](https://quotes.toscrape.com/scroll)  es el sitio web con citas populares de diferentes autores sobre diversos temas. ¿A quién no le gusta escuchar citas? A todos nos gusta escucharlas porque nos permiten conectar con sentimientos como el miedo, la tristeza, la motivación, la ciencia, el arte, entre otras...

𓇼 Mediante el uso del framework Scrapy en el siguiente proyecto, se realizara lo siguiente:

- Obtener información mediante Scrapy en una página con un scroll indefinido. Dicha pagina cuenta con una API con las citas y redirigir hacia otra página con sus correspondientes autores.
- La extracción de la citas que se encuentran en la pagina [Quotes](https://quotes.toscrape.com/scroll), como también la información de los autores desde la pagina [Good Reads](https://www.goodreads.com/), en un formato json
- Manipulación, limpieza y transformación del formato json mediante el uso de la librería [Pandas](https://pandas.pydata.org/) para obtener la información necesaria a un archivo csv para sus correspondientes análisis o carga de datos a una DB

## Indice

- [Proyecto Scrapy quotes scroll](#proyecto-scrapy-quotes-scroll)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Comando de ejecución de la araña](#comando-de-ejecucion-de-la-araña)
- [Ejemplo de la información extraída](#ejemplo-de-la-información-extraída)

## Estructura del proyecto

```bash
.
├── README.md
├── data                            # Se crea una vez ejecutada la arana
│   ├── quotes_scroll.json          # Se crea una vez se realiza la extracción
│   └── quotes_scroll_refine.csv    # Se crea una vez se realiza el refinado
├── quotes_scroll
│   ├── __init__.py
│   ├── data_refactory.py
│   ├── enum_models.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── quotes_scroll_spider.py
└── scrapy.cfg
```

## Modificaciones realizadas al proyecto Scrapy

En la siguiente lista se pueden observar los módulos a los cuales se les realizó modificaciones al proyecto creado con startproject

- [settings](quotes_scroll/settings.py):
    - Habilitar cantidad de reintentos y para ciertos códigos de respuesta HTTP
    - Tiempos de ejecución y peticiones a la pagina, con el fin de hacerlo dinámico y aleatorio, para evitar posibles bloqueos
- [items](quotes_scroll/items.py):
    - Agregados nuevos campos al model de extracción
- [enum_models](quotes_scroll/enum_models.py)
    - Configuracion del archivo formato json como del archivo csv
- [pipelines](quotes_scroll/pipelines.py)
    - Control de procesos desde el inicio de la araña hasta finalizar su extracción
    - Indicaciones al proceso cuando debe realizarse una extracción y/o refinar la data extraída.
    - Uso de la metodología Refactory para la manipulación, transformación y limpieza de los datos extraídos
- [data_refactory](quotes_scroll/data_refactory.py)
    - Metodología refactory para los procesos ETL de la data obtenida
- [quotes_scroll_spider](quotes_scroll/spiders/quotes_spider.py)
    - Mediante el método from_crawler de la clase principal de la araña, se utiliza para indicar cuando no es necesario crear o sobrescribir el archivo json de extracción

## Comando de ejecucion de la araña

🕷️ Para la ejecución de la araña es necesario contar con el entorno virtual activado (nota: revisar los [requirements](/scrapy/requirements.txt) necesarios).

Dentro del proyecto, se define un parámetro externo denominado **refine**. Dicho parámetro ronda en los siguientes valores:

```bash
refine = 0  # Extraccion de las citas y los autores en el formato json
refine = 1  # Refinado de las citas y los autores para la creacion del archivo csv
refine = 2  # Extraccion del archivo json y refinado para la creaccion del archivo csv
```

Para ejecutar la araña se tiene los siguientes comandos, según sea la conveniencia. Nota: Es necesario encontrarse dentro del proyecto [quotes_scroll](/scrapy/quotes_scroll/), para su correcta ejecución.

```bash
scrapy crawl quotes_scroll_spider -a refine = 0
scrapy crawl quotes_scroll_spider -a refine = 1
scrapy crawl quotes_scroll_spider -a refine = 2
```

Por defecto el parámetro refine es igual a 2; por lo que, se puede también ejecutar el comando:

```bash
scrapy crawl quotes_scroll_spider
```

Una vez ejecutada la araña y finalizado el proceso de extracción y refinado, se creará una carpeta en la siguiente ruta [data](data/), donde contará con:

- Un archivo json con las citas extraídas e información del autor
- Un archivo csv con las citas e información del autor con su respectiva limpieza y transformación de datos

## Ejemplo de la información extraída

Desde la pagina se observa la extracción, en formato .json, la siguiente cita:

Información de la autora [Jane_Austen](https://www.goodreads.com/author/show/1265.Jane_Austen)

``` json
{
    "quotes_author_name": "Jane Austen",
    "quotes_author_slug": "Jane-Austen",
    "quotes_author_goodreads_link": "https://www.goodreads.com/author/show/1265.Jane_Austen",
    "quotes_tags": [
        "elizabeth-bennet",
        "jane-austen"
    ],
    "quotes_text": "“There are few people whom I really love, and still fewer of whom I think well. The more I see of the world, the more am I dissatisfied with it; and every day confirms my belief of the inconsistency of all human characters, and of the little dependence that can be placed on the appearance of merit or sense.”",
    "goodreads_name": "Jane Austen",
    "goodreads_born_date": "December 16, 1775",
    "goodreads_death_date": "July 18, 1817",
    "goodreads_born_location": "in Steventon Rectory, Hampshire, England",
    "goodreads_description": "Jane Austen was an English novelist known primarily for her six novels, which implicitly interpret, critique, and comment upon the English landed gentry at the end of the 18th century... "
},
...
```
