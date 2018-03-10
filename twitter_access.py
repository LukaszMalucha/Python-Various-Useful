import json
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = 'JdtQ9Bo5WdOfwmZwZCaa6xUq7'
CONSUMER_SECRET = 'oNoZDCtojF076qj8FB9XizZapj8GImTzkrPchWz9u8lqEBBjVA'
OAUTH_TOKEN = '972493075317776385-F6SjPPjJgRs2tc5ktmFRkWiNBBHaAPh'
OAUTH_TOKEN_SECRET = '03zatnZGuWrMzpsxZAngfWNjoYtpT9OW1TqPBMk7IbBHD'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)                      
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)                  ## for authorization

api = tweepy.API(auth)                                                  ## Connect to data


count = 10
query = 'Dublin'

## Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]        ## Use api.search object based on query (10) value to create list

for result in results:                                                                  ## print as json
    print(json.dumps(result._json, indent=2))                                           ##     