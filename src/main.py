#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from models import TweepyClient, TextBlobClient
from utils import _validate_iso_639
from settings import DEFAULT_LANG, PROG_NAME


@click.group()
@click.version_option(version="0.2", prog_name=PROG_NAME)
def cli():
    pass


@cli.command(short_help="Show your Twitter user information.")
def whoami():
    """Show Twitter user information based on provided Twitter Developer API credentials."""
    tweepy = TweepyClient()
    check = tweepy.whoami()
    click.secho("Who Am I?", fg="green", bold=True)
    click.echo("Name: " + check["name"])
    click.echo("Screen Name: " + check["screen_name"])
    click.echo("Description: " + check["description"])


@cli.command(short_help="Search for tweets and analyze sentiment.")
@click.option(
    "--keyword", "-k", type=click.STRING, required=True, prompt="Twitter search", help="Keyword for Twitter search",
)
@click.option(
    "--language",
    "-l",
    type=click.STRING,
    default=DEFAULT_LANG,
    callback=_validate_iso_639,
    help="Search language, in ISO 639-1 format",
)
def analyze(keyword, language):
    """
        Perform sentment analysis for given Twitter keyword search.
        Reference Tweepy's API.search() docs as needed for input customization.
    """
    click.secho(f"Searching for tweets containing: '{keyword}'", fg="green")
    tweepy = TweepyClient()
    tweets = tweepy.get_tweets(keyword=keyword, language=language)
    total_num = len(tweets)
    current_num = 1
    for tweet in tweets:
        click.secho(f"\n({current_num}/{total_num}) Tweet Data:", fg="cyan")
        click.echo(f"• Screen Name: {tweet._json['user']['screen_name']}")
        click.echo(f"• Tweet Text: {tweet._json['text']}")
        # Sentiment Analysis
        tbc = TextBlobClient()
        analysis = tbc.analyze_tweet(tweet._json["text"])
        """
        Developer Note:
        <analysis.sentiment> is a tuple of form (polarity, subjectivity ) where polarity
        is a float within the range [-1.0, 1.0] and subjectivity is a float
        within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is
        very subjective.
        """

        click.secho("Sentiment Analysis:", fg="yellow")
        click.echo(f"• Polarity: {analysis.sentiment[0]}")
        click.echo(f"• Subjectivity: {analysis.sentiment[1]}")
        current_num += 1


if __name__ == "__main__":
    cli()
