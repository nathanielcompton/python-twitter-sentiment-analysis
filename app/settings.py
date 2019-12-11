import os
from pathlib import Path
from dotenv import load_dotenv

# Edit as needed (e.g. if you relocate `.env`)
DOT_ENV_FILENAME = ".env"
ENV_PATH = Path(__file__).resolve().parents[1] / DOT_ENV_FILENAME

if not ENV_PATH.is_file():
    raise IOError("Incorrect ENV_PATH. File not found!")
else:
    load_dotenv(dotenv_path=ENV_PATH)

# Configurable via ``.env`
TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
