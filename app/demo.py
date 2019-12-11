import click
from models import TweepyClient, TextBlobClient
from textblob import TextBlob


# Twitter search
public_tweets = api.search(input("Type a word or phrase for Twitter search: "))

# Sentiment Analysis
for tweet in public_tweets:
    """
    <analysis.sentiment> is a tuple of form (polarity, subjectivity ) where polarity
    is a float within the range [-1.0, 1.0] and subjectivity is a float
    within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is
    very subjective.
    """

    print("\nTweet from", tweet.user.name + ":", tweet.text)
    analysis = TextBlob(tweet.text)
    print("    Sentiment Analysis:", analysis.sentiment)
