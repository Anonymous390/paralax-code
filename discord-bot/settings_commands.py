# Discord.py imports
import discord
from discord.ext import commands
from io import BytesIO

# Command imports
from discord.ext import commands
from init import client

# Other imports
import requests

color = 0x3498eb

client.remove_command("help")

@client.command()
async def pypi(ctx, query=None):
    if query is None:
        await ctx.send(embed=discord.Embed(description="Please specify a package to query.", color=color))
        return

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

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help", description="Use !help <command> for extended information on a command.", color = ctx.author.color)
    em.add_field(name="Fun", value="random, h, c")
    em.add_field(name="Image", value="triggered, wanted, sparkle, deepfry")
    em.add_field(name="Package", value="pypi")

    await ctx.send(embed=em)

@help.command()
async def random(ctx):
    em = discord.Embed(title="random", description="Chooses a random item from a given set", color = ctx.author.color)
    em.add_field(name="**Syntax**", value="!random <item1> <item2> <item3>")

    await ctx.send(embed=em)

@help.command()
async def pypi(ctx):
    em = discord.Embed(title="pypi", description="Lists the details of the mentioned pypi package", color = ctx.author.color)
    em.add_field(name="**Syntax**", value="!pypi <package name>")

    await ctx.send(embed=em)

@help.command()
async def triggered(ctx):
    em = discord.Embed(title="triggered", description="Displays the profile picture of the user with the triggered meme!", color = ctx.author.color)
    em.add_field(name="**Syntax**", value="!triggered [username-optional]")

    await ctx.send(embed=em)

@help.command()
async def wanted(ctx):
    em = discord.Embed(title="wanted", description="Displays the profile picture of the user with the wanted meme!", color = ctx.author.color)
    em.add_field(name="**Syntax**", value="!wanted [username-optional]")

    await ctx.send(embed=em)

@help.command()
async def deepfry(ctx):
    em = discord.Embed(title="deepfry", description="Displays the profile picture of the user with deepfry effect!", color = ctx.author.color)
    em.add_field(name="**Syntax**", value="!deepfry [username-optional]")

    await ctx.send(embed=em)

@help.command()
async def sparkle(ctx):
    em = discord.Embed(title="wanted", description="Displays the profile picture of the user with sparkles!", color = ctx.author.color)
    em.add_field(name="**Syntax**", value="!wanted [username-optional]")

    await ctx.send(embed=em)

@help.command()
async def h(ctx):
    em = discord.Embed(title="h", description="Bot responds with 'Hello'.", color = ctx.author.color)
    em.add_field(name="**Syntax**", value="!h")

    await ctx.send(embed=em)

@help.command()
async def c(ctx):
    em = discord.Embed(title="c", description="Bot responds with ||ITS A SECRET TRY IT YOURSELF||'.", color = ctx.author.color)
    em.add_field(name="**Syntax**", value="!c")

    await ctx.send(embed=em)
