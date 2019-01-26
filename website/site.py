from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # This will get data from the data-service (a separate container) and return it
    # This is where the magic happens
    data = requests.get('http://data-service').text
    return data

app.debug = True
app.run('0.0.0.0', port=80)
