import praw

# Replace the placeholders with your Reddit account credentials
import configparser
config = configparser.ConfigParser()
config.read('token.ini')

reddit = praw.Reddit(client_id=config['reddit']['client_id'],
                     client_secret=config['reddit']['client_secret'],
                     username=config['reddit']['username'],
                     password=config['reddit']['password'],
                     user_agent='console:h_enta_i(fetch):For my own bot account')

# Get top 50 posts from my home front page (https://www.reddit.com/top?t=all)
submissions = list(reddit.front.top(
    limit=50)) + list(reddit.subreddit("hentai").top(limit=50))

# Write URLs to file
with open('URLs.txt', 'r') as f:
    urls: list[str] = f.read().splitlines()
with open('URLs.txt', 'w') as f:
    for line in urls:
        f.write(line + "\n")
    for post in submissions:
        link = reddit.config.reddit_url + post.permalink
        if link not in urls:
            urls.append(link)
            f.write(link + "\n")
            print(link)
