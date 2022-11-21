import discord

from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pfp", "av"])
    async def avatar(self, ctx, *, user: discord.User = None):
        """Display someones avatar."""
        if user == None:
            user = ctx.author
        try:
            await ctx.send(user.avatar_url)
        except Exception:
            pass


def setup(bot):
    bot.add_cog(General(bot))
