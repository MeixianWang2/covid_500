import pandas as pd
import datetime
import numpy as np
dtypes = {'tweet_id':int,'retweet_count': int, 'favorite_count':int,'WC':int, 'in_reply_to_user_id':object}
df = pd.read_csv('/Volumes/EDrive/covid1_6全/covid6_LIWC_nonull2.csv',dtype={ 'in_reply_to_user_id':object})
# df.drop('Unnamed: 0',axis = 1)
# df = df[['screen_name', 'created_at', 'tweet_id', 'retweet_count', 'favorite_count', 'in_reply_to_user_id', 'user_location', 'state_abbrev', 'WC', 'Analytic', 'Clout', 'Authentic', 'Tone', 'WPS', 'Sixltr', 'Dic', 'function', 'pronoun', 'ppron', 'i', 'we', 'you', 'shehe', 'they', 'ipron', 'article', 'prep', 'auxverb', 'adverb', 'conj', 'negate', 'verb', 'adj', 'compare', 'interrog', 'number', 'quant', 'affect', 'posemo', 'negemo', 'anx', 'anger', 'sad', 'social', 'family', 'friend', 'female', 'male', 'cogproc', 'insight', 'cause', 'discrep', 'tentat', 'certain', 'differ', 'percept', 'see', 'hear', 'feel', 'bio', 'body', 'health', 'sexual', 'ingest', 'drives', 'affiliation', 'achieve', 'power', 'reward', 'risk', 'focuspast', 'focuspresent', 'focusfuture', 'relativ', 'motion', 'space', 'time', 'work', 'leisure', 'home', 'money', 'relig', 'death', 'informal', 'swear', 'netspeak', 'assent', 'nonflu', 'filler', 'AllPunc', 'Period', 'Comma', 'Colon', 'SemiC', 'QMark', 'Exclam', 'Dash', 'Quote', 'Apostro', 'Parenth', 'OtherP']]
pd.set_option('display.max_columns', None)
# # df = df.drop(columns=['state_abbrev'])
#
# df = df.rename(columns={"A": "screen_name", "B": "created_at","C": "tweet_id", "D": "text", "E":"retweet_count",
#                         "F": "favorite_count","G":"language","H":"in_reply_to_screen_name", "I":"in_reply_to_status_id",
#                         "J":"in_reply_to_user_id", "K": "retweeted", "L":"user_location", "M":"state_abbrev"})
# df = np.unique(df[['state_abbrev']], axis=0)

# a = df['state_abbrev'].unique().tolist()


# print(df.head())
# print(df.shape)
# print(df.dtypes)
# print(df.info)

# print(df[['user_location', 'state_abbrev']])
# df = df.drop(columns=['text'])
#
# df.to_csv('covid2_location.csv', encoding='utf-8', na_rep='Null', errors='ignore', mode='a', index=False)

# #sample data
# covid_test = df.head(100)
# covid_test.to_csv('covid_test.csv')
# print(covid_test.info)

#change data type
# #
# df = pd.read_csv('/Users/annawang/icloud/Documents/Twitter copy/github/covid_id/covid2_LIWC_nonull2.csv',dtype={'tweet_id':int, 'retweet_count': int, 'favorite_count':int})
# df = pd.read_csv('/Volumes/EDrive/covid1_6全/covid3_LIWC_nonull1.csv')
pd.set_option('display.max_columns', None)
# df = df.drop(['Unnamed: 0'], axis=1)



# df['tweet_id'].replace('Null', np.nan, inplace=True)
# tw = df['tweet_id'].isnull().sum()
# print(tw)
# df.tweet_id.astype(int)
# df.retweet_count.astype("Int64")
print(df.dtypes)
#
# df.tweet_id.astype(float)
# df.retweet_count.astype(int)
print(df.shape)
print(df.head())
#
# df = pd.read_csv('/Volumes/EDrive/covid1_6全/covid4_LIWC_nonull.csv', dtype={'tweet_id': int, 'retweet_count': int, 'favorite_count':int})
# df = df.drop(columns=['in_reply_to_screen_name', 'in_reply_to_status_id', 'language','retweeted'])
# state_list = df.state_abbrev.unique().tolist()
# print(state_list)
# print(len(state_list))
# print(df.dtypes[0:15])
# print(df.head())
# print(df.shape)
# df.to_csv('/Volumes/EDrive/covid1_6全/covid3_LIWC_nonull2.csv', index=False)