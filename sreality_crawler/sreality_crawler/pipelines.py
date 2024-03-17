# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import sys

sys.path.insert(0, '../config')
import config

class PostgreSQLPipeline:
    def __init__(self):
        # Connection Details
        hostname = config.DB_CONFIG['hostname']
        username = config.DB_CONFIG['username']
        password = config.DB_CONFIG['password']
        database = config.DB_CONFIG['database']
        port = config.DB_CONFIG['port']

        # connecting to db...
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        self.cursor = self.connection.cursor()
        
        # delete old data if exists
        self.cursor.execute("DROP TABLE IF EXISTS estates")
        # create estates table if none exists
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS estates(
            id serial PRIMARY KEY, 
            title text,
            image_url text
        )
        """)
        self.connection.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        query = "INSERT INTO estates (title, image_url) VALUES (%s, %s)"
        self.cursor.execute(query, (item['title'], item['image_url']))
        self.connection.commit()
        return item
