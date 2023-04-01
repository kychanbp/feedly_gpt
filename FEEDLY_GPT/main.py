from feedly.api_client.session import FeedlySession
from feedly.api_client.stream import StreamOptions
from feedly.api_client.utils import setup_auth
import sys
from datetime import datetime

def get_feedly_feeds(category_name, end_date, date_delta):
    category = sess.user.user_categories.get(category_name)
    timstamp_ms = int(end_date.timestamp() * 1000) - date_delta * 24 * 60 * 60 * 1000 # get the timestamp in milliseconds

    # Docs for Stream API: https://developers.feedly.com/v3/streams/
    for article in category.stream_contents(options=StreamOptions(max_count=sys.maxsize, newer_than=timstamp_ms)):
        print(article['title'])

if __name__ == "__main__":
    setup_auth(overwrite=True)
    sess = FeedlySession()
    get_feedly_feeds('Newsletter', datetime.now(), 10)
