from re import M
import discord
from discord.ext import commands
import asyncio
import random
import time
from pyvesync_v2 import VeSync
manager = VeSync("email", "pass")
manager.login()
manager.update()
my_switch = manager.outlets[0]
TOKEN = ''
client = commands.Bot(command_prefix = '/')
client.remove_command('help')

@client.event
async def on_ready():
    print("The bot is ready")
    await client.change_presence(activity=discord.Game(name='Prefix is /'))
 
@client.command()
@commands.has_permissions(administrator=True)
async def help(ctx):
    cmds = discord.Embed(
        title = "Commands",
        description = "A list of all commands and their functions",
        color = discord.Color.blue()
    )

    cmds.add_field(name='Clear', value='/clear [num]', inline=False)
    cmds.add_field(name="WordClear", value="/wordclear [Num] [specific word]", inline=False)
    cmds.add_field(name="Userclear", value="/userclear [Num] [@Member]", inline=False)
    cmds.add_field(name="Userinfo", value="/userinfo [@Member]", inline=False)
    cmds.add_field(name="Coinflip", value="/coinflip", inline=False)
    cmds.add_field(name="LightFlip", value="/lightflip", inline=False)
    cmds.add_field(name="Ping", value="/ping", inline=False)
    cmds.add_field(name="Toes", value="/toepics", inline=False)

    await ctx.send(embed=cmds)

@client.command()
@commands.has_permissions(administrator=True)
async def clear(gone, amount = 2):
    await gone.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def wordclear(ctx, amount, specific):
    await ctx.message.delete()
    messages = await ctx.channel.history(limit=int(amount)).flatten()
    for message in messages: 
        if specific in message.content.lower(): await message.delete()

@client.command()
@commands.has_permissions(administrator=True)
async def userclear(ctx, amount, *member: discord.Member):
    await ctx.message.delete()
    messages = await ctx.channel.history(limit=int(amount)).flatten()
    for message in messages:
        for mem in member:
           if message.author == mem: await message.delete()

@client.command()
@commands.has_permissions(administrator=True)
async def coinflip(flip): 
    choices = ["Heads", "Tails"]
    randcoin = random.choice(choices)
    embed = discord.Embed(
        title=randcoin,
        color = discord.Color.blue()
    )
    await flip.send(embed=embed)
askuser = discord.Embed(
     title=(f'Type out your guess!'),
     color = discord.Color.blue()
     )
@client.command()
@commands.has_permissions(administrator=True)
async def lightflip(flip):
    choices = ["On", "Off"]
    randcoin = random.choice(choices)
    channel = flip.channel
    await flip.send(embed=askuser)
    def check(m):
          global guess
          guess = m.content
          return m.content == 'On' or 'Off' and m.channel == channel
        
    msg = await client.wait_for('message', check=check)
    if guess == 'On' or guess == 'Off':
     embed = discord.Embed(
     title=(f'{msg.author} chose {guess}'),
     color = discord.Color.blue()
     )
     await flip.send(embed=embed)
    else:
     embed = discord.Embed(
     title=(f'Invalid guess! Guess must be On or Off (with a capital on the first letter)'),
     color = discord.Color.red()
     )
     await flip.send(embed=embed)
     return lightflip
    if randcoin == ('On'):
     on = (7)
     for x in range(on):
         print(x)
         my_switch.turn_off()
         time.sleep(0.5)
         my_switch.turn_on()
         print("on")
    
    
    if randcoin == ('Off'):
     off = (7)
     for x in range(off):
         print(x)
         my_switch.turn_on()
         time.sleep(0.3)
         my_switch.turn_off()
         print("off")

    if guess == (randcoin):
     print("RIGHT")
     embed = discord.Embed(
     title=(f"It's {randcoin}, {msg.author} was correct!"),
     color = discord.Color.green()
     )
     await flip.send(embed=embed)
    if guess != (randcoin):
     print("WRONG")
     embed = discord.Embed(
     title=(f"It's {randcoin}, {msg.author} was incorrect! Me personly, I would never get a light flip wrong but thats just me though"),
     color = discord.Color.red()
     )
     await flip.send(embed=embed)
    
client.run(TOKEN)
