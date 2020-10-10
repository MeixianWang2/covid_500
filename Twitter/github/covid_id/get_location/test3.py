import pandas as pd
import numpy as np
columns = ['screen_name','created_at','tweet_id','retweet_count','favorite_count','in_reply_to_user_id']
df_LIWC = pd.read_csv('/Volumes/EDrive/covid1_6全/covid6_LIWC_nonull1.csv',dtype=object)

df = pd.read_csv('/Users/annawang/icloud/Documents/Twitter copy/github/covid_id/covid6_location.csv',  usecols=columns, dtype=object)
covid6_LIWC_nonull = pd.merge(df_LIWC,df,how = 'left',on = 'tweet_id')
covid6_LIWC_nonull.to_csv('/Users/annawang/icloud/Documents/Twitter copy/github/covid_id/covid6_LIWC_nonull2.csv')