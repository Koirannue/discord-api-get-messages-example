import requests
import time

DISCORD_TOKEN = ''
CHANNEL_ID = ''
AMOUNT = 1500

discord = requests.Session()
discord.headers.update({'Authorization': DISCORD_TOKEN})

DISCORD_API = 'https://discordapp.com/api'
URL = DISCORD_API + '/channels/' + CHANNEL_ID + '/messages'
print('trying')
resps = discord.get(URL + '?limit=1').json()
print('got')
data = []
data.append('id, timestamp, author, content')
for r in resps:
    data.append(r['id'] + ',' + r['timestamp'] + ',"' + r['author']['username'] + '","' + r['content'] + '"')
AMOUNT -= 1
LAST_ID = r['id']
while AMOUNT > 0:
    n = 100 if AMOUNT >= 100 else AMOUNT
    resps = discord.get(URL + '?before={}&limit={}'.format(LAST_ID, n)).json()
    for r in resps:
        data.append(r['id'] + ',' + r['timestamp'] + ',"' + r['author']['username'] + '","' + r['content'] + '"')
        LAST_ID = r['id']
    AMOUNT -= n
    if AMOUNT == 0:
        break
    print(str(AMOUNT) + ' left to go')
    time.sleep(10)
with open('test.csv', 'w', encoding='UTF-8') as f:
    f.write('\n'.join(data))
print('done')