import csv
import pandas as pd
import numpy as np
# drop columns
# df = pd.read_csv('/Users/annawang/icloud/Documents/Twitter copy/covid_4_state.csv')
# df = df.drop(columns=['state', 'tweet_city', 'tweet_country'])
#
# df.to_csv('covid4_all.csv', encoding='utf-8', na_rep='Null', errors='ignore', mode='a', index=False)

df_LIWC = pd.read_csv('/Volumes/EDrive/covid1_6全/covid6_LIWC_nonull.csv',dtype={'tweet_id':object})
pd.set_option('display.max_columns', None)

#
df_LIWC = df_LIWC.rename(columns={"A": "tweet_id", "B": "user_location","C": "state_abbrev", "D": "text"})
df_LIWC = df_LIWC.drop([0])
df_LIWC = df_LIWC.drop(columns=['text'])
# df_LIWC = df_LIWC.drop(columns=['language','in_reply_to_screen_name','in_reply_to_status_id','retweeted'])
# df_LIWC['tweet_id'].replace('Null', np.nan, inplace=True)
# df_LIWC.dropna(subset=['tweet_id'], inplace=True)
# df_LIWC['favorite_count'].replace('Null', np.nan, inplace=True)
# df_LIWC.dropna(subset=['tweet_id'], inplace=True)
# print(df_LIWC['favorite_count'].unique().tolist())
print(df_LIWC.head())
print(df_LIWC.dtypes)
# df_LIWC.to_csv(r'/Volumes/EDrive/covid1_6全/covid4_all.csv', index=False)
# #
# df_LIWC = pd.read_csv('/Volumes/EDrive/covid1_6全/covid4_all.csv')
#
# df_LIWC = df_LIWC.drop(columns='text')
# pd.set_option('display.max_columns', None)
# print(df_LIWC.head())
print(df_LIWC.shape)
# print(df_LIWC[['user_location', 'state_abbrev']])
df_LIWC.to_csv(r'/Volumes/EDrive/covid1_6全/covid6_LIWC_nonull1.csv', index=False)

