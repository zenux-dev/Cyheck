from breached import *
from ip_geolocation import *
from ip_vuln import *
from username_search import *
import discord
from discord.ext import commands
import time
import os

Token = os.getenv("DISCORD_BOT_TOKEN")
client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command(name='ipg', help='tells you the location of an ip')
async def give(ctx, *, arg):
    get_location('77a3322e5bc2467faf675c567f3a150c', arg)
    await ctx.send(get_location.response)

@client.command(name='breached', help='tells you if an email has been breached or not')
async def give(ctx, *, arg):
    check(arg)
    if check.breached or check.breached2:
       await ctx.send('Email:' + arg + 'was breached')
    else:
        await ctx.send('Email:' + arg + ' wasnt breached')

@client.command(name='ipv', help='check if an ip got any vulnerablities')
async def give(ctx, *, arg):
    ip_check(arg)
    if ip_check.vuln:
       await ctx.send('IP: ' + arg + ' is vulnerable')
    elif not ip_check.vuln:
       await ctx.send('IP: ' + arg + ' isnt vulnerable')

@client.command(name='uname', help='checks a username on all social media platforms')
async def give(ctx, *, arg):
     await ctx.send('please wait our quantum hamsters are searching for ya')
     username_search(arg)
     time.sleep(90)
     await ctx.send(ctx.message.author.mention + ' we found these: ' + username_search.Str)


client.run(Token)
