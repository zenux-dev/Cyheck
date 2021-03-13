from breached import *
from ip_geolocation import *
from ip_vuln import *
from username_search import *
from proxy import *
import discord
from discord.ext import commands
from crypto import *
from prices import *
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

@client.command(name='MD5', help='Hashes a string in md5')
async def give(ctx, *, arg):
    encrypt_md5(arg)
    await ctx.send('The hash for ' + arg + ' is:' + encrypt_md5.md5)
    
@client.command(name='bdecode', help='Decodes a Base64 encoded string')
async def give(ctx, *, arg):
    decode_base64(arg)
    await ctx.send('The string for ' + arg + ' is:' + decode_base64.result)
    
@client.command(name='bencode', help='Base64 Encodes a string')
async def give(ctx, *, arg):
    encode_base64(arg)
    await ctx.send('The encode string of ' + arg + ' is:' + encode_base64.result)
    
@client.command(name='proxy', help='check if a proxy is alive or not and retrives its data')
async def give(ctx, *, arg):
    check_proxy(arg)
    if check_proxy.r == False:
        await ctx.send("Proxy: " + arg + "is dead")
    else:
        await ctx.send("Proxy: " + arg + "is alive and here is the data we found: " + check_proxy.r)

@client.command(name='price', help='Gets the price if a crypto currency')
async def give(ctx, arg, arg2):
    get_price(arg, arg2)
    b = get_price.result
    result = str(b)
    await ctx.send('The price of ' + arg + ' in ' + arg2 + " is " + result)
    
@client.command(name='ping', help='shows the bots ping')
async def give(ctx):
    await ctx.send('My ping is ' + client.latency + '!')
    
@client.command(name='invite', help='invite me!!')
async def give(ctx):
    await ctx.send(ctx.message.author.mention + ' https://discord.com/api/oauth2/authorize?client_id=815158077597679616&permissions=2147555392&scope=bot')
    
client.run(Token)
