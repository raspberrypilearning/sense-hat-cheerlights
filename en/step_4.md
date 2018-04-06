## Cheerlights

1. Click the **Load** button and browse to the `cheerlights` folder in the home folder, and open the `cheerlights.py` file.

1. The starter code simply prints out the tweet contents. Press the **Run** button and get someone to tweet `#cheerlights red` – and you should see the word 'red' in the output.

1. Modify the `on_success` method in the `CheerlightsStreamer` class to set the Sense HAT LEDs to the tweeted colour:

    ```python
    def on_success(self, data):
        if 'text' in data:
            tweet = data['text'].replace(hashtag, '')
            color_text = tweet.strip()
            color = Color(color_text)
    	      sense.clear(color.rgb_bytes)
    ```

1. Try tweeting different colour names to test it out!

1. You might notice that some colour names you try don't work – and this can cause the program to crash. Add an exception handler to deal with this, and let you know when there's an error:

    ```python
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
    ```
