# main.py

import discord
import config

TOKEN = config.DISCORD_TOKEN
client = discord.Client()

@client.event
async def on_raw_reaction_add(reaction):
    
    channel = await client.fetch_channel(reaction.channel_id)

    if str(channel.category) != config.MAIN_CHANNEL_CATEGORY: 
        return

    message = await channel.fetch_message(reaction.message_id)
    emojiText = str(reaction.emoji)

    newChannel = discord.utils.find(lambda c: emojiText in str(c.topic), channel.guild.text_channels)

    if newChannel:
        await newChannel.send(message.content)
        await message.delete()

client.run(TOKEN)