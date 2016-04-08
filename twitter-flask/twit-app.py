#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.scss import Scss
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True
Scss(app, static_dir='static', asset_dir='assets')

@app.route('/test')
def index():
    conn = sqlite3.connect('test_database.db')
    c = conn.cursor()

    data_stream = c.execute('''SELECT * FROM records''')

    x    = []
    down = []
    up   = []
    data = []

    for d in data_stream:
        x.append(d[0])
        down.append(d[1])
        up.append(d[2])
        data.append([format_datetime(d[0]), d[1], d[2]])

    return render_template('index.html', domain=x, down=down, up=up, data=data)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run()
