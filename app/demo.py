import click
from models import TweepyClient, TextBlobClient
from utils import validate_iso_639
from settings import DEFAULT_LANG


@click.command()
@click.option(
    "--keyword",
    "-k",
    type=click.STRING,
    required=True,
    prompt="Twitter search",
    help="Keyword for Twitter search",
)
@click.option(
    "--language",
    "-l",
    type=click.STRING,
    default=DEFAULT_LANG,
    callback=validate_iso_639,
    help="Search language, in ISO 639-1 format"
)
def search_and_analyze(keyword, language):
    api = TweepyClient()
    tweets = api.get_tweets(keyword=keyword, language=language)
    for tweet in tweets:
        click.echo(tweet)


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

if __name__ == "__main__":
    search_and_analyze()
