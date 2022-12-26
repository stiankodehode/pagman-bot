from discord.ext import commands
import discord
import time
from src.get_joke import get_joke


BOT_TOKEN = "MTA1NjY0Mzc3MzMyMjUwMjI3NA.GRMODx.AuyWmBXhODW7pqETxLTtSfGuI1rw5T3iHc28Pk"
CHANNEL_ID = 1056406916424810496

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("PagMan is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("<:PagMan:1056702924253839421> is here BAYBEEE!")

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
        
        
    return



bot.run(BOT_TOKEN)

