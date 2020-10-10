import json
import gzip
import binascii
import os
import pandas as pd
import pymysql
from datetime import datetime
conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='4320241oK@',
                           database='covid_id',
                           charset='UTF8MB4')
cursor = conn.cursor()

base_dir = '/Volumes/EDrive/sentiment/2020-09'

#Get all files in the directory

data_list = []
for file in os.listdir(base_dir):

    #If file is a json, construct it's full path and open it, append all json data to list
    if 'jsonl' in file:
        json_path = os.path.join(base_dir, file)
        print(json_path)

        filename = json_path # Sample file.

        json_content = []
        with gzip.open(filename, 'rb') as gzip_file:
            for line in gzip_file:  # Read one line.
                line = line.rstrip()
                if line:  # Any JSON data on it?
                    obj = json.loads(line)
                    json_content.append(obj)

        # print(json.dumps(json_content, indent=4)) # Pretty-print data parsed.
        # items = json.dumps(json_content, indent=4)
        # print(len(items))



        def inputdict4sql(item,item_name):
            try:
                tmpitem = item[item_name]
            except:
                tmpitem = 'null'
            return tmpitem

        for item in json_content:
            language = inputdict4sql(item,'lang')

            if language == 'en':
                print(1)
                try:
                    # screen_name = inputdict4sql(item['user'], 'screen_name')
                    # created_at = datetime.strptime(inputdict4sql(item,'created_at'),'%a %b %d %H:%M:%S +0000 %Y')
                    tweet_id = inputdict4sql(item,'id')
                    text = inputdict4sql(item,'full_text')
                    # retweet_count = inputdict4sql(item,'retweet_count')
                    # favorite_count = inputdict4sql(item,'favorite_count')
                    #
                    # in_reply_to_screen_name = inputdict4sql(item, 'in_reply_to_screen_name')
                    # in_reply_to_status_id = inputdict4sql(item, 'in_reply_to_status_id')
                    # in_reply_to_user_id = inputdict4sql(item, 'in_reply_to_user_id')
                    # geo = inputdict4sql(item, 'geo')
                    # coordinates = inputdict4sql(item,'coordinates')
                    # place = inputdict4sql(item,'place')

                     # continue
                    t = [tweet_id,text]
                    # t = [screen_name, created_at, tweet_id, text, retweet_count,favorite_count,in_reply_to_screen_name,
                    #      in_reply_to_status_id, in_reply_to_user_id,geo,coordinates,place, language]
                    sql = "insert into covid1(tweet_id,text) values (%s,%s)"
                    print('sql')
                    cursor.execute(sql, t)
                    print('t')
                    conn.commit()
                except:
                    print(item)
                    # with open('except.json', 'a') as outfile:
                    #     json.dump(item, outfile)
            continue