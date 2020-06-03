import os
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='js ')

global general_id
general_id = bot.get_channel(716983938995716202)


@bot.event
async def on_ready():
    print(bot.user.name, 'has connected to the server.')


@bot.command()
async def sendPic(ctx):
    pic = discord.File('X:\github\jing-si-bot\pics\wo.png')
    await ctx.send(file=pic)


bot.run(TOKEN)
