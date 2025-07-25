# 🕷️ Web Scraping Projects with Scrapy

En la siguiente carpeta se encuentran proyectos donde se extrae información utilizando el Framework [Scrapy](https://scrapy.org/).

## 🎯 Objetivo

- Utilizar Scrapy desde una simple araña hasta la creación de un proyecto para el uso que nos ofrece Scrapy.

- Capacidad de trabajar de forma asíncrona en la extracción de data.

- Diferentes modelos de paginas para la extracción de la información según sea el caso (html, API, xmls, ...)

## 📁 Estructura de la carpeta scrapy

```bash
.
├── project_a/
├── project_b/
├    ...
├── project_c/
├── books_spider.py
└── README.md
```

## 🔧 Configuración

Creación y activacion del entorno virtual

```bash
# Ejemplo para el framework Scrapy. Creacion y activacion del entorno virtual
python -m venv venv
source venv/bin/activate
```

# 🚀 Ejemplos de proyectos incluidos

## 📚 [books to scrape](https://books.toscrape.com/)

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

## 💭 [quotes](https://quotes.toscrape.com/)

En proceso… 🛠

<img src="https://user-images.githubusercontent.com/74038190/216122049-276bc7a5-c760-4849-805a-995d8fa6ea13.png" alt="Eleven O’Clock" width="120" />