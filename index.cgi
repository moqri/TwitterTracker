#!C:\Python27\python.exe -u
#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import pymongo
import time
from pymongo import MongoClient
client = MongoClient()
db = client.test
collection = db.t2


print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers	
print "<H1>Last 20 Tweets:</H1>"
def do_something():
	for tweet in collection.find({},{"text":1}).limit(1).sort("$natural",-1):
		print "<H4>"
		print unicode(tweet['text']).encode('ascii', 'xmlcharrefreplace')
		print "</H4>"
	time.sleep(1)
while True:
    do_something()		