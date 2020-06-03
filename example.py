import os
import discord
from discord.ext import commands
import asyncio  # multithread的模組
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # 設定成跟.env裡一樣的字
bot = commands.Bot(command_prefix='ns ')  # 這裡設定prefix


def add(x, y):  # 2+2
    if(x.isdigit() and y.isdigit()):
        return str(eval(x) + eval(y))


@bot.event
async def on_ready():  # BOT準備好會觸發這個event
    print(bot.user.name, 'has connected to Discord!')


@bot.command(name='timezone')  # 這個就是觸發BOT的關鍵字，如果()留空白則函式名稱就是關鍵字
async def tz(ctx):
    a = 3
    b = 'string'
    await ctx.send(f'可以這樣用{a}yoyo{b}')

    def check(m):
        if(m == 'jing'):
            return True
    msg = await bot.wait_for('message', check=check)  # 等待使用者輸入東西加以判斷的方式
    await ctx.send(f'嫩逼你輸入了{msg}')  # msg就是剛才使用ˊ者輸的東西


@bot.command()
async def jafa(ctx, *args):  # 這樣打可以傳入參數
    if(len(args) == 2):
        msg = add(args[0], args[1])  # 可以在async中呼叫一般的def，但反過來不行
    await ctx.send(msg)  # await也只能在async中使用


@bot.event
async def on_error(event, *args, **kwargs):  # 好像是使用者亂打指令會記起來
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


@bot.command()
async def me(ctx):
    # 使用者有傳訊息，可以直接抓到user物件
    user = ctx.author
    # 第二種抓user方式，只給ID，讓BOT去每個他加入的server搜尋
    # 這種方法得到的user物件訊息更多(包含使用者在哪個語音聊天)
    for i in bot.guilds:
        user = discord.utils.find(lambda u: u.id == user.id, i.members)
    # 第三種抓user方式，一樣只給ID，得到資訊跟第一種一樣
    user = bot.get_user(user.id)
bot.run(TOKEN)
