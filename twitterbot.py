import tweepy, sys, time

from credentials import *

argfile = str(sys.argv[1])

# Set up OAuth and integrate with API.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# read in tweets from .txt file
filename = open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f: 
    print("NOW TWEETING: " + line)
    api.update_status(line)
    time.sleep(300) # Tweet every 5 minutes when testing