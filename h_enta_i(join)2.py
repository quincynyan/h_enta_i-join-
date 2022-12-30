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


# Search for all subreddits whose name includes the keyword
def search_subreddits(keyword):
    print("*" * 50)

    subreddit_names1 = [
        subreddit.display_name for subreddit in reddit.subreddits.search(keyword, limit=None)]

    # Search for all subreddits whose name starts with the keyword
    subreddit_names2 = [
        subreddit.display_name for subreddit in reddit.subreddits.search_by_name(keyword, exact=False, include_nsfw=True)]

    # Search for all subreddits whose name ends with the keyword
    try:
        subreddit_names3 = [
            subreddit.display_name for subreddit in reddit.subreddits.search_by_name(keyword, exact=True, include_nsfw=True)]
    except:
        subreddit_names3 = []

    # Combine the results from the three searches using union
    subreddit_names = set(subreddit_names1).union(
        set(subreddit_names2)).union(set(subreddit_names3))

    print("All subreddits that contain the keyword:")
    print(subreddit_names)
    print(len(subreddit_names))

    print("=====================================================")

    # Get a list of all the subreddits that the user is subscribed to
    subscribed_subreddits = list(reddit.user.subreddits(limit=None))
    print("All subreddits that the user is subscribed to:")
    print(subscribed_subreddits)
    print(len(subscribed_subreddits))
    print("=====================================================")

    # Get a list of all the subreddits that the user is not subscribed to
    unsubscribed_subreddits = [
        x for x in subreddit_names if x not in subscribed_subreddits]

    print("All subreddits that the user is not subscribed to:")
    print(unsubscribed_subreddits)
    print(len(unsubscribed_subreddits))
    print("=====================================================")

    return unsubscribed_subreddits


hentai = search_subreddits('hentai')
rule34 = search_subreddits('rule_34')
rule_34 = search_subreddits('rule_34')
r34 = search_subreddits('r34')
ru34 = search_subreddits('rule 34')

# Join all the subreddits in the list using union
subreddits = set(hentai).union(set(rule34)).union(
    set(rule_34)).union(set(r34)).union(set(ru34))

print("*" * 50)
print("All subreddits that the user is going to join:")
print(subreddits)
print(len(subreddits))
print("=====================================================")

# # If subreddit name doesn't contain the keywords, remove it from the list
# sr = list(subreddits)
# for subreddit in sr:
#     if 'hentai' not in subreddit.lower() and 'rule_34' not in subreddit.lower() and 'rule34' not in subreddit.lower() and 'r34' not in subreddit.lower() and 'rule 34' not in subreddit.lower():
#         subreddits.remove(subreddit)

# If subreddit description doesn't contain the keywords, remove it from the list
sr = list(subreddits)
for subreddit in sr:
    try:
        subreddit = reddit.subreddit(subreddit)
        if 'hentai' not in subreddit.public_description.lower() and 'rule_34' not in subreddit.public_description.lower() and 'rule34' not in subreddit.public_description.lower() and 'r34' not in subreddit.public_description.lower() and 'rule 34' not in subreddit.public_description.lower():
            subreddits.remove(subreddit.display_name)
    except Forbidden:
        print("Forbidden to access " + subreddit.display_name)
    except Exception as e:
        print("Failed to access " + subreddit.display_name)
        print(e)

print("\n")
print()
print("*" * 50)
print("=====================================================")
print("All subreddits that the user is not subscribed to and contain the keywords:")
print(subreddits)
print(len(subreddits))

# Join all the subreddits in the list
for subreddit_name in subreddits:
    try:
        subreddit = reddit.subreddit(subreddit_name)
        print("Joining " + subreddit_name)
        subreddit.subscribe()
    except:
        print("Failed to join " + subreddit_name)
