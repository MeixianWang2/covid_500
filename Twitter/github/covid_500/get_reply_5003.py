import json
import time
import logging
import twitter
import urllib.parse
#
t = twitter.Api(
    access_token_key="1250078614445608967-JMqL7diIPwuIoK8ZJmvD9NhZ6mtyiM",
    access_token_secret="9QAiPJqRufglsUMUMGgBDqkq0TtkPrJr1ryusdj4Hz7iJ",
    consumer_key="4p8kX8fcODiTRnbledyEEJQfl",
    consumer_secret="ZiVraz4cV2q5VgcBxobFah2dtH3fFwIa1tpHdrPXCwFLZvNpRt",
    sleep_on_rate_limit=True)
# #
# t = twitter.Api(
#     access_token_key = "1133765235636989962-UCNSXfoqZt5w2vUu4i6QWMNcLV1E7R",
#     access_token_secret = "mjiCNOaww4BPYwiFCn4PycSgtiAPnuAFnO452eZa8Oki3",
#     consumer_key = "NZdbhxBnNsRT3Hr95NiKnvopu",
#     consumer_secret = "vRtA7GbyemzeVJIYLTaMTtp4bqZzUMKzTRgGefZlaDDcpmzdVL")


def tweet_url(t):
    return "https://twitter.com/%s/status/%s" % (t.user.screen_name, t.id)

def get_tweets(filename):
    for line in open(filename):
        print(line)
        yield twitter.Status.NewFromJsonDict(json.loads(line))
        print(twitter.Status.NewFromJsonDict(json.loads(line)))

def get_replies(tweet):
    user = tweet.user.screen_name
    tweet_id = tweet.id
    max_id = None
    logging.info("looking for replies to: %s" % tweet_url(tweet))
    page_index = 0
    while True:
        q = urllib.parse.urlencode({"q": "to:%s" % user})
        page_index += 1
        print(f"Page: {page_index}")
        try:
            replies = t.GetSearch(raw_query=q, since_id=tweet_id, max_id=max_id, count=100)
        except twitter.error.TwitterError as e:
            print(e)
            print('Will sleep for a minute.')
            logging.error("caught twitter api error: %s", e)
            time.sleep(60)
            continue
        if not replies:
            break
        for reply in replies:
            logging.info("examining: %s" % tweet_url(reply))
            if reply.in_reply_to_status_id == tweet_id:
                print(reply.in_reply_to_status_id)
                print(reply)
                logging.info("found reply: %s" % tweet_url(reply))
                yield reply
            max_id = reply.id -1
        if len(replies) != 100:
            print(len(replies))
            # print('Length exceeded 100.')
            break


if __name__ == "__main__":
    logging.basicConfig(filename="replies.log", level=logging.INFO)
    tweets_file = "/Users/annawang/Documents/RAproject/covid_500/Twitter/github/covid_500/covid_500_id.text"
    # sys.argv[1]
    for tweet in get_tweets(tweets_file):
        for reply in get_replies(tweet):
            print(reply)
            print('reply')
            print(reply.AsJsonString())
            # with open('covid_/Users/annawang/Documents/RAproject/Twitter/github/get_reply/readID.txtly.AsJsonString(), outfile)
            with open('B.json', 'a') as f:
                f.writelines(reply.AsJsonString())
            continue