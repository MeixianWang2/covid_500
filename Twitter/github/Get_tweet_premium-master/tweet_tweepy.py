import tweepy  # https://github.com/tweepy/tweepy
import pandas as pd
from time import time

access_token = "access_token"
access_token_secret = "access_token_secret"
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"


def get_all_tweets(screen_name):
    start = time()
    # Twitter API credentials
    # consumer_key = ""
    # consumer_secret = ""
    access_key = access_token
    access_secret = access_token_secret
    # Twitter only allows access to a users most recent 3240 tweets with this timeline
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    # initialize a list to hold all the tweepy Tweets
    alltweets = []
    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    # save most recent tweets
    alltweets.extend(new_tweets)
    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))
        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        # save most recent tweets
        alltweets.extend(new_tweets)
        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[screen_name, tweet.id_str, tweet.created_at, tweet.text, tweet.retweet_count,
                  tweet.favorite_count, tweet.truncated, tweet.is_quote_status, tweet.lang, tweet.place] for tweet in
                 alltweets]
    df = pd.DataFrame(outtweets, columns=['user_name', 'id', 'time', 'text', 'retweets', 'favorite_count', 'truncated',
                                          'quoted', 'language', 'test'])

    df.to_csv(str(screen_name) + '.csv', index=False)
    print('used: {:.2f} s'.format(time() - start))


def get_data(path):
    data = pd.read_csv(path)
    return data


def get_list(path, column):
    data = get_data(path)
    data = data[column]
    return data


def get_name(company_list):
    company_name = []
    for list in company_list:
        if isinstance(list, str):
            index = get_index(list)
            if index == len(list):
                continue
            temp = list[index + 1:]
            company_name.append(temp)

    return company_name


def get_index(data):
    index = 0
    for i in data:
        if i is "@":
            break
        else:
            index = index + 1
    return index


def main():
    data = get_list("data/Company CEOs and Social Media.csv", "CEO Twitter")
    list = get_name(data)
    for name in list:
        try:
            get_all_tweets(name)
        except:
            print(name)
            continue

if __name__ == '__main__':
    main()
