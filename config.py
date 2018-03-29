import tweepy

# Twitter API Keys
consumer_key = "iPKHoyiWwRyMfzeLZuPfgGoL6"
consumer_secret = "KBUiawudLBDWWZlDYzhB7cqs4K6HVuotTIXaaiiB73Jz02HE1j"
access_token = "974883030681571328-CMOGKv7yNYMRK8T4ox5L5iCt3r4Zl43"
access_token_secret = "TxG3qZZuI6Q1f6o6unIMDcs6wdoUZuiZwrt2w3BDY4Ot0"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
