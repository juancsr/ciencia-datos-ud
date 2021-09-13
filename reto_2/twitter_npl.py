import os
import tweepy
import nltk
from database.mongo import MongoDB
from utils.logs import log_info, log_error, log_warning

consumer_key = None
consumer_secret = None
access_token = None
access_token_secret = None
db_user = None
db_passwd = None
db_name = None

'''
get_env_data_as_dict
reads environement variables from a file and return them as a dict
params:
    - path: path of the env file
'''

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

'''
if there are not tweets on db then added new ones
'''
if len(tweets) <= 0:
  log_warning('no tweets found. inserting new ones')
  # tweepy configuration
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  public_tweets = api.home_timeline()

  for tweet in public_tweets:
    tweets.append({'tweet': tweet.text})

  ok = db.insert(tweets)
  if ok:
    log_info('inserted done!')

log_info(tweets)
'''
3. Minería de datos e Interpretación
Hacerlo con Matplotlib
'''
