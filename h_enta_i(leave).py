import praw

# Replace the placeholders with your Reddit account credentials
import configparser
config = configparser.ConfigParser()
config.read('token.ini')

reddit = praw.Reddit(client_id=config['reddit']['client_id'],
                     client_secret=config['reddit']['client_secret'],
                     username=config['reddit']['username'],
                     password=config['reddit']['password'],
                     user_agent='console:h_enta_i(leave):For my own bot account')

# Get a list of all the subreddits that the user is subscribed to
subscribed_subreddits = reddit.user.subreddits()

# Leave all the subreddits that are not in English
for subreddit in subscribed_subreddits:
    if subreddit.lang != 'en':
        print("Leaving " + subreddit.display_name)
        subreddit.unsubscribe()
