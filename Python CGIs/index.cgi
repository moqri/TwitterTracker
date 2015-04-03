#!C:\Python27\python.exe -u
#!/usr/bin/env python

__author__ = 'moqri'

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.test
collection = db.t2
countT=-1

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<H1>Last 20 Tweets:</H1>"

print ('<script>window.setInterval("reloadIFrame();", 2000);function reloadIFrame() { document.getElementById("myIframe").src="read.cgi";}</script>')
print ('<iframe src="read.cgi" id= myIframe width="400" height="400"</iframe>')

