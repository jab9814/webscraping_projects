# 🕷️ Web Scraping Project with Scrapy

Este proyecto está diseñado para extraer información relevante desde múltiples fuentes web utilizando el framework [Scrapy](https://scrapy.org/). La información recopilada se guarda en un archivo estructurado en formato **CSV** para su posterior análisis.

---

## 🌐 URLs de origen

La araña recolecta datos desde los siguientes sitios web:

- https://www.bettingtips.today

---

## 📁 Estructura de salida

Los datos extraídos se exportan a un archivo `.csv` ubicado en la carpeta `output/`.  
Este archivo incluye las columnas definidas en el archivo `items.py` del proyecto y sobrescribe la versión anterior cada vez que se ejecuta la araña, garantizando que siempre contenga datos actualizados.

---

## ▶️ ¿Cómo ejecutar la araña?

Desde la raíz del proyecto, ejecuta el siguiente comando en la terminal:

```bash
scrapy crawl bettingtips_today_with_nave_spider && scrapy crawl bettingtips_today_without_nave_spider


