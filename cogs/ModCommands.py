from discord import channel, member
from discord.ext import commands
from discord.ext.commands import bot, cog, has_permissions

class ModCommands(commands.Cog): #extends
    def __init__(self, bot):
        self.bot = bot

    #@commands.command()
    @commands.has_permissions(manage_roles= True)
    async def create_role(ctx, *, name):
        guild = ctx.guild
        await guild.create_role(name= name)
        await ctx.channel.send(f'Role {name} was created by {c}')
    # @commands.Cog.listener()
    # @has_permissions(administrator= True)
    # async def on_member_join(self, member):
    #     channel = member.guild.system_channel
    #     if channel is not None:
    #         await channel.send('Welcome {0.mention}.'.format(member))

    # @commands.command()
    # async def echo(self, ctx, arg):
    #     await ctx.channel.send(arg)


def setup(bot):#required
    bot.add_cog(ModCommands(bot))

