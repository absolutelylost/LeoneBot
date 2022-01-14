# from discord import channel, Client
from discord.ext import commands
from discord.ext.commands import bot, cog
import discord


class registerCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'register', aliases= ['join', 'registering', 'reg'])
    #async def register(self, ctx, *, course):# self is instance of class
    async def register(self, ctx,  course): #member: discord.Member: self is instance of class

        #retrieve ids for channels on server
        all_channels = discord.utils.get(ctx.guild.channels)
        # print(category.channels)
        
        #initalize variable to confirm reception of course
        found = False
        
        if all_channels is None:
            await ctx.channel.send('No classes exist.\n')

        else:
            for channel in all_channels:
                print(channel.name)
                print(course)
                if channel.name == course:
                    
                    found = True
                    
                    await channel.set_permissions(ctx.author, read_messages=True,
                                                        send_messages=True)
        if(found):
            await ctx.channel.send('@{} has been registered.'.format(ctx.message.author))
        else: 
            await ctx.channel.send('This class does not exist. Please check your input again or message a mod if you believe there is an error.\n')

def setup(bot):#required
    bot.add_cog(registerCommand(bot))

# check documentation on kick and class discord.ExpireBehavior
