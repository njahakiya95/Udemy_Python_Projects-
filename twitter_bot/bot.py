import tweepy

#Tweepy authoization codes and tokens
auth = tweepy.OAuthHandler('')
auth.set_access_token('')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
	try:
		while (True):
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)

#Code for Narcisistic bot
search_string = 'congress'
numberOfTweets = 2
 
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print("I liked that tweet")
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
