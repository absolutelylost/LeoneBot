# from discord import channel, Client
from discord.ext import commands
from discord.ext.commands import bot, cog
import discord


class registerCommand(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= 'register', aliases= ['registering', 'reg'])
    #async def register(self, ctx, *, course):# self is instance of class
    async def register(self, ctx, member: discord.Member, course): #channel: discord.channel):# self is instance of class

        class_one = 882265290153525310
        class_two = 882265353332350996
        channel_id = 882265290153525310

        #mee6 159985870458322944

        print('{}\n\n'.format(member))
        print('{}\n\n'.format(course))
        #member = discord.Member
        if course == 'class_one':
            print('\n\nclass one chosen\n\n')
            channel_id = class_one
        elif course == 'class_two':
            print('\n\nclass two chosen\n\n')
            channel_id = class_two

        category = discord.utils.get(ctx.guild.categories, name= 'classes')
        if category is None:
            await ctx.channel.send('This Channel does not exist. Please check your input again or message a mod if you believe there is an error.\n')
        else:
            for channel in category.channels:
                #print('{} \n'.format(channel))
                if channel == 'course':
                    overwrites = {
                        ctx.guild.default_role: discord.PermissionOverwrite(read_messages= False), 
                        ctx.guild.me: discord.PermissionOverwrite(read_messages= True), 
                        ctx.author: discord.PermissionOverwrite(read_messages= True)            
                    }

            await ctx.channel.send('@{} has been registered.'.format(ctx.message.author))
            #await ctx.guild.create_text_channel()

        #new_channel = self.bot.get_channel(channel_id)
        # member = ctx.message.author
        # await member.move_to(new_channel) # only works for voice channels
        
        #await ctx.channel.send('Member have been registered')

def setup(bot):#required
    bot.add_cog(registerCommand(bot))


# check documentation on kick and class discord.ExpireBehavior
