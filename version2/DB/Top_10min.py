import threading
import time
from operator import itemgetter 
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.tweets
collection = db.allTweets

def get_most_retweeted():    
    threading.Timer(600, get_most_retweeted).start()  #run every 10 minutes
    month = time.strftime("%b")
    day=time.strftime("%a")
    dd=time.strftime("%d")
    today='^'+day+' '+ month+' '+dd
    all_tweets=[]
    for tweet in collection.find({'created_at': { '$regex':today},'retweeted_status':{ '$exists': 1 } },{"text":1,"created_at":1,"retweeted_status":1}).limit(10000).sort("$natural",-1):
        all_tweets.append((tweet['text'], tweet['created_at'],tweet['retweeted_status']['retweet_count']))
    all_tweets=sorted(all_tweets, key=itemgetter(2),reverse=True) #?
    print len(all_tweets)
    unique_tweets=[]
    unique_tweets_text=[]
    for tweet in all_tweets:
        if tweet[0] not in unique_tweets_text and  not "University of Central Florida" in tweet[0] and not "University of South Florida" in tweet[0] and not "Florida Atlantic University" in tweet[0]:
            unique_tweets_text.append(tweet[0])
            unique_tweets.append(tweet)
    tweets_and_counts=[]
    for unique_tweet in unique_tweets:
        count=0
        for tweet in all_tweets:
            if unique_tweet[0]==tweet[0]:
                count=count+1
        tweets_and_counts.append((unique_tweet[0],unique_tweet[1],unique_tweet[2],count))
    tweets_and_counts=sorted(tweets_and_counts, key=itemgetter(3),reverse=True)
    print len(tweets_and_counts) 
    for i in reversed(range(10)):
        tweet=tweets_and_counts[i]
        post={"text":tweet[0],"created_at":tweet[1],"retweet_count":tweet[2],"today_count":tweet[3]}
        posts = db.topTweets #new collection
        posts.insert(post)
        print tweet
        
get_most_retweeted()