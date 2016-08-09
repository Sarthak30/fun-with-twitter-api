import credential
import twitter
import json

consumer_key = credential.consumer_key
consumer_secret = credential.consumer_secret
access_token = credential.access_token
access_secret = credential.access_secret

auth = twitter.oauth.OAuth(access_token, access_secret, consumer_key, consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

#to find the location id use "http://zourbuth.com/tools/woeid//"
WORLD_ID = "1"
WOE_ID  = "23424848"    #India

trend_world = twitter_api.trends.place(_id  = WORLD_ID)
trend_india = twitter_api.trends.place(_id = WOE_ID)

trend_world_set = set([trend['name'] for trend in trend_world[0]['trends']])
trend_india_set = set([trend['name'] for trend in trend_india[0]['trends']])

trend_common = trend_world_set.intersection(trend_india_set)
print trend_common
