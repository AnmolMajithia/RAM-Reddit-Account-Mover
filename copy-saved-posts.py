import requests
import sys

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
        sys.exit('Authentication Error, exiting...')
    
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

# Fetch list of saved posts from old account

print('Fetching saved posts...')

saved = []

res3 = requests.get('https://oauth.reddit.com/user/'+usr1+'/saved',
                   headers=headers_from, params = {'limit':'100'})
count = 100

while res3.json()['data']['dist'] != 0:
    
    for post in res3.json()['data']['children']:
        saved.append(post['data']['name'])
        
    res3 = requests.get('https://oauth.reddit.com/user/'+usr1+'/saved',
                        headers=headers_from, params = {'after':saved[-1],
                                                        'limit':'100'})
    
    if res3.json()['data']['dist'] != 0:
        print('Fetched',count,'saved posts')
        count += 100
        
total = len(saved)
print('Finished fetching',total,'saved posts')

# Save fetched posts to new account

def save(name):
    res = requests.post('https://oauth.reddit.com/api/save/',
                        headers = headers_to, params = {'id':name})
    if res.status_code != 200:
        return -1

fails = 0
print('\nSaving posts to new account...')
count = 1
for post in saved:
    print('('+str(count)+'/'+str(total)+')',end='\r')
    result = save(post)
    if result == -1:
        fails += 1
    count += 1
        
if fails != 0:
    print(str(fails)+" items failed to save, probably because they belonged to quarantined communities or the original post has been deleted")
        
print('\n\n\n     SUCCESS!!!')