#!C:\Python27\python.exe -u
#!/usr/bin/env python

__author__ = 'moqri'

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import pymongo
from pymongo import MongoClient
client = MongoClient('10.247.69.18')
db = client.test
collection = db.t2
countT=-1

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

for tweet in collection.find({},{"text":1}).limit(20).sort("$natural",-1):
	print "<H4 id='NewTweet'>"
	print unicode(tweet['text']).encode('ascii', 'xmlcharrefreplace')
	print "</H4>"

	print "</H4>"
