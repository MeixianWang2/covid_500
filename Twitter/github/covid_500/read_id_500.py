import csv
import json
import pandas as pd

# with open('/Users/annawang/Documents/RAproject/Twitter/github/get_reply/Untitled.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     print(reader)
# for row in reader:
#     print(row)
#     print(row['screen_name'], row['tweet_id'])

df = pd.read_csv('/Users/annawang/Documents/RAproject/covid_500/Twitter/github/covid_500/Untitled.csv')
# print(df)
for index, row in df.iterrows():
    # print(row['screen_name'], row['tweet_id'])
    row_name = row['screen_name']
    row_id = row['tweet_id']
    response = '{"user":{"screen_name": "'+row_name +'"},"id": ' + str(row_id)+'}'
    print(response)
    with open('covid_500_id.text', 'a') as f:
        f.writelines(response+'\n')