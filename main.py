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
ipgeo_api = os.getenv("ipgeo")
shodan_api = os.getenv("shodan")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('-help'))
    print(f'{client.user} has connected to Discord!')

@client.command(name='ipg', help='tells you the location of an ip')
async def give(ctx, *, arg):
    get_location(ipgeo_api, arg)
    await ctx.send(get_location.response)

@client.command(name='breached', help='tells you if an email has been breached or not')
async def give(ctx, *, arg):
    check(arg)
    if check.breached or check.breached2:
       await ctx.send('Email:' + arg + ' was breached')
    elif not check.breached or check.breached2:
       await ctx.send('Email:' + arg + ' wasnt breached')

@client.command(name='ipv', help='check if an ip got any vulnerablities')
async def give(ctx, *, arg):
    ip_check(arg, shodan_api)
    if ip_check.vuln:
       await ctx.send('IP: ' + arg + ' is vulnerable')
    elif not ip_check.vuln:
       await ctx.send('IP: ' + arg + ' isnt vulnerable')

@client.command(name='uname', help='checks a username on all social media platforms')
async def give(ctx, *, arg):
     await ctx.send('please wait our quantum hamsters are searching for ya')
     username_search(arg)
     await ctx.send(ctx.message.author.mention + ' we found these: ' + username_search.Str)

    
@client.command(name='ping', help='shows the bots ping')
async def give(ctx):
    await ctx.send('My ping is ' + client.latency + '!')
    
@client.command(name='invite', help='invite me!!')
async def give(ctx):
    await ctx.send(ctx.message.author.mention + ' https://discord.com/api/oauth2/authorize?client_id=815158077597679616&permissions=2147555392&scope=bot')
    
client.run(Token)
