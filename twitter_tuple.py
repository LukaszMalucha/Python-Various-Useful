import json
import tweepy
from tweepy import OAuthHandler


CONSUMER_KEY = '****'
CONSUMER_SECRET = '****'
OAUTH_TOKEN = '****'
OAUTH_TOKEN_SECRET = '*****'


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)                      
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)                  ## for authorization

api = tweepy.API(auth)                                                  ## Connect to data


count = 50
query = 'Dublin'

## Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]        ## Use api.search object based on query (10) value to create list

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                                for status in results
                                        for mention in status._json['entities']['user_mentions'] ]
                                        
hashtags = [hashtag['text']
                                        for status in results
                                                    for hashtag in status._json['entities']['hashtags'] ] 
                                                    
words = [ word
                                for text in status_texts
                                         for word in text.split() ]  
                                         
                                         
print(json.dumps(status_texts[0:5], indent=1)) 
print(json.dumps(screen_names[0:5], indent=1)) 
print(json.dumps(hashtags[0:5], indent=1)) 
print(json.dumps(words[0:5], indent=1))                                         
                                         
                                         
                                         
                                         
                                         