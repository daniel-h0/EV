import discord
from discord.ext import commands
import openai
import asyncio
import random


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.guilds = True


bot = commands.Bot(command_prefix=":", intents=intents)#this serves no purpose currently

relay_channels = [  # new channels can be added here
    "1081033554726760548",  # omegle channel on projectEV
    "898149848941993984",  # the gm-gn channel on phimosis productions
    "827267043891871748", # the general channel on Hoyts server
    "413082185248014347", # the argatha something channel on echos server
    "733519577841139787", # another secret sam server
    #NOTE: whenever someone removes this bot from a server this will stop working correctly
    
]#dont forget the commas


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print("Servers that contain EV:")
    for guild in bot.guilds:
        print(guild.name)
    #bot.loop.create_task(timer()) # starts up the timer
    


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    
    if str(message.channel.id) in relay_channels:
        attachments = [await attachment.to_file() for attachment in message.attachments]
        embeds = message.embeds

        for ch_id in relay_channels:
            if ch_id != str(message.channel.id):
                channel = bot.get_channel(int(ch_id))
                await channel.send(f'{message.author}: {message.content}', files=attachments, embeds=embeds)

    await bot.process_commands(message)
    
@bot.command() #this command will list all the servers the bot is in.
async def servers(ctx):
    server_list = [guild.name for guild in bot.guilds]
    await ctx.send(f"Connected servers: {', '.join(server_list)}")

bot.run("")# bot token here
