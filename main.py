import discord

client = discord.Client()

@client.event# register event

#uses callbacks
async def on_ready():
    print('{0.user} is logged in !'.format(client))

