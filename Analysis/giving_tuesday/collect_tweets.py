__author__ = 'moqri'
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
import sys
import pymongo
from datetime import datetime
import time

#Variables that contains the user credentials to access Twitter API
#credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.db = pymongo.MongoClient().giving_tuesday
    def on_data(self, tweet):
        print 'data'
        self.db.tweets.insert(json.loads(tweet))
        decoded = json.loads(tweet)
        created_at = decoded['created_at'].encode('ascii', 'ignore')
        screen_name=decoded['user']['screen_name'].encode('ascii', 'ignore')
        text=decoded['text'].encode('ascii', 'ignore')
        dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
        self.db.tweets_clean.insert({'screen_name':screen_name,'text':text,'created_at':dt})
        try:
            tweet_string= '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
            print tweet_string
            today= time.strftime("%d_%m_%Y")
            with open(today+'.json','a') as tf:
			    tf.write(tweet_string+"\n")
            return True
        except:
            return True

    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream


sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
while True:
	print 'yay'
	try:
		sapi.filter(track=['#givingtuesday','#blackfriday','#cybermonday'])
	except:
		print 'exception2'
		
	
				   