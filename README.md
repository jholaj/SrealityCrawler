# Sreality Crawler

## Introduction
This project is a web scraping tool designed to extract data from the Sreality real estate website. It provides functionalities to scrape property listings and store them in a database for further analysis.

## Components
- **Scrapy Spiders:** Contains spider responsible for scraping data from the Sreality website and initialization of PostgreSQL table.
- **Database:** Dockerized PostgreSQL database.
- **Web Server:** Flask web server for serving scraped data via a web interface.

## Usage
1. Clone the repository.
2. Navigate to the project directory.
3. Run `docker-compose up` to start the web server.
4. Navigate to `http://localhost:8080` in your web browser to access the web interface.

## Notes
- Scraping is made by querying the sreality API
    - `https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500`
