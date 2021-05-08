# RAM - Reddit Account Mover

### DEVELOPMENT UNDER PROGRESS

Once completed, this should be able to relatively easily move all your subscriptions and saved posts from one user account to the other.
Maybe more if I get better ideas or you demand for something.

## What Works :
- [x] Subscription copying from one account to the other
- [x] Saved Posts copying
- [ ] Optional: make old accounts upvoted posts as new accounts saved posts
- [ ] Optional: Delete all posts and comments of old account
- [x] Single Script to integrate all working functions

## Steps :
Let me know if I should make an android app later which would make this much easier.

  - Login to [reddit.com](https://www.reddit.com/) with old account
  - Go to [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
  - Scroll to the bottom and select "create app" option
    1. Enter any name you want
    2. Select script
    3. Click on create app
  - In the new box that just formed:
    1. Click in the add developer text field and enter username of new account.
    2. The word below "personal use script" is your **Client ID**
    3. The word written next to "secret" is your **Secret Key**, you will need these both.
  - Clone my repository (or download zip and extract)
  - Install [python](https://www.python.org/downloads/) if not already installed
  - Run ```main.py``` or open extracted folder in terminal and type
  ```python3 main.py```
  - Follow instructions on screen :)

*Captain Obvious: You need a working net connection to run this program, program does take time to run based on your number of subscriptions but I have made my best efforts to show progress while its going on to help your anxiety. So if you hit enter and nothing happens, just give it a minute, could be slow connection issues*