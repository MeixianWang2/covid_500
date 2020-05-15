import pymysql
import json
import time
from datetime import datetime
conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='4320241oK@',
                           database ='covid_500',
                           charset='UTF8MB4')
cursor = conn.cursor()


# load item file, and save it to mysql
with open('company_500_add11-13.json', 'r') as file:
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
    try:
        screen_name = inputdict4sql(item['user'], 'screen_name')
        created_at = datetime.strptime(inputdict4sql(item,'created_at'),'%a %b %d %H:%M:%S +0000 %Y')
        tweet_id = inputdict4sql(item,'id')
        text = inputdict4sql(item,'text')
        retweet_count = inputdict4sql(item,'retweet_count')
        favorite_count = inputdict4sql(item,'favorite_count')
        truncated = inputdict4sql(item,'truncated')
        language = inputdict4sql(item,'lang')
        in_reply_to_screen_name = inputdict4sql(item, 'in_reply_to_screen_name')
        in_reply_to_status_id = inputdict4sql(item, 'in_reply_to_status_id')
        in_reply_to_user_id = inputdict4sql(item, 'in_reply_to_user_id')
        try:
            extended_tweet = inputdict4sql(item['extended_tweet'],'full_text')
        except:
            extended_tweet = text
         # continue
        t = [screen_name, created_at, tweet_id, text, extended_tweet, retweet_count,in_reply_to_screen_name,
             in_reply_to_status_id, in_reply_to_user_id, favorite_count, language]
        print(t)
        sql = "insert into tweet_500(screen_name,created_at,tweet_id,text,extended_tweet,retweet_count,in_reply_to_screen_name,in_reply_to_status_id, in_reply_to_user_id,favorite_count,language) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print('sql')
        cursor.execute(sql, t)
        print('t')
        conn.commit()
    except:
        print(item)
        # with open('A.json', 'a') as outfile:
        #     json.dump(item, outfile)
        continue