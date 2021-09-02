# from discord import channel, Client
from discord.ext import commands
from discord.ext.commands import bot, cog
import discord


class registerCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'register', aliases= ['registering', 'reg'])
    #async def register(self, ctx, *, course):# self is instance of class
    async def register(ctx, member : discord.Member, channel: discord.channel):# self is instance of class

        class_one = 882265290153525310
        class_two = 882265353332350996
        channel_id = 882265290153525310
        member = discord.Member
        # if course == 'class_one':
        #     channel_id = class_one
        # elif course == 'class_two':
        #     channel_id = class_two

        # dest_channel = Client.get_channel(id= channel_id, self=self)
        # member = ctx.message.author
        await member.move_to(channel)
        await ctx.channel.send('Member have been registered')

def setup(bot):#required
    bot.add_cog(registerCommand(bot))

