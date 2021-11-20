import discord
from discord.ext import commands
import datetime
import pytz
from youtube_search import YoutubeSearch
import requests

class Misc(commands.Cog, name="Miscellaneous"):
    MOON_EMOJIS = {
      "NEW_MOON": "🌑 New Moon",
      "WAXING_CRESCENT": "🌒 Waxing Crescent",
      "FIRST_QUARTER": "🌓 First Quarter",
      "WAXING_GIBBOUS": "🌔 Waxing Bingus",
      "FULL_MOON": "🌕 Full Moon",
      "WANING_GIBBOUS": "🌖 Waning gibbous",
      "LAST_QUARTER": "🌗 Last Quarter",
      "WANING_CRESCENT": "🌘 Waning Crescent"
    }
    def __init__(self, client):
        self.client = client
    
    @commands.command(
        name="moon",
        breif="Stats",
        description="Get the current moon"
        )
    async def moon(self, ctx):
        """ Returns the current moon, as an emoji. """
        
        t = datetime.datetime.now(pytz.timezone("utc"))
        
        mi = pylunar.MoonInfo((41, 16, 36), (174, 46, 40))
        mi.update((t.year, t.month, t.day, t.hour, t.minute, t.second))

        phase = mi.phase_name()
        emoji = Stats.MOON_EMOJIS[phase]

        await ctx.send(f"Current Moon: {emoji}")

    @commands.command(
        name="today",
        breif="Miscellaneous commands",
        description="Miscellaneous commands"
        )
    #>today returns current time and day
    async def today(self, ctx, arg):        
        day = datetime.datetime.now(pytz.timezone(str(arg)))
        await ctx.send(day.strftime("%A %B %d %Y \nTime: %H:%M:%S"))

    @commands.command(
        name="inspire",
        breif="Ai generated inspiration",
        description="Ai generated inspirational quotes from inspirobot.me"
    )
    async def inspire(self, ctx):
        link = "http://inspirobot.me/api?generate=true"
        f = requests.get(link)
        imgurl = f.text
        await ctx.send(imgurl)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.content.startswith("!!!"):
            await ctx.channel.send("That thing that OSG does out of the blue.")

def setup(bot):
    bot.add_cog(Misc(bot))