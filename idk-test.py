import os
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='js ')


@bot.event
async def on_ready():
    print(bot.user.name, 'has connected to the server.')


@bot.command()
async def sendPic(ctx):
    pass


bot.run(TOKEN)
