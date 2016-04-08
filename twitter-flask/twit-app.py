#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.scss import Scss
import sqlite3
import searchTwitter as tw

app = Flask(__name__)
app.config['DEBUG'] = True
Scss(app, static_dir='static', asset_dir='assets')

@app.route('/')
def index():
    # conn = sqlite3.connect('test_database.db')
    # c = conn.cursor()
    #
    # data_stream = c.execute('''SELECT * FROM records''')
    #
    # x    = []
    # down = []
    # up   = []
    # data = []
    #
    # for d in data_stream:
    #     x.append(d[0])
    #     down.append(d[1])
    #     up.append(d[2])
    #     data.append([format_datetime(d[0]), d[1], d[2]])
    api = tw.authenticate()
    results = tw.getJSONfromQuery('"you know that there are"',api,3)
    # results = [{'text': 'Citizens should be free to speak without having to consult the @Tx_Ethics Comm or an election lawyer or file mind-boggling forms.', 'timestamp': '7:11:22PM Fri Apr 8 2016', 'handle': '@TweetTonyMac'},
    #            {'text': "RT @PondsPH: Visit https://t.co/cfq3E29rrz to get your FREE beauty gift. Be one of the Philippines' most beautiful faces, with Pond's. @hel…", 'timestamp': '7:11:20PM Fri Apr 8 2016', 'handle': '@xilcabels'}]
    print(results)

    return render_template('index.html', data=results)

@app.route('/home/')
@app.route('/home/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run()
