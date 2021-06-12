# Discord.py imports
import discord
import os
import dotenv
from PIL import Image, ImageOps
from discord.ext import commands
from io import BytesIO

# Command imports
from discord.ext import commands
from init import client

# Other imports 
import requests

dotenv.load_dotenv()
token = os.getenv("TOKEN")
color = 0x3498eb


bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Command imports
from fun_commands import random_choice


@client.command(aliases=["h"])
async def hello(ctx):
    await ctx.send("Hello!")

@client.command(aliases=["c"])
async def cookie(ctx):
    await ctx.send("Have a 🍪")

@client.command()
async def pypi(ctx, query=None):
    if query is None:
        await ctx.send(embed=discord.Embed(description="Please specify a package to query.", color=color))
        return


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

    
    request = requests.get(f"https://pypi.org/pypi/{query}/json/")
    if request.status_code == 404:
        await ctx.send(embed=discord.Embed(description=f"There is no such package called **{query}**!", color=0x00))
    else:
        data = request.json()["info"]
        website = data['project_url']
        summary = data["summary"]
        homepage = data["home_page"]
        version = data["version"]
        requirements = "No requirements" if data["requires_dist"] is None else "\n".join(data["requires_dist"])
        await ctx.send(embed=discord.Embed(url=website, title=f"{query} version {version}", description=f"Version: {version}\nSummary: {summary}\nHomepage: {homepage}\nRequirements:\n```\n{requirements}```", color=color))

@client.event
async def on_message(message):
    if message.content.startswith("oof"):
        await message.channel.send("Bidoof!")
    await client.process_commands(message)


client.run(token)
