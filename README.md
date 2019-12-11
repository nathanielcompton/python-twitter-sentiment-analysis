# Twitter Sentiment Analysis

Tweet sentiment analysis from the command line, built in Python and implemented with [tweepy], [textblob], and [click].

### Installation and Usage
This repository uses Python 3.5+. For now, also use virtualenv.

```bash
$ git clone {repo URL}
$ cd tweepy_sentiment_demo
$ cp .env_template .env
$ python -m venv venv
$ source venv/bin/activate
<venv>$ pip install -r requirements.txt
<venv>$ python app/demo.py
```

You will need to Twitter API keys and access tokens for the environment variables in `.env`. These keys and tokens are generated in the [Twitter Developer Portal].

### Development and Testing
Use [Pytest] for testing and [Black] for formatting/styling code.

[tweepy]: https://tweepy.readthedocs.io/en/latest/
[textblob]: https://textblob.readthedocs.io/en/dev/
[click]: https://click.palletsprojects.com/en/7.x/
[Twitter Developer Portal]: https://developer.twitter.com/en/apps
[Pytest]: https://docs.pytest.org/en/latest/
[Black]: https://black.readthedocs.io/en/stable/
