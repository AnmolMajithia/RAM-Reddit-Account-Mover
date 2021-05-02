# Reddit Account Mover

### DEVELOPMENT UNDER PROGRESS

Once completed, this should be able to relatively easily move all your subscriptions and saved posts from one user account to the other.
Maybe more if I get better ideas or you demand for something.

## What Works :
- [x] Subscription copying from one account to the other
- [x] Saved Posts copying
- [ ] Optional: make old accounts upvoted posts as new accounts saved posts
- [ ] Optional: Delete all posts and comments of old account
- [ ] Single Script to integrate all functions

## Steps :
Let me know if I should make an android app later which would make this much easier.
Trying to make instructions noob friendly for non programmer redditors.

- ### Universal Steps:

- Login to [reddit.com](https://www.reddit.com/) with any one of the two accounts
- Go to [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
- Scroll to the bottom and select "create app" option
  1. Enter any name you want
  2. Select script
  3. Description optional
  4. Click on create app
- In the new box that just formed:
  1. On the right part of the box, click in the add developer text field and enter the username of the other account, hit enter.
  2. The word below "personal use script" is your **Client ID**, you will need to copy paste it into the program when asked
  3. The word written next to "secret" is your **Secret** (duh), you will need to copy paste it into the program when asked
- Clone my repository (or download zip and extract)
- Install [python](https://www.python.org/downloads/) if not already installed

*Captain Obvious: You need a working net connection to run this program, program does take time to run based on your number of subscriptions but I have made my best efforts to show progress while its going on so if you hit enter and nothing happens, just give it a minute, could be slow connection issues*

1. ### Copy Subscriptions:

- Open folder and click on copy-subscription.py and select execute if it does not automatically run
- If above step does not work, open the current directory in console/terminal/command prompt/powershell and type:
```python copy-subscription.py```
- Follow instructions on the screen and done!

2. ### Copy Saved Posts:
- Open folder and click on copy-saved-posts.py and select execute if it does not automatically run
- If above step does not work, open the current directory in console/terminal/command prompt/powershell and type:
```python copy-saved-posts.py```
- Follow instructions on the screen and done!