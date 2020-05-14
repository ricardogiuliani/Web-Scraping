# Web-Scraping
Web scraping. Crawling weather data from Brazilian cities.

Data source: [Climatempo](https://www.climatempo.com.br)

## Overview
Scrapy is a fast high-level web crawling and web scraping framework, used to
crawl websites and extract structured data from their pages. It can be used for
a wide range of purposes, from data mining to monitoring and automated testing.

## Install
```
pip install scrapy
```

## Documentation

Documentation is available online at [https://docs.scrapy.org/](https://docs.scrapy.org/) and in the ``docs``
directory.

## Start new project

To start a new Scrapy project:

```
scrapy startproject project_name
```

## Run spider and generate CSV file

```
scrapy crawl spider_name -o file_name.csv
```

