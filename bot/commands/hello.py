async def hello_command(ctx):
    await ctx.send(f"Hello {ctx.author.name}")