import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status)
        print(status.user)
        print("@"+status.user.screen_name)
        if status.user.id != api.me().id :
            api.update_status(status="@" + str(status.user.screen_name) + " meow meow", in_reply_to_status_id = status.id)


tweets = []
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

myStream.filter(track=['meow'], languages=['en'])