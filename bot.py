import os
import discord
from discord.ext import commands
import json
import random
from dotenv import load_dotenv

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
motto_lib = os.path.join(PROJECT_ROOT, 'motto.json')
info = os.path.join(PROJECT_ROOT, 'server-info.json')

env_path = os.path.join(PROJECT_ROOT, '.env')
load_dotenv(dotenv_path=env_path, override=True)
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='js ')

# 資料庫從這邊讀進去
with open(motto_lib, 'r', encoding='utf8') as read_motto:
    jMotto = json.load(read_motto)


# 用來修改server-info中的資料
def info_set(obj, ID, data):  # obj=json第一層的key; ID=東西的ID; data=用dict的格式傳進來
    with open(info, 'r') as read_info:
        jinfo = json.load(read_info)
    flag = False
    for i in jinfo[obj]:
        if(i["ID"] == ID):  # 原本就有這筆資料則更新就好
            flag = True
            i.update(data)
            break
    if(flag is False):  # 沒有這筆資料要新增
        x = {"ID": ID}
        x.update(data)
        jinfo[obj].append(x)
    with open(info, 'w') as read_info:
        json.dump(jinfo, read_info, indent=4)


@bot.event
async def on_ready():
    # bot的狀態 now playing正在玩XXX
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game('散播感恩與愛'))
    print(bot.user.name, 'has connected to the server.')


@bot.event
async def on_message(msg):
    trigger = ['e04', '幹', '幹你娘']
    random_motto = random.choice(jMotto['MOTTO'])

    if msg.content in trigger:
        await msg.channel.send(random_motto)
    if (msg.content.startswith('js ')):
        await bot.process_commands(msg)


@bot.command()
async def sendPic(msg):
    pass


@bot.command()
async def msghere(msg):
    guild_id = msg.message.guild.id
    channel_id = msg.channel.id
    x = {"ID": guild_id, "channel_set": channel_id}
    info_set("server", guild_id, x)
bot.run(TOKEN)
