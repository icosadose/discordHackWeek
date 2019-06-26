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

    if message.content.startswith("$") == False and message.author.bot == False:
        if messageLang != targetLang:
            output = translator.translate(messageRaw, targetLang)
            await message.channel.send(output.text)

    if message.content.startswith("$langChange"):
        words = messageRaw.split()
        if words[1] not in LANGUAGES:
            await message.channel.send("Invalid language! Check the list using `$help 2`")
        else:
            targetLang = words[1]

    if message.author == client.user:
        return

    if message.content.startswith("$version"):
        await message.channel.send(discord.__version__)

    if message.content.startswith("$help"):
        await message.channel.send("""
        *Help Menu*
        `$commands  - commands the bot runs`
        `$langList - languages the bot supports`
        """)
    
    if message.content.startswith("$commands"):
        await message.channel.send("""
        *Current Commands For The Bot*
        `$help`     - Displays the help menu
        `$version`  - Displays the version of discord.py the bot uses
        `$langChange` - Allows a user to change the target language
        """)

    if message.content.startswith("$langList"):
        await message.channel.send("A full list of languages used and language codes can be found at https://py-googletrans.readthedocs.io/en/latest/")

client.run("NTkyNzcyNzQ3NjQyNDA0ODc2.XREtug.X42RrVIQF8CerKizmZZzChkcuwE")
