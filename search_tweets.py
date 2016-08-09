import credential
import twitter
import json

consumer_key = credential.consumer_key
consumer_secret = credential.consumer_secret
access_token = credential.access_token
access_secret = credential.access_secret

auth = twitter.oauth.OAuth(access_token, access_secret, consumer_key, consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

q = "#Cruel"

count = 100

search_results = twitter_api.search.tweets(q=q, count=count)

statss = search_results['statuses']

for i in xrange(5):
    print "Length of status",len(statss)
    try:
        nxt = search_results['search_metadata']['next_results']
    except KeyError, e:
        break
    kwargs = dict([kv.split("=") for kv in nxt[1:].split("&")])
    search_results = twitter_api.search.tweets(**kwargs)
    statss = statss + search_results['statuses']
    print statss[0]
