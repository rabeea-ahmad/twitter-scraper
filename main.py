import tweepy
from tweepy import OAuthHandler
import time
import string
import config
import json
import ast

class Scrape:

	global process_or_store

	def read_timeline(self, api):
		print "Gathering tweets..."
		file = open('tweets.csv', 'a')
		for status in tweepy.Cursor(api.home_timeline).items(100):
			tweet = status.text
			tweet = tweet.encode('utf8')
			file.write('\n %s \n' % tweet)
		file.close() 

	def preprocess(self):
		vocabulary_size = 8000
		unknown_token = 'UNKNOWN_TOKEN'
		sentence_start_token = 'SENTENCE_START'
		sentence_end_token = 'SENTENCE_END'

		print "Reading input file..."
		with open('tweets.csv', 'rb') as f:
			reader = csv.reader(f, skipinitialspace=True)
			reader.next()

			

		



if __name__ == '__main__':
	scrape = Scrape()
	
	# Initialize settings 
	api_key = '<put key here>'
	api_secret = '<put secret here>'
	access_token = '<put access token here>'
	access_secret ='<put access secret here>'

	auth = OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth)

	# Scrape away babyy, watch out for rate limits tho :O
	scrape.read_timeline(api)

	# Clean the tweets
	scrape.preprocess()
#https://chunml.github.io/ChunML.github.io/project/Creating-Text-Generator-Using-Recurrent-Neural-Network/