import credential
import twitter
import json
from collections import Counter
from prettytable import PrettyTable

consumer_key = credential.consumer_key
consumer_secret = credential.consumer_secret
access_token = credential.access_token
access_secret = credential.access_secret

auth = twitter.oauth.OAuth(access_token, access_secret, consumer_key, consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

q = "#DoYourShare"

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

for label, data in (('Words', words), ('Screen Names', screen_name), ('Hashtag', hashtags)):
    pt = PrettyTable(field_names = [label, 'Count'])
    c = Counter(data)
    [pt.add_row(kv) for kv in c.most_common()[:10]]
    # pt.align[label], pt.align('Count') = 'l', 'r'
    print pt
