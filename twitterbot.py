# -*- coding: utf-8 -*-

# 1 - Create variables for key, secret, token. These codes are obtained by creating a Twitter app at 
#       https://apps.twitter.com/

# 2 - This website has tons of great quotes about libraries: 
#       https://ebookfriendly.com/best-quotes-about-libraries-librarians/

# 3 - This tutorial from Mary Dickson Diaz (@marythought) was particularly helpful in creating the bot 
#       http://marydickson.com/build-a-twitter-bot-with-python/

# The textfile for this bot is library_quotes.txt
# To run the program from the command line, type 'python twitterbot.py library_quotes.txt'

import tweepy, sys, time

from whs_credentials import *

argfile = str(sys.argv[1])

# Set up OAuth and integrate with API.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# read in tweets from .txt file
filename = open(argfile, 'r')
f=filename.readlines()
filename.close()

if __name__ == "__main__":
	
	while True:
		with open(argfile) as f:
			lines = f.readlines()
			rand_line_num = randint(0,len(lines)-1)
			line = lines[rand_line_num]
            
		print("NOW TWEETING: " + line.strip())
		api.update_status(line.strip())
		time.sleep(36000) # tweet every hour
