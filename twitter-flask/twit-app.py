#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.scss import Scss
import json, datetime

# import sqlite3
#import searchTwitter as tw

app = Flask(__name__)
app.config['DEBUG'] = True
Scss(app, static_dir='static', asset_dir='assets')

@app.route('/')
@app.route('/<info>')
def index(info=None):

    #api = tw.authenticate()

    # mode = tw.lyric_logic(api, '"sing out"', [8,8.5],'01')
    mode = [{
        'li': 0,
        'tweet': {
            'text': "I sing out of tune and it's just lovely☺️",
            'timestamp': '2:58:52AM Tue Apr 5 2016',
            'handle': 'AmandaCerny'
        },
        'time': 5,
        'lyrics': '"sing out"'
    }, {
        'li': 1,
        'tweet': {
            'text': 'RT @Kalugendoj: New approaches and priority international investments have Malawi’s young farmers sing out… https://t.co/KFWP54CqS7 https:/…',
            'timestamp': '7:15:58PM Mon Apr 11 2016',
            'handle': 'mc_sarafina'
        },
        'time': 6,
        'lyrics': '"sing out"'
    }]

    #print(mode)

    now = datetime.datetime.now().strftime("%I:%M%p")
    intro = {"handle":"https://twitter.com/14CodeMonkeys","now":now, "msg1":
    'Experience the wisdom of Cat Stevens through live tweets.',"msg2":'filler text'}
    header="If you want to..."
    foot="Footer"

    return render_template('index.html', data=mode, safeData=json.dumps(mode),
    intro=intro, header=header, foot=foot, info=info)

if __name__ == "__main__":
    app.run()
