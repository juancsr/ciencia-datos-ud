from pymongo import MongoClient

class MongoDB:
  '''MongoDB
  handle db
  '''
  user = ''
  passwd = ''
  db_name = ''
  port = '27016'
  host = 'localhost'
  client = MongoClient()
  db = None
  collection_name = 'covidtweets'
  collection = None

  def __init__(self, user, passwd, db):
    self.user = user
    self.passwd = passwd
    self.db_name = db
    # user:password@host:port/database_name
    connection_uri = 'mongodb://{}:{}@{}:{}/{}?authSource=admin'.format(
        self.user, self.passwd,
        self.host, self.port,
        self.db_name)
    try:
      self.client = MongoClient(connection_uri)
      self.db = self.client[self.db_name]
      self.collection = self.db[self.collection_name]
    except Exception as e:
      print('could not create mongo client: {}'.format(e))


  def insert(self, data: any) -> bool:
    ok = False
    try:
      result = self.collection.insert_many(data)
      if len(result.inserted_ids) > 0:
        ok = True
    except Exception as e:
      print('could not insert data: {}'.format(e))
    return ok

  def get_tweets(self):
    tweets = []
    try:
      results = self.collection.find()
      for result in results:
        tweets.append(result)
    except Exception as e:
      print('could not get covid tweets: {}'.format(e))
    return tweets
    
