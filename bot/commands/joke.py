from helpers.get_joke import get_joke
import time

async def joke_command(ctx):
    joke = get_joke()
    if "text" in joke:
        await ctx.send(joke["text"])
    else:
        await ctx.send(joke["setup"])
        time.sleep(2)
        await ctx.send(joke["delivery"])