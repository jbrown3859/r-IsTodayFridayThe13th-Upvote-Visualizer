import matplotlib.pyplot as plt
import numpy as np
import pylab
import requests
import json
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': REDDIT_USERNAME, 'password': REDDIT_PASSWORD}
auth = requests.auth.HTTPBasicAuth(REDDIT_APP_ID, REDDIT_APP_SECRET)
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': REDDIT_APP_NAME},
		  auth=auth)
d = r.json()
print(d)
token = 'bearer ' + d['access_token']

base_url = 'https://oauth.reddit.com'
p = {'limit': 100} #limit is restricted to 100; use after and count params to get more
headers = {'Authorization': token, 'User-Agent': REDDIT_APP_NAME}
response = requests.get(base_url + '/r/IsTodayFridayThe13th/new', params=p, headers=headers)

daysago=[]
upslist=[]

for prox in range(0,100):
    print("Day ",prox,response.json()['data']['children'][prox]['data']['ups'])
    daysago+=[prox]
    upslist+=[response.json()['data']['children'][prox]['data']['ups']]

fig, ax = plt.subplots()
ax.set_xlabel('Daily Posts, Most recent towards Zero')
ax.set_ylabel('Upvotes')
ax.set_title('Upvotes of the Daily Question on r/IsTodayFridayThe13th over the past 100 days')
ax.bar(daysago,upslist)
pylab.show()
