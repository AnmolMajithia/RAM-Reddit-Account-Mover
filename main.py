import requests
import sys

from copy_subscription import print_readme, logincaller, fetch_subscribed_subreddits, autosubscriber
from copy_saved_posts import fetch_saved_posts, autosaver

if __name__ == '__main__':
    print_readme()
    login_details = logincaller()

    c = input("""Please Choose:
    1 : Copy Subscriptions as well as Saved Posts from Old to New Account
    2 : Copy only Subscriptions
    3 : Copy only Saved Posts
    Enter anything else to quit\n""")

    if c == '1':
        autosubscriber(fetch_subscribed_subreddits(login_details[0]), login_details[1])
        autosaver(fetch_saved_posts(login_details[0], login_details[2]), login_details[1])
        
    elif c == '2':
        autosubscriber(fetch_subscribed_subreddits(login_details[0]), login_details[1])

    elif c == '3':
        autosaver(fetch_saved_posts(login_details[0], login_details[2]), login_details[1])

    else:
        sys.exit("\n\nExiting...\n")

    print('\n\n\n     SUCCESS!!!')
