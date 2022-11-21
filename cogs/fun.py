import discord

from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(usage="[amount] (arguments)", )
    async def spam(self, ctx, amount: int, *, msg):
        """Spams the chat customizable amount of times."""
        for _i in range(amount):
            try:
                await ctx.send(msg)
            except Exception:
                pass

    @commands.command(aliases=["ping"])
    async def annoy(self, ctx, *, member: discord.Member = None):
        """Mentions a user in every text channel."""
        if member == None:
            return await ctx.send(':x: *invalid user*', delete_after=3)
        for channel in ctx.guild.channels:
            try:
                await channel.send(member.mention)
            except Exception:
                pass


def setup(bot):
    bot.add_cog(Fun(bot))
