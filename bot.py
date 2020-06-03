import os
import discord
from discord.ext import commands
import asyncio
import json
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='js ')

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
motto_lib = os.path.join(PROJECT_ROOT, 'motto.json')

with open('motto.json', 'r', encoding='utf8') as read_motto:
    jMotto = json.load(read_motto)


@bot.event
async def on_ready():
    print(bot.user.name, 'has connected to the server.')


@bot.event
async def on_message(msg):
    trigger = ['e04', '幹', '幹你娘', '牙控灰機']
    random_reply = random.choice(jMotto['MOTTO'])
    motto = discord.File(random_reply)

    if msg.content in trigger:
        await msg.channel.send(motto)


@bot.command()
async def sendPic(ctx):
    pass


bot.run(TOKEN)
