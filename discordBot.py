import discord
from googletrans import Translator, LANGCODES, LANGUAGES

client = discord.Client()
translator = Translator()
targetLang = "en"

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    global targetLang
    print(message.author, message.channel, message.content)
    messageRaw = str(message.content)
    messageLang = translator.detect(messageRaw).lang
    print(targetLang)
    print(messageLang)

    if message.content.startswith("$") == False:
        if messageLang != targetLang:
            output = translator.translate(messageRaw, targetLang)
            await message.channel.send(output)

    if message.content.startswith("$language"):
        words = messageRaw.split()
        if len(words[1]) < 2 or len(words[1]) > 2:
            await message.channel.send("Invalid language! Check the list using `$help 2`")
        else:
            targetLang = words[1]
            changeLang = "The language will be changed to " + targetLang
            await message.channel.send(changeLang)

    if message.author == client.user:
        return

    if message.content.startswith("$version"):
        await message.channel.send(discord.__version__)

    if message.content.startswith("$help"):
        await message.channel.send("""
        *Help Menu*
        `$help 1 - commands`
        `$help 2 - languages`
        """)
    
    if message.content.startswith("$help 1"):
        await message.channel.send("""
        *Current Commands For The Bot*
        `$help`     - Displays the help menu
        `$version`  - Displays the version of discord.py
        `$language` - Allows a user to change the target language
        `$test`     - Returns content of a message
        """)

    if message.content.startswith("$test"):
        pass

client.run("discord bot token")
