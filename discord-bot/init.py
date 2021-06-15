# Discord.py imports
import discord
from discord.errors import Forbidden
from discord.ext import commands, tasks


client = commands.Bot(command_prefix="!")

@tasks.loop(hours=1)
async def loops():
    role = discord.utils.get(server.roles, name="Muted")
    for channel in server.channels:
        try:
            await channel.set_permissions(role, speak=False, send_messages=False)
        except Forbidden:
            pass

@bot.event
async def on_ready():
    global mod_role, muted_role
    print("bot ready:", bot.user)
    server = client.get_guild(835851448784257044)
    mod_role = discord.utils.get(server.roles, name="Moderator")
    muted_role = discord.utils.get(server.guild.roles, name='Muted')
    loops.start()