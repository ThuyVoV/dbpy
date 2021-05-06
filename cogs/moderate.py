import discord
from discord.ext import commands

class Moderate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.something = discord.ClientUser
        print(self.something.avatar_url)

    @commands.command()
    async def purge(self, ctx, amt=1):
        await ctx.channel.purge(limit=amt)

    @commands.command(aliases=['audit'])
    async def get_audit(self, ctx):
        
        async for entry in self.bot.guild.audit_logs(limit=100):
            print('{0.user} did {0.action} to {0.target}'.format(entry))

    @commands.command()
    async def cu(self, ctx):
        await ctx.send(f"{ctx.guild} |||guild")
        await ctx.send(f"{ctx.message} |||message")
        await ctx.send(f"{ctx.author} |||author")
        #await ctx.send(f"{ctx.} |||")


def setup(bot):
    bot.add_cog(Moderate(bot))