# Discord.py imports
import discord
import os
import dotenv
from discord.ext import commands

# Command imports
from discord.ext import commands
from init import client


dotenv.load_dotenv()
token = os.getenv("TOKEN")
color = 0x3498eb

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Command imports
from fun_commands import random_choice, on_message, hello, cookie
from img_commands import on_command_error, triggered, wanted, deepfry, sparkle
from settings_commands import pypi
from moderation_commands import mute, unmute, ban, unban, warn, kick


client.run(token)
