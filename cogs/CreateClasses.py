# from discord import channel, Client
from discord.ext import commands
from discord.ext.commands import bot, cog
import discord


class createClassCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'create_classes', aliases= ['createclasses'])

    async def create_classes(self, ctx,  course): #member: discord.Member: self is instance of class

        #retrieve ids for channels on server
        category = discord.utils.get(ctx.guild.categories, name= 'classes')
        sections = ['eml3022-song', 'eml3034-kassab', 'eml3101-peles',]
        
        if category is None:
            await ctx.channel.send('No classes exist.\n')

        else:
            for section in sections:
                # print("made it here")
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages= False), 
                }
                await ctx.guild.create_text_channel(section, overwrites=overwrites)
        
        await ctx.channel.send('channels have been created for classes {}'.format(sections))

        #new_channel = self.bot.get_channel(channel_id)
        # member = ctx.message.author
        # await member.move_to(new_channel) # only works for voice channels
        
        #await ctx.channel.send('Member have been registered')

def setup(bot):#required
    bot.add_cog(createClassCommand(bot))


# check documentation on kick and class discord.ExpireBehavior
