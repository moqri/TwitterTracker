import threading

def printit():
    threading.Timer(600, printit).start()
    from operator import itemgetter
    import pymongo
    import time
    from pymongo import MongoClient
    client = MongoClient('10.247.69.18:27017')
    db = client.test
    collection = db.t2
    countT=-1
    c=[]
    for tweet in collection.find({'created_at': { '$regex':'^Wed Apr 08'},'retweeted_status':{ '$exists': 1 } },{"text":1,"created_at":1,"retweeted_status":1}).limit(10000).sort("$natural",-1):
        t= (tweet['text'], tweet['created_at'],tweet['retweeted_status']['retweet_count'])
        c.append(t)
    c=sorted(c, key=itemgetter(2),reverse=True)
    print len(c)
    cn=[]
    ct=[]
    for t in c:
        if t[0] not in ct and  not "University of Central Florida" in t[0] and not "University of South Florida" in t[0] and not "Florida Atlantic University" in t[0]:
            ct.append(t[0])
            cn.append(t)
    cnn=[]
    for t2 in cn:
        count=0
        for t in c:
            if t[0]==t2[0]:
                count=count+1
        t2n=(t2[0],t2[1],t2[2],count)
        cnn.append(t2n)
    cnn=sorted(cnn, key=itemgetter(3),reverse=True)
    for t in cnn[:50]:
        post={"text":t[0],"created_at":t[1],"retweet_count":t[2],"today_count":t[3]}
        posts = db.top
        posts.insert(post)



printit()