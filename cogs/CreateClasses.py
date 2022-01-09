# from discord import channel, Client
from discord.ext import commands
from discord.ext.commands import bot, cog
import discord
from Data import class_parser as cp


class createClassCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'create_classes', aliases= ['createclasses'])

    async def create_classes(self, ctx): #member: discord.Member: self is instance of class

        #retrieve ids for channels on server
        category = discord.utils.get(ctx.guild.categories, name= 'classes')
        sections = cp.class_parser().parse()
        # ['eml3022-song', 'eml3034-kassab', 'eml3101-peles',]
        
        if category is None:
            await ctx.channel.send('No classes exist.\n')

        else:
            for section in sections:

                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages= False), 
                }
                await ctx.guild.create_text_channel(section, overwrites=overwrites, category=category)
            await ctx.channel.send('channels have been created for classes {}'.format(sections))

def setup(bot):#required
    bot.add_cog(createClassCommand(bot))
