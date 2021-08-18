import discord
import requests
import json
import textwrap
from discord.ext import commands

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qwe(self, ctx):
        print(type(self.bot.users))
        d = self.bot.users
        for x in d:
            print(x.name)
        await ctx.send("hey")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"lol ok {self.bot.latency * 1000}")

    @commands.command()
    async def stfu(self, ctx):
        await ctx.send(f"STFU RIGHT NOW")

    @commands.command()
    async def catp(self, ctx, amt=1):
        for i in range(amt):
            response = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=jpg,png")
            cat = json.loads(response.text)[0]
            await ctx.send(cat["url"])

    @commands.command()
    async def catg(self, ctx, amt=1):
        for i in range(amt):
            response = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=gif")
            cat = json.loads(response.text)[0]
            await ctx.send(cat["url"])

    @commands.command()
    async def dog(self, ctx, amt=1):
        for i in range(amt):
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            dog = json.loads(response.text)
            await ctx.send(dog["message"])

    @commands.command()
    async def emo(self, ctx, *, message = "stfu lol"):
        reg = ":regional_indicator_a: "

        messages = textwrap.wrap(message.lower().split('#')[0], 50, break_long_words=False)

        numbers = {
            '0': ':zero:', '1': ':one:', '2': ':two:', '3': ':three:', '4': ':four:', 
            '5': ':five:', '6': ':six:', '7': ':seven:', '8': ':eight:', '9': ':nine:' 
        }
        #await ctx.channel.purge(limit=1)

        for n in range(int(len(message)/50)+1):
            output = ""
            for i in messages[n]:
                if i.isalpha():
                    output += reg[:20] + i + reg[21:]
                elif i.isnumeric():
                    output += numbers[i]
                elif i == '!':
                    output += ":exclamation:"
                elif i == '?':
                    output += ":question:"
                elif i == ' ':
                    output += " "
                else:
                    output += i
            
            await ctx.send(output)

    # @commands.command()
    # async def speak(self, ctx, *, message):
    #     await ctx.send(message)

def setup(bot):
    bot.add_cog(Random(bot))
