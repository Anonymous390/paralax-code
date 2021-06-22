# Discord.py imports
import discord
import os
import dotenv

# Command imports
from discord.ext import commands
from init import client, mod_role, muted_role

color = 0x3498eb

def is_mod(user):
    return mod_role in user.roles

# Mute command
@client.command(aliases=["m"])
async def mute(ctx, member: discord.Member, reason="No reason provided"):
    if is_mod(ctx.message.author):
        if muted_role in member.roles:
            await ctx.send(embed=discord.Embed(title="Cannot mute user", description=f"User **{member}** is already muted", color=color))
            return
        await member.add_roles(muted_role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=color)
        await ctx.send(embed=embed)
        await member.send("You have been muted from " + ctx.guild.name + " for reason: " + reason)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=color)
        await ctx.send(embed=embed) 

# Unmute command
@client.command(aliases=["u", "umute"])
async def unmute(ctx, member: discord.Member):
  if is_mod(ctx.message.author):
    if muted_role not in member.roles:
        await ctx.send(embed=discord.Embed(title="Cannot unmute user", description=f"User **{member}** is already unmuted", color=color))
        return
    await member.remove_roles(muted_role)
    await member.send(f"You have been unmuted from {ctx.guild.name}")
    embed = discord.Embed(title="User Unmuted!", description=f"User **{member}** was unmuted by {ctx.message.author}!",colour=color)
    await ctx.send(embed=embed)

@bot.command(aliases=["b"])
async def ban(ctx, member: discord.Member, reason="No reason provided"):
    if is_mod(ctx.message.author):
        await ctx.send(f'User {member} has been banned')
        await member.ban()
        await member.send("You have been banned from " ctx.guild.name + " for reason: " + reason)

@bot.command()
async def unban(ctx, member=None):
    if not is_mod(ctx.message.author):
        await ctx.send("You do not have permission to do that!")
        return
    if member is None:
        await ctx.send("Please specify a user.")
    
    if "#" not in member:
        await ctx.send("That is not a valid username!")
    
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')[:-1], member.split('#')[-1]

    for ban_entry in banned_users:
        user = ban_entry.banned_users
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("Unbanned **" + user.name + "#" + user.discriminator + "**")
            await user.send("You have been unbanned from " + ctx.guild.name)

