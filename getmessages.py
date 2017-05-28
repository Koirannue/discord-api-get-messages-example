import requests
import time
import sys

'''USAGE: filename.py "YOUR TOKEN" "Channel ID" "number of messages"'''

DISCORD_TOKEN = sys.argv[1]
CHANNEL_ID = sys.argv[2]
AMOUNT = int(sys.argv[3])

discord = requests.Session()
discord.headers.update({'Authorization': DISCORD_TOKEN})

DISCORD_API = 'https://discordapp.com/api'
URL = DISCORD_API + '/channels/' + CHANNEL_ID + '/messages'
n = 100 if AMOUNT >= 100 else AMOUNT
resps = discord.get(URL + '?limit={}'.format(n)).json()
data = []
data.append('id, timestamp, author, content')
for r in resps:
    data.append(r['id'] + ',' + r['timestamp'] + ',"' + r['author']['username'] + '","' + r['content'] + '"')
    LAST_ID = r['id']
AMOUNT -= n
while AMOUNT > 0:
    print(str(AMOUNT) + ' left to go')
    time.sleep(2)
    n = 100 if AMOUNT >= 100 else AMOUNT
    resps = discord.get(URL + '?before={}&limit={}'.format(LAST_ID, n)).json()
    for r in resps:
        data.append(r['id'] + ',' + r['timestamp'] + ',"' + r['author']['username'] + '","' + r['content'] + '"')
        LAST_ID = r['id']
    AMOUNT -= n
with open('last {} messages in {}.csv'.format(sys.argv[3], sys.argv[2]), 'w', encoding='UTF-8') as f:
    f.write('\n'.join(data))
print('done')