import re

# Open subreddits.txt
with open('subreddits.txt', 'r') as f:
    text = f.read()

# match all subreddit using regex
subreddits = re.findall(r'\b(r/\w+)\b', text)

# record back to clean_subreddits.txt
with open('clean_subreddits.txt', 'w') as f:
    for subreddit in subreddits:
        f.write(subreddit + "\n")
