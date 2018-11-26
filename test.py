import tweepy, time, datetime

consumer_key = "bQDnixR5ylKP9BmmRgcAIhEZR"
consumer_secret = "NK6MReRROxR9g7RZngfzQdjL2HllyLsFs18o8BPbqp0rMKZbvV"
access_token = "1022913483531329538-HulI8TPquoPqdpbNaWuzpzkAxwFkzk"
access_token_secret = "QsbgUflXJOoFcV3wbidSL6osO1rhcb5Zd0jqERH0D51z4"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
    while True:
        print (time.asctime(time.localtime(time.time())) + " ---------- STARTING ITERATION... ----------")
        numberOfTweets = 9
        timeUntilNextBatch = 360
        for tweet in tweepy.Cursor(api.search, "giveaway retweet -filter:retweets").items(numberOfTweets):
            try:
                # Retweet and Like Tweet
                tweet.retweet()
                tweet.favorite()

                print(time.asctime(time.localtime(time.time())) + " Tweet Retweeted and Liked")

                # Follow User if Needed
                if "follow" in tweet.text or "#follow" in tweet.text or "Follow" in tweet.text or "#Follow" in tweet.text or "FOLLOW" in tweet.text or "#FOLLOW" in tweet.text or "following" in tweet.text or "#following" in tweet.text or "FOLLOWING" in tweet.text or "#FOLLOWING" or "Following" in tweet.text or "#Following" in tweet.text:
                    user_id = tweet.user.id
                    api.create_friendship(user_id)
                    print(time.asctime(time.localtime(time.time())) + " Followed")

            except tweepy.TweepError as e:
                print(time.asctime(time.localtime(time.time())) + " " + e.reason)
            except StopIteration:
                break
        print(time.asctime(time.localtime(time.time())) + " ---------- ITERATION SUCCESSFUL ----------")
        time.sleep(timeUntilNextBatch)


main()