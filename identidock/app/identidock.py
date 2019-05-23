#!/usr/local/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Php Strom Start 555!\n'

if __name__ == '__main__':
    app.run(port=9090,debug=True,use_reloader=True, host='0.0.0.0')
