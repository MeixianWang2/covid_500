import requests
import pymysql
import json
import time
import sys
from datetime import datetime
conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='4320241oK@',
                           database ='covid_startup',
                           charset='UTF8MB4')
cursor = conn.cursor()

# endpoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/developing.json"
#maven1
# endpoint = "https://api.twitter.com/1.1/tweets/search/30day/sandbox.json"
# headers = {"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAAJh5DQEAAAAAjCz8jvR3LIv8gF%2F2cVdsclN72SU%3DIz4LVXcM8V22zWNPZEX0ZMvONWX59P9UtweTUbXZSt5XqysrYx", "Content-Type": "application/json"}
#maven2
# 30 days
endpoint = "https://api.twitter.com/1.1/tweets/search/30day/covid.json"
# fullachive
# endpoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/covid.json"
headers = {"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANeRDgEAAAAA%2FXkoCiB3YX3Rx6kHj1keDlK8K3w%3DpUvvkKeW4HpVD48u25846YlzPlSPPVWpYhT2SzEZB0QueJywHd", "Content-Type": "application/json"}

# 30 days query
data ='{"query":"((#Covid19 #startup) OR (#Coronavirus #entrepreneur) OR (#Covid19 #entrepreneur) OR (#Covid19 #small business) OR (#Cornavirus #small business) OR (#Cornavirus #startup)) lang:en", "maxResults": 100,"fromDate": "202006280000"}'
# full_archive query
# data ='{"query":"((#Covid19 #startup) OR (#Covid19 #entrepreneur) OR (#Covid19 #small business) OR (#Coronavirus #entrepreneur)) lang:en", "maxResults": 100,"fromDate": "202001010000", "toDate": "202001280000"}'
# data ='{"query":"((#Covid #startup) OR (#Cornavirus #small business) OR (#Cornavirus #startup)) lang:en", "maxResults": 100,"fromDate": "202003140000", "toDate": "202003140000"}'

response = requests.post(endpoint, data=data, headers=headers).json()
print(response)
# save json file
with open('covid_startup.json', 'a') as outfile:
    json.dump(response, outfile)

items = response['results']

# print(items)
def inputdict4sql(item,item_name):
    try:
        tmpitem = item[item_name]
    except:
        tmpitem = 'null'
    return tmpitem

for item in items:
    try:
        screen_name = inputdict4sql(item['user'], 'screen_name')
        created_at = datetime.strptime(inputdict4sql(item, 'created_at'), '%a %b %d %H:%M:%S +0000 %Y')
        tweet_id = inputdict4sql(item, 'id')
        text = inputdict4sql(item, 'text')
        quote_count = inputdict4sql(item, 'quote_count')
        reply_count = inputdict4sql(item, 'reply_count')
        retweet_count = inputdict4sql(item, 'retweet_count')
        favorite_count = inputdict4sql(item, 'favorite_count')
        truncated = inputdict4sql(item, 'truncated')
        language = inputdict4sql(item, 'lang')
        try:
            extended_tweet = inputdict4sql(item['extended_tweet'], 'full_text')
        except:
            extended_tweet = text
            # continue
        t = [screen_name, created_at, tweet_id, text, extended_tweet, quote_count, reply_count, retweet_count,
             favorite_count, truncated, language]
        sql = "insert into covid_startup_1 (screen_name,created_at,tweet_id,text,extended_tweet,quote_count,reply_count,retweet_count,favorite_count,truncated,language) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, t)
        conn.commit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print(item)
        with open('except_covid.json', 'a') as outfile:
            json.dump(item, outfile)
        # continue
next_token = response['next']
token_count = 301
s=[next_token,token_count]
sql = "insert into token_covid_startup_1 (next_token,token_count) values (%s,%s)"
cursor.execute(sql, s)
conn.commit()
print(next_token)
for t in range(10):
    for i in range(10):
        print(i)
        data = '{"query":"((#Covid #startup) OR (#Coronavirus #entrepreneur) OR (#Covid19 #entrepreneur) OR (#Covid19 #small business) OR (#Cornavirus #small business) OR (#Cornavirus #startup) ) lang:en ", "maxResults": 100, "fromDate": "202006280000","next":"' + next_token + '"}'
        response = requests.post(endpoint, data=data, headers=headers).json()
        with open('covid_startup.json', 'a') as outfile:
            json.dump(response, outfile)
        next_token = response['next']
        token_count = token_count+1
        s = [next_token, token_count]
        sql = "insert into token_covid_startup_1 (next_token,token_count) values (%s,%s)"
        cursor.execute(sql, s)
        conn.commit()
        items = response['results']
        for item in items:
            try:
                screen_name = inputdict4sql(item['user'], 'screen_name')
                created_at = datetime.strptime(inputdict4sql(item, 'created_at'), '%a %b %d %H:%M:%S +0000 %Y')
                tweet_id = inputdict4sql(item, 'id')
                text = inputdict4sql(item, 'text')
                quote_count = inputdict4sql(item, 'quote_count')
                reply_count = inputdict4sql(item, 'reply_count')
                retweet_count = inputdict4sql(item, 'retweet_count')
                favorite_count = inputdict4sql(item, 'favorite_count')
                truncated = inputdict4sql(item, 'truncated')
                language = inputdict4sql(item, 'lang')
                try:
                    extended_tweet = inputdict4sql(item['extended_tweet'], 'full_text')
                    # print(extended_tweet)
                except:
                    extended_tweet = text
                    # continue
                t = [screen_name, created_at, tweet_id, text, extended_tweet, quote_count, reply_count, retweet_count,
                     favorite_count, truncated, language]
                sql = "insert into covid_startup_1 (screen_name,created_at,tweet_id,text,extended_tweet,quote_count,reply_count,retweet_count,favorite_count,truncated,language) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, t)
                conn.commit()
            except:
                print("Unexpected error:", sys.exc_info()[0])
                print(item)
                with open('except_covid.json', 'a') as outfile:
                    json.dump(item, outfile)
                continue
    time.sleep(120)