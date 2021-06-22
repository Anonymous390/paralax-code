from discord.ext import commands
from discord.ext.commands import has_permissions
import discord
from init import client

# @client.event()
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.errors.CheckFailure):
#         await ctx.send('You do not have the correct role for this command.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Looks like you don't have the permissions and the required role.")

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member.mention} has been kicked!')

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member.mention} has been banned!')

@client.command()
@has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    verified_role = discord.utils.get(ctx.guild.roles, name="verified")
    non_verified_role = discord.utils.get(ctx.guild.roles, name="non-verified")
    await member.add_roles(muted_role)
    await member.remove_roles(verified_role)
    await member.add_roles(non_verified_role)
    await ctx.send(f'User {member.mention} has been muted!')

@client.command()
@has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    verified_role = discord.utils.get(ctx.guild.roles, name="verified")
    non_verified_role = discord.utils.get(ctx.guild.roles, name="non-verified")
    await member.remove_roles(non_verified_role)
    await member.add_roles(verified_role)
    await member.remove_roles(muted_role)
    await ctx.send(f'User {member.mention} has been unmuted!')

@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'User {user.name}#{user.discriminator} has been unbanned!')
            return

@client.command()
@has_permissions(manage_roles=True)
async def warn(ctx, member: discord.Member, *, reason):

    await ctx.send(f'{member.mention} you are being warned for "{reason}"')