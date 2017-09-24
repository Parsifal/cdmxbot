import os
import sys
from config import config

from tweepy import API, OAuthHandler, Stream
from tweepy.streaming import StreamListener
from tweepy.error import TweepError
from rq import Queue
from worker import conn

q = Queue(connection=conn)

auth = OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
client = API(auth)

topics_to_track = [t for t in config.get('track').get('topics')]


class Listener(StreamListener):
    
    def on_status(self, status):
        '''
        Enqueues tweets to be processed
        '''
        print(u'{1} (https://twitter.com/{0}/status/{2}) - @{0}'.format(
            status.user.screen_name,
            status.text[:20] + '...' if len(status.text) > 10 else status.text,
            status.id_str
        ))
    
    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            return False


if __name__ == '__main__':
    listener = Listener()
    stream = Stream(auth=client.auth, listener=listener)
    stream.filter(track=topics_to_track, async=True)
