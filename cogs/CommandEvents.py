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
        
    @commands.command()
    async def echo(self, ctx, arg):
        await ctx.channel.send(arg)


def setup(bot):#required
    bot.add_cog(CommandEvents(bot))

