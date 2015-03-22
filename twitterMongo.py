__author__ = 'moqri'
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
import sys
import pymongo

#Variables that contains the user credentials to access Twitter API
access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.db = pymongo.MongoClient().test

    def on_data(self, tweet):
        self.db.t2.insert(json.loads(tweet))
        decoded = json.loads(tweet)
        try:
            print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
            print ''
            return True
        except:
            return True

    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream


sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=['Ebola'])