from discord.ext import commands

class Listen(commands.Cog):
    def __init__(self, client):
        self.client = client

    commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.client.get_channel(self.client.config["welcome_channel"]).send(f"{member.name} has left")
    
    commands.Cog.listener()
    async def on_member_join(self, member):
        await self.client.get_channel(self.client.config["welcome_channel"]).send(f"{member.name} has joined (testing)")



def setup(bot):
    bot.add_cog(Listen(bot))