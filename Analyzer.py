import tweepy

import io

import re

from textblob import TextBlob

class Twitter:

    def __init__(self):

        #Initialising tweepy library and authenticating with twitter using access_keys

        consumer_key = 'yec9qqb5GixrrBngG4TLKJ08x'

        consumer_secret = '4h8mkItWDuuhSQ1EP6VzIZHzq4izXqct0uLallmqiITDAWgs8V'

        access_token = '1194890338030145537-IH55wQR197CzpaJP9LOKYvk15s2tks'

        access_token_secret = 'jwffR5EmK2OQu9v21aaSe0Z8bCYtY6Vet3XiA9nPZ5F1U'

        try:

            self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

            self.auth.set_access_token(access_token, access_token_secret)

            self.api = tweepy.API(self.auth)

            print("Authentication Complete!")

        except:

            print("Error: Authentication Failed")

           

    def get_tweet(self,query,count=100):

       

        self.analysis=list()

        file=io.open("tweets.txt", "w", encoding="utf-8")

        for tweet in tweepy.Cursor(self.api.search, q=query).items(count):

            m=self.clean_tweet(tweet.text)

            file.write(m)

            self.analysis.append(self.get_tweet_sentiment(m))

        file.close()

        print("Written to tweets.txt")

        return self.analysis

 

 

    def clean_tweet(self, tweet):

            

        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

   

    def get_tweet_sentiment(self, tweet):

        analysis = TextBlob(tweet)

        if analysis.sentiment.polarity > 0:

            return 'positive'

        elif analysis.sentiment.polarity == 0:

            return 'neutral'

        else:

            return 'negative'

   

    

twitter=Twitter()

g=twitter.get_tweet(input("Enter Keyword \n"))

print("Positive: ",g.count('positive'),"Percent")

print("Negative: ",g.count('negative'),"Percent")

print("Neutral: ",g.count('neutral'),"Percent")
