import credential
import twitter
import json
from collections import Counter
from prettytable import PrettyTable

def lexical_diversity(tokens):
    return 1.0*len(set(tokens))/len(tokens)

def average_words(statss):
    total_word = sum([len(s.split()) for s in statss])
    return 1.0*total_word/len(statss)

consumer_key = credential.consumer_key
consumer_secret = credential.consumer_secret
access_token = credential.access_token
access_secret = credential.access_secret

auth = twitter.oauth.OAuth(access_token, access_secret, consumer_key, consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

q = "#1DayToRustom"

count = 100

search_results = twitter_api.search.tweets(q=q, count=count)

statss = search_results['statuses']

for i in xrange(5):
    try:
        nxt = search_results['search_metadata']['next_results']
    except KeyError, e:
        break
    kwargs = dict([kv.split("=") for kv in nxt[1:].split("&")])
    search_results = twitter_api.search.tweets(**kwargs)
    statss = statss + search_results['statuses']

rt = list(set([
    (status['retweet_count'], status['retweeted_status']['user']['screen_name'], status['text'])
    for status in statss
        if(status.has_key('retweeted_status'))
    ]))

pt = PrettyTable(field_names=['Count', 'Screen Names', 'Text'])
[pt.add_row(row) for row in sorted(rt, reverse=True)[:5]]
pt.max_width['Text'] = 50
print pt
