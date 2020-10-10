import tweepy  # https://github.com/tweepy/tweepy
from time import time
import json

access_token = "1133765235636989962-UCNSXfoqZt5w2vUu4i6QWMNcLV1E7R"
access_token_secret = "mjiCNOaww4BPYwiFCn4PycSgtiAPnuAFnO452eZa8Oki3"
consumer_key = "NZdbhxBnNsRT3Hr95NiKnvopu"
consumer_secret = "vRtA7GbyemzeVJIYLTaMTtp4bqZzUMKzTRgGefZlaDDcpmzdVL"

def get_all_tweets(n):
    access_key = access_token
    access_secret = access_token_secret
    # Twitter only allows access to a users most recent 3240 tweets with this method
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    # initialize a list to hold all the tweepy Tweets

    # make initial request for most recent tweets (200 is the maximum allowed count)
    tweets = api.statuses_lookup(id[id])
    print(n)
    print(tweets)

        # with open('covid_startup_comments.json', 'a') as f:
        #     f.writelines(tweet.AsJsonString())
    with open('tweet_id.json', 'w', encoding='utf-8') as f:
        json.dump(tweets, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    get_all_tweets('1270506031345471488')
    # list = ['Xu_TremorBuster']
    # for i in list:
    #     try:
    #         get_all_tweets(i)
    #     except:
    #         print(i)
    #         continue


