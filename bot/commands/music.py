import discord
import youtube_dl
from discord.utils import get



async def music_command(ctx, url):
    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)
    await voice.connect()


    # ydl_opts = {
    #     'format': 'bestaudio/best',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '192',
    #     }],
    # }

    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     info = ydl.extract_info(url, download=False)
    #     title = info["title"]
    #     thumbnail = info["thumbnail"]
    #     duration = info["duration"]
    
    
