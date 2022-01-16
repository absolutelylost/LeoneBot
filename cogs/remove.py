# from discord import channel, Client
from discord.ext import commands
from discord.ext.commands import bot, cog
import discord
from discord.ext.commands.core import check
import asyncio
import os, sys
from Data import class_parser as cp

#remove users from all classes
class removeCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'remove_all', aliases= ['remove'])
    #async def remove(self, ctx, *):# self is instance of class
    async def remove(self, ctx): #member: discord.Member: self is instance of class
        if ctx.author.guild_permissions.administrator == True:

            asker = ctx.author
            channel = ctx.channel
        
            confirmation = await ctx.channel.send('Are you sure you want to remove all participants from all classes?')
            
            def check(m):
                return m.content in ['yes', 'y', 'no', 'n'] and m.channel == channel and m.author == asker
            try:
                msg = await self.bot.wait_for('message', check = check, timeout=30)
            except asyncio.TimeoutError:
                await channel.send('No timely response ... Issue command again if needed.')
                return  
            
            # if host replies yes then remove users
            if (msg.content.lower() == 'yes' or msg.content.lower() == 'y'):
                await channel.send('Ok I`ll handle that')
                #retrieve ids for channels on server
                
                # remove channels from server
                category = discord.utils.get(ctx.guild.categories, name= 'classes')
                files = os.listdir('Data/')
                await ctx.channel.send(files)
                for file in files:
                    if '.txt' in file:
                        sections = cp.class_parser().parse(file)
                        
                        # for guild in bot.guilds:
                        guild = ctx.guild
                        for channel in guild.text_channels:
                            if channel.name in sections:
                                await channel.delete(reason=None)                       
                        await ctx.channel.send('All class channels removed')
                        
                        
                # remove users from channels
                # category = discord.utils.get(ctx.guild.categories, name= 'classes')
                # for channel in category.channels:
                #     members = channel.members
                #     print(members)
                #     await channel.send('{}'.format(members.name))
                #     for member in members:
                #         await channel.set_permissions(member, read_messages=False,
                #                                             send_messages=False)
                
            else:
                await channel.send('Nevermind')
                return
            #retrieve ids for channels on server
            # category = discord.utils.get(ctx.guild.categories, name= 'classes')
            # print(category.channels)
            
            # found = False
            
            # if category is None:
            #     await ctx.channel.send('No classes exist.\n')
            # else:
            #     for channel in category.channels:
            #         print(channel.name)
            #         print(course)
            #         if channel.name == course:
            #             found = True
                    
            #             print("made it here")
                    
            #             await channel.set_permissions(ctx.author, read_messages=True,
            #                                                 send_messages=True)
            # if(found):
            #     await ctx.channel.send('@{} has been registered.'.format(ctx.message.author))
            # else: 
            #     await ctx.channel.send('This class does not exist. Please check your input again or message a mod if you believe there is an error.\n')
        else:
            await ctx.channel.send('You do not have permission for this command')

def setup(bot):#required
    bot.add_cog(removeCommand(bot))


# check documentation on kick and class discord.ExpireBehavior
