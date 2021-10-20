import discord
from discord.ext import commands

class DungeonCog(commands.Cog, name="Dungeon"):
    def __init__(self, client):
        self.client = client

    async def cog_check(self, ctx):
        print(ctx)
        ids = [role.id for role in ctx.author.roles]
        return any(
            role in self.client.config["mod_roles"]
            for role in ids
        )


    @commands.command(
        name="dungeon",
        breif="send a member to the dungeon",
        description="send a user to the dungeon"
    )
    async def dungeon(self, ctx, *, member: discord.Member):
        try:
            await ctx.send(f"You have sent {member.mention} to the dungeon")
            await self.send_to_dungeon(member)
        except Execption as e:
            await ctx.send(e)


    @commands.command(
        name="undungeon",
        breif="retrieve a member from the dungeon",
        description="retrieve a user from the dungeon"
    )
    async def dungeon(self, ctx, *, member: discord.Member):  
        try:
            await ctx.send(f"You have retreived {member.mention} from the dungeon")
            await self.unsend_to_dungeon(member)
        except Execption as e:
            await ctx.send(e)

    async def send_to_dungeon(self, member):
        jail_role = member.guild.get_role(self.client.config["dungeon_role"])
        await member.add_role(jail_role)

    async def unsend_to_dungeon(self, member):
        jail_role = member.guild.get_role(self.client.config["dungeon_role"])
        await member.remove_role(jail_role)

def setup(bot):
    bot.add_cog(DungeonCog(bot))
