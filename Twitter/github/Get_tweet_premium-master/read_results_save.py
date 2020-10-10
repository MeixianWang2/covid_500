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
def inputdict4sql(item, item_name):
    try:
        tmpitem = item[item_name]
    except:
        tmpitem = 'null'
    return tmpitem

# load item file, and save it to mysql
with open('amazon_response_token.json', 'r') as file:
    data = file.read().replace('\n', '').replace('}{', '},{')
    # print(data)
    response = '[' + data + ']'
results = json.loads(response)

for result in results:
    # print(result)
    # print(result['results'])
    try:
        items = result['results']
        for item in items:
            try:
                screen_name = inputdict4sql(item['user'], 'screen_name')
                created_at = datetime.strptime(inputdict4sql(item, 'created_at'), '%a %b %d %H:%M:%S +0000 %Y')
                tweet_id = inputdict4sql(item, 'id')
                text = inputdict4sql(item, 'text')
                try:
                    extended_tweet = inputdict4sql(item['extended_tweet'], 'full_text')
                except:
                    extended_tweet = text
                quote_count = inputdict4sql(item, 'quote_count')
                reply_count = inputdict4sql(item, 'reply_count')
                retweet_count = inputdict4sql(item, 'retweet_count')
                favorite_count = inputdict4sql(item, 'favorite_count')
                truncated = inputdict4sql(item, 'truncated')
                language = inputdict4sql(item, 'lang')
                t = [screen_name, created_at, tweet_id, text, extended_tweet, quote_count, reply_count, retweet_count,
                     favorite_count, truncated, language]
                sql = "insert into company_100(screen_name,created_at,tweet_id,text,extended_tweet,quote_count,reply_count,retweet_count,favorite_count,truncated,language) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                print('sql')
                cursor.execute(sql, t)
                print('t')
                conn.commit()
            except:
                print(item)
                with open('exception.json', 'a') as outfile:
                    json.dump(item, outfile)
    except:
        print(result)
        with open('exception.json', 'a') as outfile:
            json.dump(results, outfile)


