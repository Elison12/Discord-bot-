import discord
from discord.ext import commands
import asyncio
import os
import random

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

newUserMessage = """
???Welcome message???
"""


@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
        try:
            await member.create_dm()
            await member.dm_channel.send(newUserMessage)
            print("sent message to " + member.name)

                except:
            print("Could't message to " + member.name)

# @client.event
# async def on_member_join(member):
# 	member  = member.guild
# 	guild  = member.guild
# 	await member.create_dm()
# 	await member.dm_channel.send(newUserMessage)


@client.event
async def on_message(message):
    if message.content.startswith('$eae'):
        await message.channel.send('eae!')
    myId = "<@!ID>"
    if message.content.startswith('$best'):
        await message.channel.send(myId)


@commands.command()
async def join(self, ctx, voice_channel: commands.VoiceChannelConverter):
    try:
        await voice_channel.connect()
    except commands.BotMissingPermissions as error:
        await ctx.send(f"I have joined: {voice_channel}")

client.run('TOKEN')
