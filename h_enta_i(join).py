import praw
from prawcore.exceptions import Forbidden

# Replace the placeholders with your Reddit account credentials
import configparser
config = configparser.ConfigParser()
config.read('token.ini')

reddit = praw.Reddit(client_id=config['reddit']['client_id'],
                     client_secret=config['reddit']['client_secret'],
                     username=config['reddit']['username'],
                     password=config['reddit']['password'],
                     user_agent='console:h_enta_i(join):For my own bot account')

# Set the keyword you want to search for
keyword = 'rule_34'

# Find all the subreddits whose name includes the keyword
subreddit_names = [
    subreddit.display_name for subreddit in reddit.subreddits.search(keyword, limit=None)]

# Join all the subreddits in the list
for subreddit_name in subreddit_names:
    try:
        subreddit = reddit.subreddit(subreddit_name)
        print("Joining " + subreddit_name)
        subreddit.subscribe()
    except Forbidden:
        print("Forbidden to join " + subreddit_name)
    except:
        print("Failed to join " + subreddit_name)
