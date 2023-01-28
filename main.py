import discord
from discord.ext import commands
import youtube_dl

# Inicializa o bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Comando para tocar uma música do YouTube
@bot.command()
async def play(ctx, url):
    # Cria uma nova conexão de voz
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()

    # Usa a biblioteca youtube_dl para baixar e reproduzir a música
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        vc.play(discord.FFmpegPCMAudio(info['url']))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 0.5

# Inicia o bot
bot.run('O_TOKEN_VAI_AQUI')


