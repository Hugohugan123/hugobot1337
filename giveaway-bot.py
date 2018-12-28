import tweepy, time

consumer_key = "xKek38hcWdBpIYcEuAOg0RiE3"
consumer_secret = "kEBQgfc0a7r3ytTAQU7fkgC2tTgiex1XZl0bWc2bpv9D3puN3M"
access_token = "1078434202314514432-Yz4CQizdOlq0lvUHEdEiPbi6xsIO7P"
access_token_secret = "rqa4VJwnx8khHIrjFGcjuOxfF8MqL8LhhKvSWYvqXYmq8"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
    while True:
        print (time.asctime(time.localtime(time.time())) + " ---------- STARTING ITERATION... ----------")

        # Unfollow if Exceeded Friends Limit
        friendsLimit = 5000
        followerCount = user.followers_count

        if followerCount > 5000:
            friendsLimit = int(followerCount * 1.1)

        friendsLimit -= 50
        friendsCount = user.friends_count
        
        print(time.asctime(time.localtime(time.time())) + " Following: " + str(friendsCount))
        print(time.asctime(time.localtime(time.time())) + " Follow Limit: " + str(friendsLimit))
        
        if friendsCount > friendsLimit:
            print(time.asctime(time.localtime(time.time())) + " Friend Limit Exceeded, Unfollowing...")
            i = 0
            for friend in tweepy.Cursor(api.friends_ids).items():
                api.destroy_friendship(friend)
                i += 1
                if i == 5:
                    i = 0
                    time.sleep(60)
                    
            print(time.asctime(time.localtime(time.time())) + " Successfully Unfollowed All Friends!")

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
