import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
# # 1. get a random sample 100 rows
# df = pd.read_csv('/Users/annawang/icloud/Documents/Twitter copy/github/covid_id/scratch.csv')
# pd.set_option('display.max_columns', None)
# # print(len(df.columns))
# # print(df.columns)
#
# cols = df.columns.tolist()
# print(cols)
# print(len(cols))
# #




# print(len(list))
# pd.set_option('display.max_columns', None)
# # df = df.sample(n = 1000)
# is_na = df['user_location'].isnull().sum()
# print(is_na)
# df.to_csv('sample_covid5.csv', encoding='utf-8', na_rep='Null', errors='ignore', mode='a', index=False)

# 2. try to delete null rows in sample data
# df = pd.read_csv('/Volumes/EDrive/covid1_6全/covid6_location.csv')
# df['state_abbrev'].replace('Null', np.nan, inplace=True)
# df.dropna(subset=['state_abbrev'], inplace=True)
# print(df['state_abbrev'])
# is_na= df['state_abbrev'].isnull().sum()
# print(is_na)
# print(df.head())
# print(df.shape)
# print(df.dtypes)
# #
# # 3. process the data
# df = pd.read_csv('/Volumes/EDrive/covid1_6全/covid4_state_abbrev.csv')
#
# df['state_abbrev'].replace('Null', np.nan, inplace=True)
# df = df.dropna(subset=['state_abbrev'], inplace=False)
# #
# df.to_csv('covid4_nonull.csv')


# check null value
df = pd.read_csv('/Users/annawang/icloud/Documents/Twitter copy/github/covid_id/covid6_LIWC_nonull1.csv',dtype=object)
df.drop(['Unnamed: 0'], axis=1, inplace = True)
# df['tweet_id'].replace('Null', np.nan, inplace=True)
# print(df['tweet_id'].isnull().sum())
# # df.dropna(subset=['tweet_id'], inplace=True)
# # is_na= df['tweet_id'].isnull().sum()
# # print(is_na)
# # df['retweet_count'].replace('Null', np.nan, inplace=True)
# # df.dropna(subset=['retweet_count'], inplace=True)
# is_na= df['retweet_count'].isnull().sum()
# print(is_na)
# # df['favorite_count'].replace('Null', np.nan, inplace=True)
# # df.dropna(subset=['favorite_count'], inplace=True)
# is_na= df['favorite_count'].isnull().sum()
# print(is_na)
df['tweet_id']=df['tweet_id'].astype(int)
df['retweet_count']=df['retweet_count'].astype(int)
df['favorite_count']=df['favorite_count'].astype(int)
df['WC']=df['WC'].astype(float)
df['WC']=df['WC'].astype(int)


print(df.head())
print(df.shape)
print(df.dtypes[0:17])
# df.to_csv('/Volumes/EDrive/covid1_6全/covid3_LIWC_nonull3.csv', index=False)
# df= pd.read_csv('/Users/annawang/icloud/Documents/Twitter copy/github/covid_id/covid6_location.csv')
# df_part = df.loc[:,['tweet_id','user_location']]
df.to_csv('/Users/annawang/icloud/Documents/Twitter copy/github/covid_id/covid6_LIWC_nonull2.csv',index =False)
# print(df_part.head())
# print(df.dtypes)