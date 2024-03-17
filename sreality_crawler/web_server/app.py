from flask import Flask, render_template
import sys
import psycopg2

sys.path.insert(0, '../config')
import config

# Connection details
hostname = config.DB_CONFIG['hostname']
username = config.DB_CONFIG['username']
password = config.DB_CONFIG['password']
database = config.DB_CONFIG['database']
port = config.DB_CONFIG['port']

print(config.DB_CONFIG['hostname'])

connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
cursor = connection.cursor()

cursor.execute("SELECT * FROM estates")

# fetching results
estates = cursor.fetchall()

cursor.close()
connection.close()

app = Flask(__name__)

@app.route('/')
def index():
    estate_data = []
    for estate in estates:
        title = estate[1]  # extract title
        image_url = estate[2]  # extract image URL
        estate_data.append({'title': title, 'image_url': image_url})

    return render_template('index.html', estates=estate_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
