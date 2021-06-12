import discord
from discord.ext import commands
import os
import dotenv
import requests

dotenv.load_dotenv()
token = os.getenv("TOKEN")

client = commands.Bot(command_prefix="#")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

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
    request = requests.get(f"https://pypi.org/pypi/{query}/json/")
    if request.status_code == 404:
        await ctx.send(embed=discord.Embed(description=f"There is no such package called **{query}**!", color=color))
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
    await bot.process_commands(message)

client.run(token)
