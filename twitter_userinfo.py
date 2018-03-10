import tweepy
from tweepy import OAuthHandler




CONSUMER_KEY = '****'
CONSUMER_SECRET = '****'
OAUTH_TOKEN = '****'
OAUTH_TOKEN_SECRET = '*****'


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)                      
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)                  ## for authorization

api = tweepy.API(auth)                                                  ## Connect to data

user = api.get_user('@realDonaldTrump')


print(user.screen_name)
print(user.followers_count)


for friend in user.friends():
    print(friend.screen_name)
    print(friend.followers_count)
