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
