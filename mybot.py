import discord
import os
import logging
import random
import json
import requests
from config import TOKEN, PREFIX
from discord.ext import commands, tasks

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents = intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    game = discord.Game("big donger ok")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'loaded cogs.{extension}')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'unloaded cogs.{extension}')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'reloaded cogs.{extension}')

for file in os.listdir("./cogs"): # list all files in cogs folder
    if file.endswith(".py"): # gets cogs files that ends in .py
        bot.load_extension(f"cogs.{file[:-3]}") # loads the cog


class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)        

@bot.command()
async def speak(ctx, *, message):
    await ctx.send(message)   

bot.run(TOKEN)





