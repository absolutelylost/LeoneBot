import discord
from discord.ext import commands, tasks
from Data import config
import requests # make http requests and returns .json files
import json
import random, os


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

# class Client(discord.Client):
#     async def on_ready(self):
#         print('{0} is logged in !'.format(self.user))
#     async def on_message(self, message):
#         if(message.author == self.user):
#             return
#         if(message.content.startswith(config.prefix)):
#             return

#         if(message.content.startswith(config.prefix+'hi' or config.prefix+'hello')):
#             await message.channel.send('Hello there!')
#         if(message.content.startswith(config.prefix + 'inspire')):
#             await message.channel.send(get_quote())

#@commands.command()
#async def test(ctx):
#    pass

#client = Client()
client = commands.Bot(command_prefix= config.prefix)

@client.event
async def on_ready():
    print('LeoneBot is logged in !')

extensions= os.listdir('cogs')

print(extensions)


if __name__ == '__main__':
    for ext in extensions:
        if '.py' in ext:
            client.load_extension('cogs.'+ ext.removesuffix('.py'))

# extensions = 'cogs.CommandEvents'

# if __name__ == '__main__':
#     for ext in extensions:
#         client.load_extension(ext)


client.run(config.token)