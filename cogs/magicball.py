from discord import channel
from discord.ext import commands
from discord.ext.commands import bot, cog
import random

class magicballCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'magicball', aliases= ['8ball', 'magic8ball', 'fortuneball'] )
    async def magicball(self, ctx, * , question):
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
    bot.add_cog(magicballCommand(bot))

