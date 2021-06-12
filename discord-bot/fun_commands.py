# Discord.py imports
import discord
import os
import dotenv

# Command imports
from discord.ext import commands
from init import client

# Other imports
import random

@client.command(aliases=["random"])
async def random_choice(ctx):
    variables = ctx.message.content.split(' ')
    num = random.choice(variables[1:])
    await ctx.send(num)

@client.event
async def on_message(message):
    if message.content.startswith("oof"):
        await message.channel.send("Bidoof!")
    await client.process_commands(message)

@client.command(aliases=["h"])
async def hello(ctx):
    await ctx.send("Hello!")

@client.command(aliases=["c"])
async def cookie(ctx):
    await ctx.send("Have a 🍪")

