__author__ = 'moqri'
#Import the necessary methods from tweepy library
#from tweepy.streaming import StreamListener
#from tweepy import OAuthHandler
#from tweepy import Stream
#import tweepy
import json
import sys
import pymongo
from datetime import datetime
import time
from twython import Twython
import pprint as pp

#Variables that contains the user credentials to access Twitter API
#credentials
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth)

twitter = Twython(consumer_key, consumer_secret)
auth = twitter.get_authentication_tokens()
f = open('unicef.txt')
c=0
for line in f:
	c+=1
	if c % 180<>0:	
		id=line.split('|')
		print id[0]
		status = twitter.show_status(id=id[0])
		dump=json.dumps(status, ensure_ascii=False)
		db=pymongo.MongoClient().tweet_meter
		db.unicef.insert(json.loads(dump))
	else:
		time.sleep(15*60+1)
		twitter = Twython(consumer_key, consumer_secret)
raw_input("Press Enter to continue...")