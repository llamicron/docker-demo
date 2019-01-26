from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Provides some data for the other container to get
    return 'Heres some data'

app.debug = True
app.run('0.0.0.0', port="80")
