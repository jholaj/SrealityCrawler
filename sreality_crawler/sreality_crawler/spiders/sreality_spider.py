import scrapy
import json
from sreality_crawler.items import SrealityItem

class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    # sreality api
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500']

    def parse(self, response):
        data = json.loads(response.body)
        # extracting data from json
        estates = data.get('_embedded', {}).get('estates', [])
        for estate in estates:
            title = estate.get('name', '')
            first_image_url = estate.get('_links', {}).get('images', [{}])[0].get('href', '')  # only first image
            yield SrealityItem(title=title, image_url=first_image_url)