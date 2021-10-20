import discord
import asyncio
from discord.ext import commands


class PromoCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def give_member_promo(self, member):
        role = member.guild.get_role(self.client.config["promo_role"])
        await member.add_roles(role)

    async def take_member_promo(self, member):
        role = member.guild.get_role(self.client.config["promo_role"])
        await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.give_member_promo(member)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in self.client.config["promo_channels"]:
            await self.take_member_promo(message.author)

    @commands.command(
            name="promo"
    )
    async def promo(self, ctx):
        await ctx.send("Resetting promotion role for all users")

        awaitables = []

        async for member in ctx.guild.fetch_members():
            role_ids = [role.id for role in member.roles]
            if self.client.config["promo_role"] not in role_ids:
                awaitables.append(self.give_member_promo(member))

        await ctx.send(f"Giving role to {len(awaitables)} members")

        await asyncio.gather(*awaitables)

        await ctx.send("Done")


def setup(bot):
    bot.add_cog(PromoCog(bot))
