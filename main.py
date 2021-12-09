import json, discord
from random import choice
from discord.ext import commands
import os
from discord.ui import Button, View

client = commands.Bot(command_prefix= '~', help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Activity(
        type=discord.ActivityType.listening, name="~help"))
     
@client.command()
async def help(ctx):
    with open('helps.json') as helps:
        helps = list(json.load(helps).items())
        helps = choice(helps)
        helps, author = helps
    embed = discord.Embed(title="Truth or Dare", description=helps,color=0xe75480)
    inv_button = Button(label = "Invite Me!", url = "https://discord.com/api/oauth2/authorize?client_id=890608373437980732&permissions=380104727552&scope=bot")
    view = View()
    view.add_item(inv_button)
    await ctx.reply(embed=embed, view=view)

@client.command(aliases=['d'])
async def dare(ctx):
    with open('dare.json') as dare:
        dare = list(json.load(dare).items())
        dare = choice(dare)
        dare, author = dare
    embed = discord.Embed(title="Dare", description=dare,color=0xa020f0)
    await ctx.reply(embed=embed)

@client.command(aliases=['t'])
async def truth(ctx):
    with open('truth.json') as truth:
        truth = list(json.load(truth).items())
        truth = choice(truth)
        truth, author = truth
    embed = discord.Embed(title="Truth", description=truth,color=0xffb6c1)
    await ctx.reply(embed=embed)

@client.command(aliases = ['haveyouever'])
async def hye(ctx):
    with open('hye.json') as hye:
        hye = list(json.load(hye).items())
        hye = choice(hye)
        hye, author = hye
    embed = discord.Embed(title="Have You Ever", description=hye,color=0x007fff)
    await ctx.reply(embed=embed)

@client.command(aliases = ['wouldyourather'])
async def wyr(ctx):
    with open('wyr.json') as wyr:
        wyr = list(json.load(wyr).items())
        wyr = choice(wyr)
        wyr, author = wyr
    embed = discord.Embed(title="Would You Rather", description=wyr,color=0xadd8e6)
    await ctx.reply(embed=embed)

@client.command(aliases = ['invite'])
async def inv(ctx):
    with open('inv.json') as inv:
        inv = list(json.load(inv).items())
        inv = choice(inv)
        inv, author = inv
    embed = discord.Embed(title= "Invite me!",description=f"[Invite me to your Server!]({inv})" ,color=0xa9a9a9)
    await ctx.reply(embed=embed)

@client.command()
async def server(ctx):
    with open('server.json') as server:
      server = list(json.load(server).items())
      server = choice(server)
      server, author = server
      embed = discord.Embed(title="Join my Server!",description=f"[Join here!]({server)",color=0xffea00)
      await ctx.reply(embed=embed)
      
@commands.has_permissions(administrator=True) #you can remove this setting if u want, here i set this command to an only admin, so that only roles with admin power can create dares
@client.command()
async def created(ctx, *, sentence):
  with open('dare.json', "r+") as dare:
    data = json.load(dare)
    data[sentence.capitalize()] = str(ctx.message.author)
    dare.seek(0)
    json.dump(data, dare)
    await ctx.reply("Dare created.\nREMEMBER: Your dare may not break the rules of this server!")
    
@commands.has_permissions(administrator=True) #here also same as before
@client.command()
async def createt(ctx, *, sentence):
  with open('truth.json', "r+") as truth:
    data = json.load(truth)
    data[sentence.capitalize()] = str(ctx.message.author)
    truth.seek(0)
    json.dump(data, truth)
  await ctx.reply("Truth created.\nREMEMBER: Your truth may not break the rules of this server!")

@commands.has_permissions(administrator=True) #same
@client.command()
async def createhye(ctx, *, sentence):
  with open('hye.json', "r+") as hye:
    data = json.load(hye)
    data[sentence.capitalize()] = str(ctx.message.author)
    hye.seek(0)
    json.dump(data, hye)
  await ctx.reply("HYE created.\nREMEMBER: Your HYE may not break the rules of this server!")

@commands.has_permissions(administrator=True) #same
@client.command()
async def createwyr(ctx, *, sentence):
  with open('wyr.json', "r+") as wyr:
    data = json.load(wyr)
    data[sentence.capitalize()] = str(ctx.message.author)
    wyr.seek(0)
    json.dump(data, wyr)
  await ctx.reply("WYR created.\nREMEMBER: Your WYR may not break the rules of this server!")


my_secret = os.environ['TOKEN']
client.run(os.getenv('TOKEN'))
