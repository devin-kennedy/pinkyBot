import asyncio

import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import os

bot = commands.Bot(command_prefix="p.", intents=discord.Intents.all())
TOKEN = os.environ["DISCORD_AUTH"]


@bot.event
async def on_ready():
    print(f"{bot.user} connected to discord")


@bot.command()
async def narrate(ctx, fname):
    channel = ctx.author.voice.channel
    if bot.user not in channel.members:
        await channel.connect()
    fname = f"assets\\clip{fname}.mp3"
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(fname,
                                                                 executable="C:\\Users\\llama\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe"))
    ctx.voice_client.play(source, after=lambda e: print(f"Player error: {e}") if e else print("Success"))


@bot.command()
async def disconnect(ctx):
    await ctx.voice_client.disconnect()


bot.run(TOKEN)
