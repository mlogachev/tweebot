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
        print(status.text)
        # if status.user.id != api.me().id :
        #     api.update_status(status="@" + str(status.user.screen_name) + " meow meow", in_reply_to_status_id = status.id)


tweets = []
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

russian_alphabet = [
    u'\u0430' ,
    u'\u0431' ,
    u'\u0432' ,
    u'\u0433' ,
    u'\u0434' ,
    u'\u0435' ,
    u'\u0436' ,
    u'\u0437' ,
    u'\u0438' ,
    u'\u0439' ,
    u'\u043a' ,
    u'\u043b' ,
    u'\u043c' ,
    u'\u043d' ,
    u'\u043e' ,
    u'\u043f' ,
    u'\u0440' ,
    u'\u0441' ,
    u'\u0442' ,
    u'\u0443' ,
    u'\u0444' ,
    u'\u0445' ,
    u'\u0446' ,
    u'\u0447' ,
    u'\u0448' ,
    u'\u0449' ,
    u'\u044a' ,
    u'\u044b' ,
    u'\u044c' ,
    u'\u044d' ,
    u'\u044e' ,
    u'\u044f'
]


myStream.filter(track=russian_alphabet, languages=['ru'])