import tweepy
from typing import Dict
from textblob import TextBlob
from settings import (
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

    def get_tweets(self, keyword: str, language: str):
        return self.api.search(q=keyword, lang=language)

    def whoami(self) -> Dict[str, str]:
        res = self.api.me()
        return {
            'name': res.name,
            'screen_name': res.screen_name,
            'description': res.description
        }


class TextBlobClient:
    def analyze_tweet(self, text: str):
        return TextBlob(text)
