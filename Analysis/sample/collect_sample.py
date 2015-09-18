__author__ = 'moqri'
#Import the necessary methods from tweepy library
import json
import sys
import pymongo
from datetime import datetime
import time
from twython import TwythonStreamer
import pprint as pp

#Variables that contains the user credentials to access Twitter API
#credentials

#twitter = Twython(consumer_key, consumer_secret)
#auth = twitter.get_authentication_tokens()

class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			print data['text'].encode('utf-8')
			dump=json.dumps(data, ensure_ascii=False)
			db=pymongo.MongoClient().tweet_meter
			db.sample.insert(json.loads(dump))
	def on_error(self, status_code, data):
		print status_code
		print "on_error"

stream = MyStreamer(consumer_key, consumer_secret, access_token, access_token_secret)
while True:
	try:	
		stream.statuses.filter(languages=["en"],track=
		['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	except:
		continue