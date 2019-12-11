import click
from models import TweepyClient, TextBlobClient
from utils import validate_iso_639
from settings import DEFAULT_LANG


@click.group()
def cli():
    pass


@cli.command()
def whoami():
    tweepy = TweepyClient()
    check = tweepy.whoami()
    click.secho("Who Am I?", fg="green", bold=True)
    click.echo('Name: ' + check['name'])
    click.echo('Screen Name: ' + check['screen_name'])
    click.echo('Description: ' + check['description'])


@cli.command()
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
def analyze(keyword, language):
    tweepy = TweepyClient()
    tweets = tweepy.get_tweets(keyword=keyword, language=language)
    for tweet in tweets:
        click.echo("\n" + "User: " + tweet._json['user']['screen_name'])
        click.echo("Tweet Text: " + tweet._json['text'])
        # Sentiment Analysis
        tbc = TextBlobClient()
        analysis = tbc.analyze_tweet(tweet._json['text'])
        """
        <analysis.sentiment> is a tuple of form (polarity, subjectivity ) where polarity
        is a float within the range [-1.0, 1.0] and subjectivity is a float
        within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is
        very subjective.
        """

        click.echo("Analysis:")
        click.echo(analysis.sentiment)


if __name__ == "__main__":
    cli()
