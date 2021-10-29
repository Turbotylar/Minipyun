import discord
from discord.ext import commands
import datetime
from youtube_search import YoutubeSearch
import requests

class Misc(commands.Cog, name="Miscellaneous"):
    def __init__(self, client):
        self.client = client

    @commands.command(
        name="today",
        breif="Miscellaneous commands",
        description="Miscellaneous commands"
        )
    #>today returns current day in NZT
    async def today(self, ctx):        
        day = datetime.date.today()
        await ctx.send(day.strftime("Time in New Zealand is:\n%A %B %d %Y"))
    
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

def setup(bot):
    bot.add_cog(Misc(bot))