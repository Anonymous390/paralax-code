import discord
from discord.ext import commands
import os
import dotenv

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

client.run(token)
