import praw
import configparser

config = configparser.ConfigParser()
config.read('token.ini')

reddit = praw.Reddit(client_id=config['reddit']['client_id'],
                     client_secret=config['reddit']['client_secret'],
                     username=config['reddit']['username'],
                     password=config['reddit']['password'],
                     user_agent='console:h_enta_i(join):For my own bot account')

# Open the text file
with open('clean_subreddits.txt', 'r') as f:
    # Read each line of the file
    for line in f:
        # Strip the leading and trailing whitespace from the line
        subreddit_name = line.strip()
        # Check if the line is a subreddit name in the format of r/subreddit
        if subreddit_name.startswith('r/'):
            # Get the subreddit object
            subreddit = reddit.subreddit(subreddit_name[2:])
            # Join the subreddit
            try:
                subreddit.subscribe()
            except:
                print(f'Failed to join subreddit {subreddit.display_name}')
            print(f'Joined subreddit {subreddit.display_name}')
