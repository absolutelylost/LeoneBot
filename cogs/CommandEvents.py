from discord import channel
from discord.ext import commands
from discord.ext.commands import bot, cog
import random

class CommandEvents(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    #@commands.Cog.listener()
    @commands.command()
    async def ping(self, ctx):# self is instance of class
        await ctx.channel.send(f'pong!')


    @commands.Cog.listener()
        #aliases= ['8ball', 'eightball'])
    async def _8ball(self, ctx, * , question):
        responses= [
            "It is Certain.", 
            "It is decidedly so.", 
            "Without a doubt", 
            "Yes definitely", 
            "Without a doubt.", 
            "You may rely on it",
            "As I see it, yes.", 
            "Most likely.", 
            "Outlook good.", 
            "Yes.", 
            "Signs point to yes.", 
            "Reply hazy, try again.", 
            "Ask again later.", 
            "Better not tell you now.", 
            "Cannot predict now.", 
            "Concentrate and ask again.", 
            "Don't count on it.", 
            "My reply is no.", 
            "My sources say no.", 
            "Outlook not so good.", 
            "Very doubtful."
            ]
        await ctx.channel.send(f'Question: {question}\nAnswer: {random.choice(responses)}')



def setup(bot):#required
    bot.add_cog(CommandEvents(bot))

