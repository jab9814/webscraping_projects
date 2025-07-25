## 🔍 Proyectos de Web-Scraping 🌐

## 🕷️ Web Scraping Projects with Python

Bienvenido a este repositorio de proyectos de **Web Scraping con Python**, utilizando tres de las herramientas más potentes en el ecosistema Python:

- [Scrapy](https://scrapy.org/)
- [Selenium](https://www.selenium.dev/)
- [Playwright](https://playwright.dev/python/)

---

## 🎯 Objetivo

El objetivo de este repositorio es proporcionar una colección de **proyectos prácticos** que simulan desafíos reales de web scraping. Aquí encontrarás ejemplos que exploran:

- Páginas con contenido estático (HTML puro)
- Sitios web dinámicos (JavaScript renderizado en cliente)
- Interacciones complejas como login, scroll infinito o paginación AJAX
- Comparativas entre scraping directo vs APIs públicas
- Buenas prácticas para scraping ético y eficiente

---

## ⚙️ Frameworks utilizados

| Framework   | Uso principal                                                  | Nivel de complejidad |
|-------------|----------------------------------------------------------------|-----------------------|
| `Scrapy`    | Scraping estructurado de HTML estático, crawlers y pipelines   | ⭐⭐                    |
| `Selenium`  | Navegación simulada, manejo de formularios, JS básico          | ⭐⭐⭐                   |
| `Playwright`| Automatización moderna, scraping de páginas altamente dinámicas| ⭐⭐⭐⭐                  |

Cada carpeta del repositorio contiene un proyecto que aprovecha uno o varios frameworks dependiendo de la complejidad del sitio.

---

## 📁 Estructura del repositorio

```bash
.
├── scrapy/         # Proyectos Scrapy con spiders básicos e intermedios
├── selenium/       # Scripts Selenium para scraping dinámico interactivo
├── playwright/     # Scrapers Playwright para sitios JS-heavy
├── apis/           # Ejemplos de uso de APIs públicas y comparación con scraping manual
├── notebooks/      # Exploración y análisis de datos con Python
└── docs/           # Documentación adicional, referencias y buenas prácticas
```

## 🚀 Ejemplos de proyectos incluidos

- 📚 books.toscrape.com: Scraping básico de libros con Scrapy

- 🏠 sitios inmobiliarios: Extraer datos de listados de propiedades con Playwright

- 🛍️ precios de productos: Monitoreo de precios con Selenium

- 📊 twitter/reddit: Extracción de contenido público (JS dinámico)

- 🆚 Comparativa entre scraping vs API pública (JSONPlaceholder)

## ✅ Requisitos

- Python 3.9+

- Navegador Chromium (para Playwright/Selenium)

- Entorno virtual recomendado

## 🔧 Configuración

Cada una de las carpetas scraping cuentan con un archivo **requiremnts.txt**. Es necesario crear un entono virtual e instalar las dependencias para utilizar los frameworks para su debida ejecución.

Para la creacion y activacion de los entornos virtuales, es necesario encontrarse a nivel del archivo README.md, y ejecutar los siguientes comandos como ejemplo:

```bash
# Ejemplo para el framework Scrapy. Creacion y activacion del entorno virtual
cd scrapy
python -m venv venv
source venv/bin/activate
```

```bash
# Ejemplo para el framework Selenium. Creacion y activacion del entorno virtual
cd selenium
python -m venv venv
source venv/bin/activate
```

```bash
# Ejemplo para el framework Playwright. Creacion y activacion del entorno virtual
cd playwright
python -m venv venv
source venv/bin/activate
```

Cada carpeta cuenta con un archivo README.md donde indica como ejecutar cada uno de los proyectos asocidados a la carpeta.

## 🖥️ Autor
Desarrollado y mantenido por: jab9814
🔗 GitHub: @jab9814
