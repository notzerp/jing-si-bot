import os
import discord
from discord.ext import commands
import asyncio  # multithread的模組
from dotenv import load_dotenv
import random
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # 設定成跟.env裡一樣的字
bot = commands.Bot(command_prefix='ns ')  # 這裡設定prefix
Path = os.path.dirname(os.path.abspath(__file__))
f_ch = os.path.join(Path, 'whichChannel.txt')


def add(x, y):  # 2+2
    if(x.isdigit() and y.isdigit()):
        return str(eval(x) + eval(y))


# 檢查對人使用的指令有沒有正確@使用者 ex: js sendPic @電火王
# 這個檢查函式是寫死後面最多只能送一個使用者
async def command_handler(ctx, args, command):
    flag = False
    user = 0
    if(len(args) > 1):
        msg = f'你輸入了錯誤的格式, usage: **ns {command} @使用者**(不輸入則查詢自己)'
    if(len(args) == 0):
        user = ctx.author
        flag = True  # 成功get user
    if(len(args) == 1):
        length = len(args[0])
        lamda = args[0][0:3] + args[0][length-1]
        if(lamda != '<@!>'):
            msg = '用@的方式查別人喇'
        else:
            user = bot.get_user(int(args[0][3:length-1]))
            if(user is None):  # user搜尋結果為None，使用者可能亂輸入
                msg = '你輸入了三小??'
            else:
                flag = True  # 成功get user
    if(flag):
        return user
    else:
        await ctx.send(msg)
        user = 0  # 使用者亂輸入回傳user = 0
        return user


@bot.event
async def on_ready():  # BOT準備好會觸發這個event
    print(bot.user.name, 'has connected to Discord!')
    # 更改遊戲狀態的方法
    await bot.change_presence(status=discord.Status.online,
        activity=discord.Game('散播感恩與愛'))


@bot.event
async def on_message(msg):  # 有人在BOT可以看到的地方打字
    trigger = ['e04', '幹', '幹你娘']
    random_motto = random.choice(jMotto['MOTTO'])

    if msg.content in trigger:
        await msg.channel.send(random_motto)


@bot.command(name='timezone')  # 這個就是觸發BOT的關鍵字，如果()留空白則函式名稱就是關鍵字
async def tz(ctx):
    a = 3
    b = 'string'
    await ctx.send(f'可以這樣用{a}yoyo{b}')

    def check(m):
        if(m.content == 'jing'):  # 這邊可以設定訊息條件，回傳True代表成功
            return True
    msg = await bot.wait_for('message', check=check)  # 等待使用者輸入東西加以判斷的方式
    await ctx.send(f'嫩逼你輸入了{msg.content}')  # msg就是剛才使用ˊ者輸的東西


@bot.command()
async def jafa(ctx, *args):  # 這樣打可以傳入參數
    if(len(args) == 2):
        msg = add(args[0], args[1])  # 可以在async中呼叫一般的def，但反過來不行
    await ctx.send(msg)  # await也只能在async中使用


@bot.command()
async def me(ctx):
    # 使用者有傳訊息，可以直接抓到user物件
    user = ctx.author
    await ctx.send(f'第一種方法會顯示暱稱{user.display_name}')
    # 第二種抓user方式，只給ID，讓BOT去每個他加入的server搜尋
    # 這種方法得到的user物件訊息更多(包含使用者在哪個語音聊天)
    for i in bot.guilds:
        user = discord.utils.find(lambda u: u.id == user.id, i.members)
    await ctx.send(f'第二種方法也會顯示暱稱{user.display_name}')
    # 第三種抓user方式，一樣只給ID，得到資訊是較少的
    user = bot.get_user(user.id)
    await ctx.send(f'第三種方法只會顯示帳號{user.display_name}')


@bot.command()  # 讓BOT找你DM
async def DMme(ctx):
    user = ctx.author
    await user.create_dm()
    await user.dm_channel.send('我這不就來思訓你了嗎')


bot.run(TOKEN)
