# Made for Python 3.6
#This is the github version so may not include updated commands when they are added to HonkBot
import random
import asyncio
import aiohttp
import json
import ffmpeg
import youtube_dl
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("Insert Custom Prefix Here")
TOKEN = "Insert Token Here"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(pass_context=True)
async def yt(ctx, url):

    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

    player = await vc.create_ytdl_player(url)
    player.start()
    await client.join_voice_channel(voice_channel)
    await client.say("Now Playing")
    print("Now Playing")
    await client.join_voice_channel(voice_channel).disconnect()
    

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="sagoi"))
    print("Logged in as " + client.user.name)





async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
