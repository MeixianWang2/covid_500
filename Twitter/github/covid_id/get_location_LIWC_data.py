import pandas as pd
import numpy as np
df = pd.read_csv('/Volumes/EDrive/covid1_6全/covid2_LIWC.csv')

pd.set_option('display.max_columns', None)
# # df = df.drop(columns=['state_abbrev'])
#
# df = df.rename(columns={"A": "screen_name", "B": "created_at","C": "tweet_id", "D": "text", "E":"retweet_count",
#                         "F": "favorite_count","G":"language","H":"in_reply_to_screen_name", "I":"in_reply_to_status_id",
#                         "J":"in_reply_to_user_id", "K": "retweeted", "L":"user_location", "M":"state_abbrev"})
# df = np.unique(df[['state_abbrev']], axis=0)

# a = df['state_abbrev'].unique().tolist()

# drop null rows
df['state_abbrev'].replace('', np.nan, inplace=True)
df = df.dropna(axis=0, subset=['Charge_Per_Line'])

print(df.head())
print(df.shape)
