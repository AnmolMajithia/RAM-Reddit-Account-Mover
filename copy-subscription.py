import requests
import sys

print('''READ ME:

    Follow the steps given on my repository before running this script
    
    Ensure you have Client ID and Secret with you.

    To paste in console use Ctrl+Shift+V

    Old Account = Account to move from
    New Account = Account to move to''')

input("\nPress enter to get started...\n")

def login(auth, usrnm, pw):
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth = auth,
                        data = {'grant_type': 'password',
                                'username': usrnm,
                                'password': pw}, 
                        headers = headers)
    if res.status_code == 200:
        TOKEN = res.json()['access_token']
        headers['Authorization'] = f'bearer {TOKEN}'
    else:
        sys.exit('\n\nAuthentication Error, exiting...')
    
    return headers

CLIENT_ID = input("Enter Client ID: ")
SECRET_KEY = input("Enter Secret: ")

usr1 = input("\nEnter username of old account: ")
ps1 = input("Enter password of old account: ")

usr2 = input("\nEnter username of new account: ")
ps2 = input("Enter password of new account: ")

print("Authenticating...", end="")

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

headers_from = login(auth, usr1, ps1)
headers_to = login(auth, usr2, ps2)

print('success!\n')

# Fetch list of subreddits from old account

print('Fetching list of subreddits from old account...')

subreddits = []

res3 = requests.get('https://oauth.reddit.com/subreddits/mine/subscriber',
                   headers=headers_from, params = {'limit':'100'})
count = 100

while res3.json()['data']['dist'] != 0:
    
    for post in res3.json()['data']['children']:
        subreddits.append((post['data']['name'], post['data']['url']))
        
    res3 = requests.get('https://oauth.reddit.com/subreddits/mine/subscriber',
                        headers=headers_from, params = {'after':subreddits[-1][0],
                                                        'limit':'100'})
    
    if res3.json()['data']['dist'] != 0:
        print('Fetched',count,'subreddits')
        count += 100
        
total = len(subreddits)
print('Finished fetching',total,'subreddits')


subreddits = sorted(subreddits, key = lambda x: x[1])


# Subscribe subreddits to new account


def subscribe(name):
    res = requests.post('https://oauth.reddit.com/api/subscribe/',
                        headers = headers_to, params = {'skip_initial_defaults':'True',
                                                       'action':'sub',
                                                       'sr':name})
    if res.status_code != 200:
        return -1


fails = []
print('\n\nSubscribing to:')
count = 1
for subreddit in subreddits:
    print('('+str(count)+'/'+str(total)+')'+' '+subreddit[1]+"...",end='')
    result = subscribe(subreddit[0])
    if result == -1:
        print('failed')
        fails.append(subreddit[1])
    else:
        print('success')
    count += 1
        
if len(fails) != 0:
    
    f = open('fails.txt','w')
    wr='\n'.join(fails)
    f.write(wr)
    f.close()
    
    print('''Some of the subreddits failed to subscribe
    The reason could be the subreddit being quarantined, private, inaccessible, deleted, network failure or something else.
    A text file "fails.txt" has been created which has the list of all the fails.
    The list is also printed below:''')
    
    for fail in fails:
        print(fail)
        
print('\n\n\n     SUCCESS!!!')