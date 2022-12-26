import random
from helpers.munki_quote import munki_quote

async def amunski_quote_event(message, bot):
    if message.author == bot.user:
        return
    if message.author.name == "SmarDon":
        chance = random.random()
        if chance < 0.05:
            await message.channel.send(munki_quote())
    await bot.process_commands(message)