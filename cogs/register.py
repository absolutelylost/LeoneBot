from discord import channel
from discord.ext import commands
from discord.ext.commands import bot, cog

class registerCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    #@commands.Cog.listener()
    @commands.command(name= 'register', aliases= ['registering', 'reg'])
    async def register(self, ctx, *, course):# self is instance of class
        
        await ctx.channel.send(f'pong!')

def setup(bot):#required
    bot.add_cog(registerCommand(bot))

