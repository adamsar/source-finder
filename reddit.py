import praw

import feedfinder

reddit_agent = praw.Reddit(user_agent="daedalus")

domains = set(
    [submission.domain for submission in \
     reddit_agent.get_subreddit('programming').get_hot(limit=50)]
    )
for domain in domains:
    print str(feedfinder.getFeeds(domain))
