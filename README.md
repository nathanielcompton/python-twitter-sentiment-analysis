# Twitter Sentiment Analysis
[![PyPI - Python Version](https://img.shields.io/badge/python-3.5.0-blue.svg)](https://www.python.org/downloads/release/python-350/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)


Tweet sentiment analysis from the command line, built in Python and implemented with [tweepy], [textblob], and [click].

### Installation
This repository uses Python 3.5+. For now, also use virtualenv.

```bash
$ git clone {repo URL}
$ cd tweepy_sentiment_analysis
$ cp .env.example .env
$ python -m venv venv
$ source venv/bin/activate
<venv>$ pip install -r requirements.txt
```

You will need to Twitter API keys and access tokens for the environment variables in `.env`.
These keys and tokens are generated in the [Twitter Developer Portal].

### Usage
Once installation is complete, using this tool is as simple as calling:
```bash
<venv>$ python src/main.py [COMMAND] [OPTIONAL FLAGS]
```
Reference Click and Tweepy documentation as needed to understand

### Development and Testing
Use [Pytest] for testing and [Black] for formatting/styling code.

Run tests by calling:
```bash
<venv>$ pytest
```

N.B. Pytest configuration is in [pytest.ini](pytest.ini). Black configuration is in [pyproject.toml](pyproject.toml).

[tweepy]: https://tweepy.readthedocs.io/en/latest/
[textblob]: https://textblob.readthedocs.io/en/dev/
[click]: https://click.palletsprojects.com/en/7.x/
[Twitter Developer Portal]: https://developer.twitter.com/en/apps
[Pytest]: https://docs.pytest.org/en/latest/
[Black]: https://black.readthedocs.io/en/stable/
