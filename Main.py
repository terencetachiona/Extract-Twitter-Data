import sys
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main():

	def printTweet(descr, t):
		print(descr)
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Text: %s" % t.text)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)

	# Example 1 - Get tweets by username
	tweetCriteria = got.manager.TweetCriteria().setUsername('econet_support').setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]		

	printTweet("### Example 1 - Get tweets by username [econet_support]", tweet)

	# Example 2 - Get tweets by query search
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch('ecocash').setSince("2019-04-01").setUntil("2015-06-14").setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	printTweet("### Example 2 - Get tweets by query search [ecocash]", tweet)

	# Example 3 - Get tweets by username and bound dates
	tweetCriteria = got.manager.TweetCriteria().setUsername("econet_support").setSince("2019-03-01").setUntil("2015-06-14").setMaxTweets(1)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

	printTweet("### Example 3 - Get tweets by username and bound dates [econet_support, '2019-03-01', '2015-06-14']", tweet)

if __name__ == '__main__':
	main()
