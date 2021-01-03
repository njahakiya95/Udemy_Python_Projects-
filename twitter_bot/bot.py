import tweepy

#Tweepy authoization codes and tokens
auth = tweepy.OAuthHandler('eZHntR2D0Sc1gVkuD16fHntqA', 'J7lOeKmBHTwGVyJVvEFCZDXt4MTYNy47jk2KYa5qLZlGmrJ7Vn')
auth.set_access_token('1336511702922301440-gATGxJ1t6y5sYD54bqgson00H5dRJX', 'IuzkS2G2XDQfQU9AJr16XEcO5ykFY7y7NBuVMkmyM4ahs')

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