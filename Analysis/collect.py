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
from twython import Twython
import pprint as pp

#Variables that contains the user credentials to access Twitter API
#cred
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

twitter = Twython(consumer_key, consumer_secret)
auth = twitter.get_authentication_tokens()

for i in range(10000):
	status = twitter.show_status(id="112652479837110273")
	dump=json.dumps(status, ensure_ascii=False)
	db=pymongo.MongoClient(#ip).giving_tuesday
	db.unicef.insert(json.loads(dump))
