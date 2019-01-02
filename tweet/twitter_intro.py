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

DUB_WOE_ID = 560743                                                     ## Dublin WhereOnEarth
LON_WOE_ID = 44418 

dub_trends = api.trends_place(DUB_WOE_ID)                               ## assign Dublin trends to variable
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']                                     ## create sets for lon and dub
                    for trend in dub_trends[0]['trends']])
lon_trends_set = set([trend['name']
                    for trend in lon_trends[0]['trends']])         
                    
common_trends = set.intersection(dub_trends_set, lon_trends_set)        ## common trends for both cities          


print(common_trends)