from TwitterAPI import TwitterAPI
#import datetime
from datetime import datetime
import re

# feed this 'created_at' dict value
def cleanDateString(datestring):
    clean_timestamp = datetime.strptime(datestring, '%a %b %d %H:%M:%S +0000 %Y')
    #convert to am/pm format for easy reading
    formatted_date =  ' ' + datetime.strftime(clean_timestamp,'%I:%M:%S%p %a %b %d %Y')
    formatted_date = re.sub(r' 0([0-9])|([0-9])0 ',r' \1',formatted_date).strip()
    return formatted_date

def authenticate():
    # Variables that contains the user credentials to access Twitter API
    ACCESS_TOKEN = '701456120825536512-VjgPUhj4U67XsOlnMruognOasLkBvyj'
    ACCESS_SECRET = 'uLF7wBCOrwVmtqzIbwzjKWoUCNjPsYhuRGGAJveAcicHq'
    CONSUMER_KEY = 'KGiy3gzu9J70N8gFiNDTCHWMN'
    CONSUMER_SECRET = 'PBK83DQDEKdjqiiohfyIucaSL4mz2WIHxVxkcfruEOOwgXveXg'
    #get twitter api obj
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    return api

#e.g. getJSONfromQuery('"sing out"', authenticate())
def getJSONfromQuery(q_str,api,resp_num):
    # r = api.request('search/tweets', {'q':'list:NASA/astronauts-in-space-now', 'lang':'en', 'count':3, 'result_type': 'recent'})
    r = api.request('search/tweets', {'q':q_str, 'lang':'en', 'count':resp_num, 'result_type': 'mixed'})
    #
    items = [a for a in r]
    #
    handle = lambda i: '@' + items[int(i)]['user']['screen_name']
    timestamp = lambda i: cleanDateString(items[int(i)]['created_at'])
    text = lambda i: items[int(i)]['text']
    #
    data = []
    #
    for i,entry in enumerate(items):
        ha,ti,tx = handle(i), timestamp(i), text(i)
        data.append({'handle':ha, 'timestamp':ti, "text": tx})
    #
    return data

#e.g. (api, '"sing out"', [8,8.5], '01'), # which_li is int, 0 = top, 1 = bottom
def lyric_logic(api,raw_lyrics,timing_array,which_li):
    results = getJSONfromQuery(raw_lyrics, api, len(timing_array))
    lyric_modules = []
    for i,time in enumerate(timing_array):
        lyric_modules.append({'lyrics':raw_lyrics, 'time':time, 'li':int(which_li[i]) ,'tweet':results[i]})
    return lyric_modules
