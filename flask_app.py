from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route('/')
def hello_world():
    return send_file('./figure.png', mimetype='image/png')