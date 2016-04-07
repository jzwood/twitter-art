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

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '701456120825536512-VjgPUhj4U67XsOlnMruognOasLkBvyj'
ACCESS_SECRET = 'uLF7wBCOrwVmtqzIbwzjKWoUCNjPsYhuRGGAJveAcicHq'
CONSUMER_KEY = 'KGiy3gzu9J70N8gFiNDTCHWMN'
CONSUMER_SECRET = 'PBK83DQDEKdjqiiohfyIucaSL4mz2WIHxVxkcfruEOOwgXveXg'

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# r = api.request('search/tweets', {'q':'list:NASA/astronauts-in-space-now', 'lang':'en', 'count':3, 'result_type': 'recent'})
r = api.request('search/tweets', {'q':'"sing out"', 'lang':'en', 'count':2, 'result_type': 'recent'})

items = [a for a in r]

handle = lambda i: '@' + items[int(i)]['user']['screen_name']
timestamp = lambda i: cleanDateString(items[int(i)]['created_at'])
text = lambda i: items[int(i)]['text']
