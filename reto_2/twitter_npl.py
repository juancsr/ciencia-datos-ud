import os
import nltk
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

nltk.download('punkt')
nltk.download('wordnet')
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
# From: https://www.youtube.com/watch?v=ujId4ipkBio
# -- Pre-procesor
df = pd.DataFrame([tweet['text'] for tweet in tweets], columns=['Tweets'])

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
  # Remove '
  tweet_text = tweet_text.replace("'", '')
  tweet_text = tweet_text.lower()
  return tweet_text

df['Tweets'] = df['Tweets'].apply(clean_tweet)

# -- Transformation
def get_words(text):
  return TextBlob(text).words.lemmatize()

# Word Cloud
df['Words'] = df['Tweets'].apply(get_words)
allwords = ' '.join([twts for twts in df['Tweets']]) # this one works better than lemmatize
#allwords = ' '.join([str(twts) for twts in df['Words']])
wc = WordCloud(width=500, height=300, random_state=21, max_font_size=119).generate(allwords)

# Statistics
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.savefig('./bilinear.png')
# common words: covid19, lockdown, victoria, delta

# -- Data mining
# Sentiment Analysis
def get_subjectivity(text):
  return TextBlob(text).sentiment.subjectivity

def get_polarity(text):
  return TextBlob(text).sentiment.polarity


df['Subjectivity'] = df['Tweets'].apply(get_subjectivity)
df['Polarity'] = df['Tweets'].apply(get_polarity)

# function that compute the negative, neutral and positive analysis
def get_analysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

df['Analysis'] = df['Polarity'].apply(get_analysis)

log_info('Print all of the positive tweets')
sorted_df = df.sort_values(by=['Polarity'])
pos_tweets = []
for i in range(0, sorted_df.shape[0]):
  analysis = sorted_df['Analysis'][i]
  if analysis == 'Positive':
    pos_tweets = sorted_df['Tweets'][i]

# Plot polarity and subjectivity
plt.figure(figsize=(10, 12))
for i in range(0, df.shape[0]):
  plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Blue')

plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.savefig('./scatter.png')

log_info('Final results')
# Positive tweets count
pos_tweets = df[df.Analysis == 'Positive'].shape[0]
per_pos = round(pos_tweets / df.shape[0] * 100, 1)
# Negative tweets count
neg_tweets = df[df.Analysis == 'Negative'].shape[0]
per_neg = round(neg_tweets / df.shape[0] * 100, 1)
# Neutral tweets count
neu_tweets = df[df.Analysis == 'Neutral'].shape[0]
per_neu = round(neu_tweets / df.shape[0] * 100, 1)

print('Number of positive tweets: {} ({} %)'.format(pos_tweets, per_pos) )
print('Number of negative tweets: {} ({} %)'.format(neg_tweets, per_neg) )
print('Number of neutral tweets: {} ({} %)'.format(neu_tweets, per_neu))

# Plot and visualize the counts
plt.figure(figsize=(10, 13))
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind='bar')
plt.savefig('./bar.png')