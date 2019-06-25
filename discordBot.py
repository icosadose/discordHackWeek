import discord
import googletrans

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    print(message.author, message.channel, message.content)
    if message.author == client.user:
        return

    if message.content.startswith("$version"):
        await message.channel.send(discord.__version__)

    if message.content.startswith("$help"):
        await message.channel.send("""
        `$help 1 - commands`\n
        `$help 2 - languages`\n
        """)

    if message.content.startswith("$language"):


client.run("discord bot token")
