import discord
from discord.ext import commands
import youtube_dl
import asyncio

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'no_warnings': True,
        'quiet': True,
        'no_playlist': True,
        'duration': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        vc.play(discord.FFmpegPCMAudio(info['url']))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 0.5
        
    await asyncio.sleep(info['duration'])
    await vc.disconnect()

# Inicia o bot
bot.run('O_TOKEN_VAI_AQUI')


