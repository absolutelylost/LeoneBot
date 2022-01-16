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
        def replace(text):
            name = "no name"
            if text == 'eas':
                name = 'Engineering: Aerospace'
            if text == 'egn':
                name = 'Engineering: General'
            if text == 'ema':
                name = 'Engineering: Materials'
            if text == 'eml':
                name = 'Engineering: Mechanical'
            if text == 'mac':
                name = 'Mathematics, Calculus, and PreCalculus'
            return name  
        
        if ctx.author.guild_permissions.administrator == True:
            list_of_categories = []
            list_of_prefix = []
            first_letters = ""
            category = None
            category2 = None
            # save attachment to server
            file = ctx.message.attachments[0].filename
            print(file)
            await ctx.message.attachments[0].save("Data/" + file)
            
            # parse contents of file to get classes
            sections = cp.class_parser().parse(file)
            length = len(sections)
            
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages= False), 
            }
            # pull prefix from sections of classes
            for section in sections:
                # await ctx.channel.send(section)
                # get first 3 characters
                first_letters = section[0:3]
                newName = replace(first_letters)
                
                if first_letters not in list_of_prefix:
                    # place new prefix into list
                    list_of_prefix.append(first_letters)
                    
                    category = await ctx.guild.create_category(newName)
                    if length > 49:
                        category2 = await ctx.guild.create_category(newName + " 2")
                        # list_of_categories.append(category2)
                        await category2.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
                
                    #place category info into list
                    list_of_categories.append(category)                    
                    await category.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
                
                #find category information based on prefix list of categories
                category = list_of_categories[list_of_prefix.index(first_letters)]
                
                # create text channel  based on section then place it in the correct category 
                if len(category.channels) < 49:
                    await ctx.guild.create_text_channel(section, overwrites=overwrites, category=category)
                else:
                    await ctx.guild.create_text_channel(section, overwrites=overwrites, category=category2)
                    
            await ctx.channel.send('channels have been created for classes {}'.format(sections))
        
        else:
             await ctx.channel.send('You do not have permission for this command')                
            
            
            # await ctx.message.attachments[0].save("Data/file.txt")
            
            # sections = cp.class_parser().parse()
                        
        #     if category is None:
        #         await ctx.channel.send('No classes exist.\n')

        #     else:
        #         for section in sections:

        #             overwrites = {
        #                 ctx.guild.default_role: discord.PermissionOverwrite(read_messages= False), 
        #             }
        #             await ctx.guild.create_text_channel(section, overwrites=overwrites)
        #                                                 #, category=category)
        #         await ctx.channel.send('channels have been created for classes {}'.format(sections))
        # else:
        #     await ctx.channel.send('You do not have permission for this command')

def setup(bot):#required
    bot.add_cog(createClassCommand(bot))
