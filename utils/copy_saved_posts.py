def fetch_saved_posts(headers_from, usr1):
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
    
    print('Finished fetching', len(saved), 'saved posts')

    return saved

def save(name, headers_to):
    res = requests.post('https://oauth.reddit.com/api/save/',
                        headers = headers_to, params = {'id':name})
    if res.status_code != 200:
        return -1

def autosaver(saved, headers_to):
    fails = 0
    print('\nSaving posts to new account...')
    count = 1
    total = len(saved)
    for post in saved:
        print('('+str(count)+'/'+str(total)+')',end='\r')
        result = save(post, headers_to)
        if result == -1:
            fails += 1
        count += 1
            
    if fails != 0:
        print(str(fails)+" items failed to save, probably because they belonged to quarantined communities or the original post has been deleted")

if __name__ == '__main__':
    import requests
    import sys
    from copy_subscription import logincaller, print_readme
    print_readme()
    login_details = logincaller()
    autosaver(fetch_saved_posts(login_details[0], login_details[2]), login_details[1])
    print('\n\n\n     SUCCESS!!!')
