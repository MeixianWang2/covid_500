# get timeline tweet (including statue and reply)
from TwitterAPI import TwitterAPI, TwitterPager
import pandas as pd
from datetime import datetime
screen_name = 'amazon'
api = TwitterAPI("access_token",
                 "access_token_secret",
                 "consumer_key",
                 "consumer_secret")

def get_all_tweets(screen_name):
    pager = TwitterPager(api,'statuses/user_timeline',{'screen_name': screen_name, 'count': 200})
    alltweets = pager.get_iterator(wait=3.5)
    outtweets = [[screen_name, tweet['id_str'], pd.to_datetime(tweet['created_at']), tweet['text'], tweet['retweet_count'],
                 tweet['user']['location'], tweet['favorite_count'], tweet['truncated'], tweet['is_quote_status'],
                 tweet['lang'], tweet['place']]for tweet in alltweets]
    
    df = pd.DataFrame(outtweets, columns=['user_name', 'id', 'time', 'text', 'retweets', 'geo', 'favorite_count',
                                      'truncated', 'quoted', 'language', 'test'])
    
    df.to_csv(str(screen_name) + '.csv', index=False)
    print('finish')

if __name__ == '__main__':
    get_all_tweets('amazon')
    
