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

text_status = [status['text'] for status in statss]
words = [w for t in text_status for w in t.split()]
screen_name = [user_mention['screen_name'] for status in statss for user_mention in status['entities']['user_mentions']]
hashtags = [hashtag['text'] for status in statss for hashtag in status['entities']['hashtags']]

print lexical_diversity(words)
print lexical_diversity(screen_name)
print lexical_diversity(hashtags)
print average_words(text_status)
