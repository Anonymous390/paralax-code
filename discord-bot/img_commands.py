# Discord.py imports
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import cv2
import os
import numpy as np
import random
import cv2
import discord
from discord.ext import commands
from io import BytesIO
from init import client

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@client.command()
async def wanted(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    background = Image.open("discord-bot/wanted.jpg")
    asset = member.avatar_url_as(size =128)
    data = BytesIO(await asset.read())
    foreground = Image.open(data)
    resized_foreground = foreground.resize((300, 300))

    offset = ((background.size[0] - resized_foreground.size[0]) // 2, (background.size[1] - resized_foreground.size[1]) // 2)
    background.paste(resized_foreground, offset, resized_foreground.convert("RGBA"))
    background.save("output.png")

    await ctx.send(file = discord.File("output.png"))
    os.remove("output.png")

@client.command()
async def triggered(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    background = Image.open("discord-bot/triggered.png")
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

@client.command()
async def sparkle(ctx, memeber: discord.Member = None):
    if memeber == None:
        member = ctx.author
    foregorund = Image.open("sparkles.png")
    asset = member.avatar_url_as(size =128)
    data = BytesIO(await asset.read())
    background = Image.open(data)
    resized_background = background.resize((500, 500))
    resized_foreground = foregorund.resize((500, 500))

    resized_background.paste(resized_foreground, (0, 0), resized_foreground.convert("RGBA"))
    resized_background.save("output.png")

    await ctx.send(file = discord.File("output.png"))
    os.remove("output.png")

@client.command()
async def deepfry(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    im = Image.open("images.jpeg")

    enhancer = ImageEnhance.Brightness(im)

    im = enhancer.enhance(0.5)
    im = im.filter(ImageFilter.GaussianBlur(radius = 1.4))
    converter = ImageEnhance.Color(im)
    im = converter.enhance(10)
    im.save('rev.png')
    image = cv2.imread('rev.png')
    noise_img = sp_noise(image,0.05)
    cv2.imwrite('output.png', noise_img)

    await ctx.send(file = discord.File("output.png"))
    os.remove("output.png")
    os.remove("rev.png")
