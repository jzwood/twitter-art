#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.scss import Scss
import json, datetime

# import sqlite3
import searchTwitter as tw

app = Flask(__name__)
app.config['DEBUG'] = True
Scss(app, static_dir='static', asset_dir='assets')

@app.route('/')
@app.route('/<info>')
def index(info=None):

    api = tw.authenticate()
    #
    # mode = []
    # mode += tw.lyric_logic(api, '"sing out"', [8,8.6],'01')
    # mode += tw.lyric_logic(api, '"be free"', [12,12.6],'01')
    mode = [{
        'li': 0,
        'tweet': {
            'text': "I Sing out of tune and it's just lovely☺️",
            'timestamp': '2:58:52AM Tue Apr 5 2016',
            'handle': 'AmandaCerny'
        },
        'time': 8,
        'lyrics': '"sing out"'
    }, {
        'li': 1,
        'tweet': {
            'text': 'RT @Kalugendoj: New approaches and priority international investments have Malawi’s young farmers sing Out… https://t.co/KFWP54CqS7 https:/…',
            'timestamp': '7:15:58PM Mon Apr 11 2016',
            'handle': 'mc_sarafina'
        },
        'time': 8.6,
        'lyrics': '"sing out"'
    }]

    #print(mode)

    now = datetime.datetime.now().strftime("%I:%M%p")
    intro = {
        "handle":"https://twitter.com/14CodeMonkeys",
        "now":now,
        "msg1":'Experience the wisdom of Cat Stevens through live tweets.'
        }
    header="If you want to..."
    foot="Footer"

    return render_template('index.html', data=mode, safeData=json.dumps(mode),
    intro=intro, header=header, foot=foot, info=info)

if __name__ == "__main__":
    app.run()
