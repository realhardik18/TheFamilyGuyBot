# script for the discord bot
import discord
import os
from discord.ext import commands
from keep_alive import keep_alive
import random
from downloader import download  # importing from /scraper

client = commands.Bot(command_prefix="f ")
client.remove_command('help')


@client.event
async def on_ready():
    print("im alive and working!!(logged in as {0.user})".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Family Guy"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title="SLOW DOWN!!", description="there is a 30 second cooldown for this command!", color=0x1abc9c)
        embedVar.add_field(
            name="Bored?", value="Check out our [insta page](https://www.instagram.com/daily.griffins/) with more clips!\n follow us for more daily clips!!", inline=False)
    await ctx.send(embed=embedVar)


@client.command()
async def test(ctx):
    await ctx.send("yessir")


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def clip(ctx):
    file_name = f"{str(random.randint(1000000000, 9999999999))}.mp4"
    download(file_name)
    await ctx.send(file=discord.File(file_name))
    os.remove(file_name)


@client.command()
async def help(ctx):
    embedVar = discord.Embed(title="Here are my commands",
                             description=f"requested by {ctx.author.display_name}", color=0x1abc9c)
    embedVar.add_field(name="For a random familiy guy clip",
                       value="use **f clip**", inline=False)
    embedVar.add_field(
        name="FOLLOW US!", value="our [instagram](https://www.instagram.com/daily.griffins/)\ncontact [developer](https://realhardik18.github.io)", inline=False)

    await ctx.send(embed=embedVar)
keep_alive()
client.run('bot token')
