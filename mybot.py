#https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-discord-connection

import discord
import os
import logging
import random
import json
import requests
from env import TOKENXX

from discord.ext import commands, tasks
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents = intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    game = discord.Game("big donger ok")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
@commands.is_owner()
async def load(ctx,extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'loaded cogs.{extension}')

@bot.command()
@commands.is_owner()
async def unload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'unloaded cogs.{extension}')

@bot.command()
@commands.is_owner()
async def reload(ctx,extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'reloaded cogs.{extension}')

for file in os.listdir("./cogs"): # lists all the cog files inside the cog folder.
    if file.endswith(".py"): # It gets all the cogs that ends with a ".py".
        #name = file[:-3] # It gets the name of the file removing the ".py"
        bot.load_extension(f"cogs.{file[:-3]}") # This loads the cog.

#bot.run(os.getenv("TOKEN"))
bot.run(TOKENXX)





