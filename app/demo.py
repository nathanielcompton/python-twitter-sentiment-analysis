import click
from models import TweepyClient, TextBlobClient


@click.command()
@click.option('--keyword', '-k', prompt='Twitter search', help='Keyword for Twitter search.')
def search_and_analyze(keyword):
    api = TweepyClient()
    tweets = api.get_tweets(keyword=keyword)
    for tweet in tweets:
        click.echo(tweet.items())


# # Sentiment Analysis
# for tweet in public_tweets:
#     """
#     <analysis.sentiment> is a tuple of form (polarity, subjectivity ) where polarity
#     is a float within the range [-1.0, 1.0] and subjectivity is a float
#     within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is
#     very subjective.
#     """
#
#     print("\nTweet from", tweet.user.name + ":", tweet.text)
#     analysis = TextBlob(tweet.text)
#     print("    Sentiment Analysis:", analysis.sentiment)

if __name__ == '__main__':
    search_and_analyze()
