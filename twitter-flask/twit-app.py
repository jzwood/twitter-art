#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.scss import Scss
import sqlite3
import searchTwitter as tw

app = Flask(__name__)
app.config['DEBUG'] = True
Scss(app, static_dir='static', asset_dir='assets')

@app.route('/')
@app.route('/<info>')
def index(info=None):

    # api = tw.authenticate()
    # results = tw.getJSONfromQuery('"you know that there are"',api,3)
    results = [{'timestamp': '2:31:23AM Tue Apr 5 2016', 'handle': '@DepEd_PH', 'text': 'Did you know that there are 21 sports (17 annual events &amp; 4 demonstration sports) in Palarong Pambansa? #Palaro2016 https://t.co/VshYsu1biZ'},
                {'timestamp': '7:37:02AM Fri Apr 1 2016', 'handle': '@DrRanj', 'text': "Did you know that there are over 175,000 #youngcarers (5-18yrs) in the UK? Join us on @itvthismorning today where we'll be meeting some!"}, {'timestamp': '11:25:34PM Fri Apr 8 2016', 'handle': '@sarahmerie17', 'text': 'You know that there are some people who would never do for you what you do for them.  And you do it anyways.'}]
    print(results)

    return render_template('index.html', data=results, info=info)


if __name__ == "__main__":
    app.run()
