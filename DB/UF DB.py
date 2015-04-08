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
while True:
	try:
		sapi.filter(track=['#UF ','#GatorNation','#Gators','#GatorFamily','#GatorGang','#GatorFootball','#ItsGreatUF','#tourUF','#GoGators','#ChompChomp','#FloridaGator',	
		'@Gator','@Univ of Florida','@UF','@GatorZone','@GatorZoneNews','@GatorZoneFB','@GatorZoneBB','@GatorZoneMBK','@ufalumni','@TheAlligator','@accentspeakers'	
		'university of florida','Univ of Florida'])
	except:
		print 'mahdimoqri02'
		
	
				   