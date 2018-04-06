from twython import TwythonStreamer
from sense_emu import SenseHat
from colorzero import Color
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

sense = SenseHat()

hashtag = '#cheerlights'

class CheerlightsStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            tweet = data['text']
            tweet = tweet.replace(hashtag, '')
            color_text = tweet.strip()
            try:
                color = Color(color_text)
                sense.clear(color.rgb_bytes)
            except ValueError:
                print('Failed: {}'.format(color_text))

stream = CheerlightsStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track=hashtag)
