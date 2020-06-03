import os
import discord
from discord.ext import commands
import asyncio  # multithread的模組
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # 設定成跟.env裡一樣的字
bot = commands.Bot(command_prefix='ns ')  # 這裡設定prefix
Path = os.path.dirname(os.path.abspath(__file__))
f_ch = os.path.join(Path, 'whichChannel.txt')


def add(x, y):  # 2+2
    if(x.isdigit() and y.isdigit()):
        return str(eval(x) + eval(y))


def read(File):  # 讀檔的，沒這個檔會新增
    with open(File, 'a+') as f:
        f.seek(0)
        return f.readlines()


def write(File, content):  # 寫檔的，沒這個檔會新增
    with open(File, 'w+') as f:
        f.seek(0, 2)
        f.writelines(content)


# 用來純修改File中某個位置的資料
def only_change(File, text, index, value):  # File:str text:str index:int value:str
    content = read(File)
    x = text.split('\t')
    x.pop()
    text_new = ''
    for i in range(len(x)):
        if(i == index):
            text_new = text_new + value + '\t'
        else:
            text_new = text_new + x[i] + '\t'
    text_new = text_new + '\n'
    # 這行不知道是三小 List的replace小方法
    content = [text_new if x == text else x for x in content]
    write(File, content)
    return text_new


@bot.event
async def on_ready():  # BOT準備好會觸發這個event
    print(bot.user.name, 'has connected to Discord!')


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


@bot.command()
async def DMme(ctx):
    user = ctx.author
    await user.create_dm()
    await user.dm_channel.send('我這不就來思訓你了嗎')


@bot.command()
async def msghere(ctx):
    # 設定BOT主動說話會傳在這裡(使用者沒有先在chat觸發的狀況)
    content = read(f_ch)
    channel = ctx.channel.id
    server = ctx.message.guild.id
    flag = False
    for i in content:
        if(str(channel) in i):
            flag = True
            only_change(f_ch, i, 1, str(channel))
            break
    if(flag is False):
        text = f'{server}\t{channel}\t\n'
        content.append(text)
        write(f_ch, content)
    await ctx.send('如果我突然想講話的話就在這裡講')
bot.run(TOKEN)
