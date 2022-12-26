import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

from commands.ping import ping_command
from commands.hello import hello_command
from commands.joke import joke_command
from commands.music import music_command

from events.amunski_quote import amunski_quote_event


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
VOICE_CHANNEL = int(os.getenv("VOICE_CHANNEL"))

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#
# COMMANDS
#     
@bot.command()
async def ping(ctx):
    await ping_command(ctx)

@bot.command()
async def hello(ctx):
    await hello_command(ctx)


@bot.command()
async def joke(ctx):
    await joke_command(ctx)

@bot.command()
async def play(ctx, url: str):
    await music_command(ctx, url)


#
# EVENTS
#

@bot.event
async def on_ready():
    # Tells you when pagman is ready, and he send a message in a provided channel that he has arrived.
    print("PagMan is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("<:PagMan:1056702924253839421> is here BAYBEEE!")

@bot.event
async def on_message(message):
    await amunski_quote_event(message, bot)


bot.run(TOKEN)

