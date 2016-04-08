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
    results = [{'timestamp': '7:36:58PM Fri Apr 8 2016', 'text': "@JTerry_03 @CarlyMaiani same -- do it. It changes you in a million ways staying put won't.", 'handle': '@amandarporter'},
                {'timestamp': '7:19:48PM Fri Apr 8 2016', 'text': 'So true &lt;3  "There is no way to be a perfect mother...but a million ways to be a good one." #JillChurchill https://t.co/AewRiFPyFD', 'handle': '@JacquelineRic1'},
                {'timestamp': '7:18:53PM Fri Apr 8 2016', 'text': '@JustKamia lmao we think of. a million ways to get out tuition paid 😭😂', 'handle': '@CheckEmLikeNike'}]
    print(results)

    return render_template('index.html', data=results, info=info)


if __name__ == "__main__":
    app.run()
