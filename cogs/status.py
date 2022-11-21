import discord

from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cs(self, ctx):
        """Clears your status."""
        await self.bot.change_presence(status=discord.Status.dnd, activity=None)

    @commands.command(aliases=["streaming"], usage="(arguments)")
    async def stream(self, ctx, *, args):
        """Sets your status as streaming."""
        stream = discord.Streaming(
            name=args, url='https://twitch.tv/' + self.bot.user.display_name)
        await self.bot.change_presence(status=discord.Status.dnd, activity=stream)

    @commands.command(aliases=["playing", "game"], usage="(arguments)")
    async def play(self, ctx, *, args):
        """Sets your status as playing."""
        game = discord.Game(name=args)
        await self.bot.change_presence(status=discord.Status.dnd, activity=game)

    @commands.command(aliases=["watching"], usage="(arguments)")
    async def watch(self, ctx, *, args):
        """Sets your status as watching."""
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(
            type=discord.ActivityType.watching, name=args
        ))

    @commands.command(aliases=["listening"], usage="(arguments)")
    async def listen(self, ctx, *, args):
        """Sets your status as listening to."""
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(
            type=discord.ActivityType.listening, name=args
        ))

    @commands.command(aliases=["competing"], usage="(arguments)")
    async def compete(self, ctx, *, args):
        """Sets your status as competing in."""
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(
            type=discord.ActivityType.competing, name=args
        ))


def setup(bot):
    bot.add_cog(Status(bot))
