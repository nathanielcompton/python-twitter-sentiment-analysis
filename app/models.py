import tweepy
from textblob import TextBlob
from config import (
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET,
)


class TweepyClient:
    def __init__(self):
        # Initialize Auth
        self.auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def get_tweets(self, keyword: str = None):
        return self.api.search(keyword)


class TextBlobClient:
    def analyze_tweet(tweet):
        return TextBlob(tweet.text)
