import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
import time
import random

from helpers.get_joke import get_joke
from helpers.munki_quote import munki_quote

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = 1056406916424810496
VOICE_CHANNEL = 1056406779585626145

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#
# COMMANDS
#     

@bot.command()
async def play(ctx):
    command = ctx.message.content.split(" ")
    url = command[1]
    channel = bot.get_channel(VOICE_CHANNEL)
    await channel.connect()
    
    

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}")


@bot.command()
async def joke(ctx):
    joke = get_joke()
    if "text" in joke:
        await ctx.send(joke["text"])
    else:
        await ctx.send(joke["setup"])
        time.sleep(2)
        await ctx.send(joke["delivery"])
        
#
# EVENTS
#

@bot.event
async def on_ready():
    print("PagMan is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("<:PagMan:1056702924253839421> is here BAYBEEE!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.name == "SmarDon":
        chance = random.random()
        if chance < 0.05:
            await message.channel.send(munki_quote())
    await bot.process_commands(message)



bot.run(TOKEN)

