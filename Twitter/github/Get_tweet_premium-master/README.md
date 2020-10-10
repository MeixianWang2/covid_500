# Get_tweet_premium_search(official method)
In this file I use premium search api to get tweets from twitter API. (#https://developer.twitter.com/en/docs/tweets/search/overview)
full_achrive search api can get tweet from anytime, 30 days search api can only get tweet in past 30 days.

#connect to twitter search api (premium: full_archive or 30 days)
#fullarchive
endpoint = "https://api.twitter.com/1.1/tweets/search/fullarchive/your_app_name.json"
# or 30 days
endpoint = "https://api.twitter.com/1.1/tweets/search/30day/your_app_name.json"
# get bearer token
#https://developer.twitter.com/en/docs/basics/authentication/oauth-2-0/bearer-tokens(guid of getting brearer-token)
headers = {"Authorization":"Bearer token_name", "Content-Type": "application/json"}

# write query
# full_archive
data = '{"query":"(#covid_19 OR #Covid19 OR #Covid OR #Coronavirus OR #Coronavirus19) lang:en", "fromDate": "202003010000", "toDate": "202003310000", "maxResults": 100}'
# 30 days
data = '{"query":"(#covid_19 OR #Covid19 OR #Covid OR #Coronavirus OR #Coronavirus19) lang:en",  "maxResults": 100}'

response = requests.post(endpoint, data=data, headers=headers).json()

#search and filter rules
https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/operators-by-product

# premium has free version: sandbox, which can be used to have a try


Free api: twitter api, tweepy can get tweets post in past 7 days 

or use timeline can get the 3400 tweets post by authors from now to the past.

