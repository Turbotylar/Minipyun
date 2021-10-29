import discord
import json
from discord.ext import commands

import sys
import traceback

intents = discord.Intents.default()
intents.members = True

def get_prefix(bot, message):
    prefixes = bot.config["prefixes"]
    return commands.when_mentioned_or(*prefixes)(bot, message)

startup_cogs = [
    "cogs.dungeon",
    "cogs.error",
    "cogs.promo",
    "cogs.manage",
    "cogs.music",
    "cogs.misc"
]

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name} ({bot.user.id})")

    await bot.change_presence(status=discord.Status.online, activity=discord.Game("https://github.com/Turbotylar/Minipyun"))

if __name__ == "__main__":
    for ext in startup_cogs:
        bot.load_extension(ext)
    
    for cog_name in bot.cogs:
        cog = bot.get_cog(cog_name)
        for command in cog.get_commands():
            print(command)


    with open("config.json") as f:
        bot.config = json.load(f)

    
    bot.run(bot.config["bot_api_key"])

