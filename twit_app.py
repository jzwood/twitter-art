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

    mode = []
    mode += tw.lyric_logic(api, '"sing out"', [8,8.6],'01')
    mode += tw.lyric_logic(api, '"be free"', [12,12.6],'01')
    mode += tw.lyric_logic(api, '"live high"', [23,23.6],'01')
    mode += tw.lyric_logic(api, '"live low"', [27,27.6],'01')
    mode += tw.lyric_logic(api, '"you know that there are"', [32],'0')
    mode += tw.lyric_logic(api, '"what you want"', [37],'0')
    mode += tw.lyric_logic(api, '"the opportunity"', [45],'1')
    mode += tw.lyric_logic(api, '"you can do it"', [48],'0')
    mode += tw.lyric_logic(api, '"ah ah"', [60,64],'01')
    # mode = [{'li': 0, 'lyrics': '"sing out"', 'tweet': {'handle': 'AmandaCerny', 'text': "I sing out of tune and it's just lovely☺️", 'timestamp': '2:58:52AM Tue Apr 5 2016'}, 'time': 8}, {'li': 1, 'lyrics': '"sing out"', 'tweet': {'handle': 'leakedcelebs777', 'text': 'Therefore, dear Sir, love your solitude and try to sing out with the pain it causes you. For those who are near you are far away... and this', 'timestamp': '5:59:33PM Tue Apr 12 2016'}, 'time': 8.6}, {'li': 0, 'lyrics': '"be free"', 'tweet': {'handle': 'JoyceMeyer', 'text': "In today's article, Joyce talks about how to be free from negative thinking. You can overcome it through God's help! https://t.co/m6KHGLcFWZ", 'timestamp': '11:01:55AM Tue Apr 12 2016'}, 'time': 12}, {'li': 1, 'lyrics': '"be free"', 'tweet': {'handle': 'travismills', 'text': 'VIP m&amp;g will be free for first 100 ppl in line on this tour  https://t.co/IMcPPwUugc', 'timestamp': '11:27:04PM Mon Apr 11 2016'}, 'time': 12.6}, {'li': 0, 'lyrics': '"live high"', 'tweet': {'handle': 'live_high_', 'text': 'How many more days till we can leave to hell hole??', 'timestamp': '5:58:29PM Tue Apr 12 2016'}, 'time': 23}, {'li': 1, 'lyrics': '"live high"', 'tweet': {'handle': 'live_high_', 'text': 'RT @TumbIrsPosts: *gets hit by a car* \n\nPasserby: "ARE YOU OKAY?"\n\nMe: "Please... I need my... phone"\n\n*opens Twitter*\n\nMe: "LMFAOOOOOOO YA…', 'timestamp': '5:54:28PM Tue Apr 12 2016'}, 'time': 23.6}, {'li': 0, 'lyrics': '"live low"', 'tweet': {'handle': 'geneiuspower', 'text': "/ you can't die with nothing i live low /\n.  . .", 'timestamp': '2:50:46PM Tue Apr 12 2016'}, 'time': 27}, {'li': 1, 'lyrics': '"live low"', 'tweet': {'handle': 'stressfm', 'text': '🎶 Cartografias Sonoras #7: Pedro Augusto (Ghuna X, Live Low) Playlist: 01 - Deathprod - Dead People´s... https://t.co/TsQfERL5Is', 'timestamp': '12:15:31PM Tue Apr 12 2016'}, 'time': 27.6}, {'li': 0, 'lyrics': '"you know that there are"', 'tweet': {'handle': 'DeptofDefense', 'text': 'Did you know that there are 1.82 million #MilKids?? #KidsServeToo #PurpleUp Learn More: https://t.co/4gVb9j7d9v https://t.co/6R0bFj54zo', 'timestamp': '12:01:40PM Tue Apr 12 2016'}, 'time': 32}]

    print(mode)

    now = datetime.datetime.now().strftime("%I:%M%p")
    intro = {
        "handle":"https://twitter.com/14CodeMonkeys",
        "now":now,
        "msg1":'Experience the wisdom of Cat Stevens through live tweets.'
        }
    header="If you want to..."
    foot="a simple web app brought to you by jake"

    return render_template('index.html', data=mode, safeData=json.dumps(mode),
    intro=intro, header=header, foot=foot, info=info)

if __name__ == "__main__":
    app.run()
