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
access_token = "3088029851-u03eZ1X6rTKcduGTWSNZnW9KOvqsUsAu3Pg9FxA"
access_token_secret = "IhsXQslEVPIyUQWfqPxeNxPp144B5DqQtCJl1dG2cNV99"
consumer_key = "DHepfM484PrDdknfDfACq0NaG"
consumer_secret = "wVEIt3j3TC9fuIkou9LEOucRwUyHbZAUZwM1du0jV2jJxLcDv4"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        
        #Refers to the specific database from mongodb
        self.db = pymongo.MongoClient().tweets


    #Adds every individual tweet to the collection specified
    def on_data(self, tweet):
        self.db.allTweets.insert(json.loads(tweet))
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

#Streaming API
sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))

#Searches for these key words
while True:
	try:
		sapi.filter(track=['#UF ','#GatorNation','#Gators','#GatorFamily','#GatorGang','#GatorFootball','#ItsGreatUF','#tourUF','#GoGators','#ChompChomp','#FloridaGator',	
		'@Gator','@Univ of Florida','@UF','@GatorZone','@GatorZoneNews','@GatorZoneFB','@GatorZoneBB','@GatorZoneMBK','@ufalumni','@TheAlligator','@accentspeakers'	
		'university of florida','Univ of Florida'])
	except:
		print 'mahdimoqri02'
		
	
				   