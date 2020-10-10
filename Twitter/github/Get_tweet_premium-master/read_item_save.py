import pymysql
import json
import time
from datetime import datetime
conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='password',
                           database ='database_name',
                           charset='UTF8MB4')
cursor = conn.cursor()


# load item file, and save it to mysql
with open('amazon_item_token.json', 'r') as file:
    data = file.read().replace('\n', '').replace('}{', '},{')
    response = '['+data +']'
    print(response)
items = json.loads(response)

def inputdict4sql(item,item_name):
    try:
        tmpitem = item[item_name]
    except:
        tmpitem = 'null'
    return tmpitem

for item in items:
    print(2)
    try:
        screen_name = inputdict4sql(item['user'], 'screen_name')
        created_at = datetime.strptime(inputdict4sql(item,'created_at'),'%a %b %d %H:%M:%S +0000 %Y')
        tweet_id = inputdict4sql(item,'id')
        text = inputdict4sql(item,'text')
        quote_count = inputdict4sql(item, 'quote_count')
        reply_count = inputdict4sql(item, 'reply_count')
        retweet_count = inputdict4sql(item,'retweet_count')
        favorite_count = inputdict4sql(item,'favorite_count')
        truncated = inputdict4sql(item,'truncated')
        print(truncated)
        language = inputdict4sql(item,'lang')
        try:
            extended_tweet = inputdict4sql(item['extended_tweet'],'full_text')
        except:
            extended_tweet = text
         # continue
        t = [screen_name, created_at, tweet_id, text, extended_tweet, quote_count, reply_count, retweet_count,
             favorite_count, language]
        print(t)
        sql = "insert into company_100(screen_name,created_at,tweet_id,text,extended_tweet,quote_count,reply_count,retweet_count,favorite_count,language) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print('sql')
        cursor.execute(sql, t)
        print('t')
        conn.commit()
    except:
        print(item)
        # with open('A.json', 'a') as outfile:
        #     json.dump(item, outfile)
        continue
