import os
import tweepy
from textblob import TextBlob

# Config
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

# Auth
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Twitter search
public_tweets = api.search(input("Type a word or phrase for Twitter search: "))

# Sentiment Analysis
for tweet in public_tweets:
    print("\nTweet from", tweet.user.name + ":", tweet.text)
    analysis = TextBlob(tweet.text)
    print("    Sentiment Analysis:", analysis.sentiment)

    """
    FYI: <analysis.sentiment> is a tuple of form (polarity, subjectivity ) where polarity
    is a float within the range [-1.0, 1.0] and subjectivity is a float
    within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is
    very subjective.
    """
