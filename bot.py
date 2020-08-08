import discord
from discord.ext import commands
from individualism import individualism
from io import BytesIO

bot = commands.Bot(command_prefix='`')

개인주의png = open("./image/개인주의.png", "rb")
인성 = open("./image/인성.png", "rb")
머리부터 = open("./image/머리부터발끝까지.png", "rb")

@bot.event
async def on_ready():
    print('ready')

@bot.command()
async def 개인주의(ctx, *, custom=None):
    if custom is not None:
        custom = custom.replace("\n", "\\n")
        if "인성" in custom:
            buf = individualism(인성, custom=custom)
        elif "머리" in custom or "발끝" in custom:
            buf = individualism(머리부터, custom=custom)
        else:
            buf = individualism(개인주의png, custom=custom)
    else:
        img = await ctx.author.avatar_url_as(format="png", size=512).read()
        buf = individualism(
            개인주의png,
            discriminator=ctx.author.discriminator,
            avatar=BytesIO(img)
        )
    await ctx.send(file=discord.File(buf, filename="sans.png"))

@bot.command()
async def 인성문제(ctx, *, custom=None):
    if custom is not None:
        custom = custom.replace("\n", "\\n")
        buf = individualism(인성, custom=custom)
    else:
        buf = individualism(인성, custom='"이 X끼 뭐야. 너 인성 문제있어?"')
    await ctx.send(file=discord.File(buf, filename="sans.png"))

@bot.command()
async def 머리부터발끝까지(ctx, *, custom=None):
    if custom is not None:
        custom = custom.replace("\n", "\\n")
        buf = individualism(머리부터, custom=custom)
    else:
        buf = individualism(머리부터, custom='"머리부터 발끝까지."')
    await ctx.send(file=discord.File(buf, filename="sans.png"))

@bot.command()
async def 자막(ctx, *, custom):
    custom = custom.replace("\n", "\\n")
    att = ctx.message.attachments[0]
    buf = individualism(BytesIO(await att.read()), custom=custom)
    await ctx.send(file=discord.File(buf, filename="sans.png"))

bot.run('너의 토큰')