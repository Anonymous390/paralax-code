import discord
import os
import dotenv
from PIL import Image, ImageOps
from discord.ext import commands
from io import BytesIO

dotenv.load_dotenv()
token = os.getenv("TOKEN")

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#hello'):
        await message.channel.send('Hello!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@client.command()
async def wanted(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    background = Image.open("wanted.jpg")
    asset = member.avatar_url_as(size =128)
    data = BytesIO(await asset.read())
    foreground = Image.open(data)
    resized_foreground = foreground.resize((round(foreground.size[0]*0.5), round(foreground.size[1]*0.5)))

    offset = ((background.size[0] - resized_foreground.size[0]) // 2, (background.size[1] - resized_foreground.size[1]) // 2)
    background.paste(resized_foreground, offset, resized_foreground.convert("RGBA"))
    background.save("output.png")

    await ctx.send(file = discord.File("output.png"))
    os.remove("output.png")

@client.command()
async def triggered(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    background = Image.open("triggered.png")
    asset = member.avatar_url_as(size =128)
    data = BytesIO(await asset.read())
    foreground = Image.open(data)
    resized_foreground = foreground.resize((500, 500))
    resized_foreground = resized_foreground.convert("L")
    resized_foreground = ImageOps.colorize(resized_foreground, black = (246, 31, 31), white = (245, 223, 81))

    background.paste(resized_foreground, (0, 0), resized_foreground.convert("RGBA"))
    background.save("output.png")

    await ctx.send(file = discord.File("output.png"))
    os.remove("output.png")


client.run(token)
