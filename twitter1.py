import credential
import twitter

consumer_key = credential.consumer_key
consumer_secret = credential.consumer_secret
access_token = credential.access_token
access_secret = credential.access_secret

auth = twitter.oauth.OAuth(access_token, access_secret, consumer_key, consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

print twitter_api
