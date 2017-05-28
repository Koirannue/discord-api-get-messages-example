import requests
import time
import datetime

DISCORD_TOKEN = ''
CHANNEL_ID = ''

discord = requests.Session()
discord.headers.update({'Authorization': DISCORD_TOKEN})

DISCORDAPI = 'https://discordapp.com/api'
print('trying')
resps = discord.get(DISCORDAPI + '/channels/' + CHANNEL_ID + '/messages').json()
print('got')
with open('test.csv', 'w', encoding='UTF-8') as f:
    for resp in resps:
        f.write(resp['timestamp'] + ',"' + resp['author']['username'] + '","' + resp['content'] + '"\n')
print('done')