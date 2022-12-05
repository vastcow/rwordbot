import discord
import os
import random
from dotenv import load_dotenv


load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Client(intents=intents)
CHANNEL_ID = 1042139766851907697


rwords = [
    "retard",
    "retarded",
    "retart",
    "retarted",
    "retardeded"
]

bwords = [
    "vomit",
    "scat",
    "puke",
    "nigger",
    "tranny",
    "poop",
    "gore"
]


@bot.event
async def on_ready():
    guildCount = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guildCount = guildCount + 1
    print("retardbot is in " + str(guildCount) + " guilds.")


@bot.event
async def on_message(message):
    if message.author.id == 631068575406358539:
        message.author.kick()
        
    if message.channel.id == CHANNEL_ID:
        if message.author.bot and len(message.embeds) > 0:
            await message.delete()

        for word in bwords:
            if word in message.content.lower():
                await message.delete()
                break

    if message.author == bot.user or message.author.bot:
        return

    for words in rwords:
        if words in message.content.lower():
            await message.channel.send(f"{random.randint(0, 100)}% retarded")
            break

bot.run(DISCORD_TOKEN)
