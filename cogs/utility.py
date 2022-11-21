import discord
import time

from time import sleep
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["whois"])
    async def user(ctx, *, member: discord.User = None):
        """Displays some information about users account."""
        if member == None:
            member = ctx.author
        embed = discord.Embed(description=member.mention,
                              title=f'{member} ({member.id})')
        embed = embed.add_field(name='Created At', value=member.created_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
        await ctx.send(embed=embed, delete_after=5)

    @commands.command()
    async def mark(self, ctx):
        """Marks all servers as read."""
        for guild in self.bot.guilds:
            await guild.ack()

    @commands.command(aliases=["eat", "cl"])
    async def prune(self, ctx, amount: int = None):
        """Deletes all your past messages."""
        if amount == None:
            amount = 999999
        channel = await self.bot.fetch_channel(ctx.channel.id)
        async for message in channel.history(limit=amount).filter(lambda msg: msg.author == ctx.message.author).map(lambda m: m):
            try:
                await message.delete()
            except Exception:
                pass

    @commands.command(aliases=["gp"], usage="[channel/user id]")
    async def ghostprune(self, ctx, idx, amount: int = None):
        """Deletes all your past messages in provided channel/user id's channel."""
        try:
            try:
                channel = await self.bot.fetch_channel(int(idx))
            except Exception:
                channel = await self.bot.fetch_user(int(idx))
        except Exception:
            return await ctx.send(':x: *invalid channel/user id*', delete_after=2)

        if amount == None:
            amount = 999999

        async for message in channel.history(limit=amount).filter(lambda msg: msg.author == ctx.message.author).map(lambda m: m):
            try:
                # await sleep(1)
                await message.delete()
            except Exception:
                pass


def setup(bot):
    bot.add_cog(Utility(bot))
