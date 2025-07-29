# Web Scraping Projects with Scrapy

🕷️ En la siguiente carpeta se encuentran proyectos donde se extrae información utilizando el Framework [Scrapy](https://scrapy.org/).

# Indice

- [Web Scraping Projects with Scrapy](#web-scraping-projects-with-scrapy)
- [Objetivo](#objetivo)
- [Estructura de la carpeta scrapy](#estructura-de-la-carpeta-scrapy)
- [Configuración](#configuración)
- [Ejemplos de proyectos incluidos](#ejemplos-de-proyectos-incluidos)

## Objetivo

- Utilizar Scrapy desde una simple araña hasta la creación de un proyecto para el uso que nos ofrece Scrapy.

- Capacidad de trabajar de forma asíncrona en la extracción de data.

- Diferentes modelos de paginas para la extracción de la información según sea el caso (html, API, xmls, ...)

## Estructura de la carpeta scrapy

```bash
.
├── books_spider.py
├── quotes/
├── quotes_scroll/
└── README.md
```

📁 Seleccione las siguientes rutas para ser redirigido hacia ellas:

- [README](README.md)
- [books_spider](books_spider.py)
- [quotes](quotes)
- [quotes con scroll indefinido](quotes_scroll)

## Configuración

🔧 Creación y activacion del entorno virtual

```bash
# Ejemplo para el framework Scrapy. Creacion y activacion del entorno virtual
python -m venv venv
source venv/bin/activate

# Instalacion de paquetes en el entorno virtual
pip install -r requirements.txt     
```

## Ejemplos de proyectos incluidos

- [books to scrapy](#books-to-scrape). Script .py
- [quotes](#quotes). Proyecto scrapy con modificaciones en los módulos.
- [quotes with scroll](#quotes-with-scroll) Proyecto scrapy con modificaciones en los módulos y enviar parámetros via consola

##  [books to scrape](https://books.toscrape.com/)

- 📚 [books_spider](books_spider.py)

Página con información de diferentes tipos de libros.

Para este caso se hará uso de una araña y no un proyecto Scrapy, con el fin de mostrar como es un script simple utilizando dicho framework.

Para la ejecución de la araña simplemente se debe ejecutar el siguiente comando *(nota: Recordar tener activo el entorno virtual)*

```bash
python books_spider.py
```

Con ello se crea una carpeta **data** donde se guarda la información extraida en formato .json

Se puede observar un ejemplo del libro [A Light in the Attic](https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html):

```json
{
    "PAGE_IMAGE": "https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg",
    "PAGE_TITLE": "A Light in the ...",
    "PAGE_URL_INFO": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "PAGE_PRICE": "£51.77",
    "PAGE_STATUS": "In stock",
    "BOOK_NAME": "A Light in the Attic",
    "BOOK_PRICE": "£51.77",
    "BOOK_STATUS_AND_COUNT": "In stock (22 available)",
    "BOOK_IMAGE": "https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg",
    "BOOK_DESCRIPTION": "It's hard to imagine a world without A Light in the Attic. This now-classic collection of ...",
    "BOOK_TAX": "£0.00"
},
```

## [quotes](https://quotes.toscrape.com/)

- 💭 [quotes](quotes/)

✨📝 [Quotes](https://quotes.toscrape.com/)  es el sitio web con citas populares de diferentes autores sobre diversos temas...

En esta ocasión utilizaremos el comando que nos ofrece scrapy: startproject, con el fin de extraer la información de la página pero mediante un proyecto estructurado con dicho framework.

Veremos los cambios que se realizaron a ciertos módulos del proyecto:

- Configuraciones en el setting.py
- Configuraciones en el pipelines.py
- Configuraciones de los campos a extraer mediante items.py
- Creación de modelos con Enum, enum_models.py
- Como se puede iniciar una sesión en la página y la extracción de la información, quotes_spider.py

Toda la información necesaria se encuentra en el siguiente enlace: [quotes](quotes/)

## [quotes with scroll](https://quotes.toscrape.com/scroll)

- 💭 [quotes with scroll](quotes_scroll/)

Aunque la pagina sigue siendo similar a [quotes](#quotes), en esta ocasión difiere en que las demás citas, solo se pueden observar si se realiza un scroll a la página.
Ademas, la API contiene la pagina [goodreads](https://www.goodreads.com/) que nos ofrece informacion sobre el autor de la cita.

Veremos los cambios que se realizaron a ciertos módulos del proyecto, pero manteniendo los cambios del proyecto [quotes](#quotes), con ciertas variaciones

- Manipulación de una API ofrecida por la página
- Agregar posibles reintentos de peticiones a la pagina o API, mediante el modulo settings.py
- El archivo salida será directamente un csv
- Configuraciones en el pipelines.py con el fin de manipular el csv después de su extracción
- Parámetros de entrada a la araña con el fin de indicar si_
    - Si solo se desea realizar la extracción de la información.
    - Si desea realizar el refinado de la información extraída.
    - Realizar ambas

Toda la información necesaria se encuentra en el siguiente enlace: [quotes with scroll](quotes_scroll/)
