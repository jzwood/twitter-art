# Making art with Twitter #

This project was inspired by the brilliant work done by Wearebrightly: [Preflight Nerves](http://tweetflight.wearebrightly.com/). In summary, live-tweets mirroring the lyrics of a song overlay its music video, which is kinda sweet. I thought, I could do that, so I did in my own way.

Let's look at the technology necessary to make it possible:

- [Twitter API](https://github.com/geduldig/TwitterAPI)
	- Python backend queries tweets then feeds context to the page template.
- [Youtube API](https://developers.google.com/youtube/iframe_api_reference#Playback_controls)
	- detects video state (paused/time/etc) and syncs tweet animations with Youtube.
- [Greensock](http://greensock.com/)
	- Javascript timeouts and the Greensock library flexibly handle the tweet animations and timing. The animations honor both pausing and scrubbing. I probably could have used css animations but I initially experimented with more sophisticated animations that necessitated Greensock.


## How to use locally ##

### get from git ###
`git clone https://github.com/jzwood/twitter-art.git;cd twitter-art`

### install dependecies ###

- Install [Flask](http://flask.pocoo.org/docs/0.10/installation/)
  - `pip install Flask`
- Install [Flask Scss](http://pythonhosted.org/Flask-Scss/)
  - `pip install Flask-Scss`
- Install the [TwitterAPI](https://github.com/geduldig/TwitterAPI)
  - `pip install TwitterAPI`

### run ###
make sure you have python3
`python3 twit_app.py`

Navigate browswer to `http://127.0.0.1:5000/`
