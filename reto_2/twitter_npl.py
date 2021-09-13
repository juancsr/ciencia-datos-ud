import os
from typing import Text
import tweepy
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud
from database.mongo import MongoDB
from utils.logs import log_info, log_error, log_warning

plt.style.use('fivethirtyeight')

consumer_key = None
consumer_secret = None
access_token = None
access_token_secret = None
db_user = None
db_passwd = None
db_name = None


def get_env_data_as_dict(path: str) -> dict:
  with open(path, 'r') as f:
    return dict(tuple(line.replace('\n', '').split('=')) for line
      in f.readlines() if not line.startswith('#'))


# Getting sensible data from env variables
try:
  consumer_key = os.environ['TWITTER_CONSUMER_KEY']
  consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
  access_token = os.environ['TWITTER_ACCESS_TOKEN']
  access_token_secret = os.environ['TWITTER_SECRET_ACCESS_TOKEN']

  env = get_env_data_as_dict('./.env')
  db_user = env['DB_USERNAME']
  db_passwd = env['DB_PASSWORD']
  db_name = env['DB_DATABASE']

except Exception as e:
  log_error('could not get env variables', e)

# connecting to db...
db = MongoDB(db_user, db_passwd, db_name)
tweets = db.get_tweets()


# if there are not tweets on db then added new ones
if len(tweets) <= 0:
  log_warning('no tweets found. inserting new ones')
  # tweepy configuration
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  search_words = ['covid','#covid-19','#covid19', 'lockdown']
  public_tweets = api.search(q=search_words, lang='en', count=1000)
  
  for tweet in public_tweets:
    tweets.append({'text': tweet.text})

  ok = db.insert(tweets)
  if ok:
    log_info('inserted done!')

# NLP

# -- Pre-procesor
df = pd.DataFrame([tweet['text'] for tweet in tweets], columns=['Tweets'])
print(df.head())

# cleanning data...
def clean_tweet(tweet_text: str):
  # Removing @mentions
  tweet_text = re.sub(r'@[A-Za-z0-9]+', '', tweet_text)
  # Removing '#' hashtags
  tweet_text = re.sub(r'#', '', tweet_text)
  # Removing RT (ReTweets)
  tweet_text = re.sub(r'RT[\s]', '', tweet_text)
  # Removing URLs
  tweet_text = re.sub(r'https?:\/\/\S+', '', tweet_text)
  tweet_text = tweet_text.lower()
  return tweet_text

df['Tweets'] = df['Tweets'].apply(clean_tweet)
print(df.head())
# -- Transformation

# -- Data mining
# Sentiment Analysis
def get_subjectivity(text):
  return TextBlob(text).sentiment.subjectivity

def get_polarity(text):
  return TextBlob(text).sentiment.polarity

df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
df['Polarity'] = df['Tweets'].apply(get_polarity)
print(df)

# Word Cloud
