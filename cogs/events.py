import aiohttp
import discord
import json

from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

# from ..multitoken import multitoken

file = open('./conf.json', 'r')
data = json.load(file)


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {}'.format(self.bot.user))

        # reconn = client_reconn()

    @commands.Cog.listener()
    async def on_relationship_add(self, relationship=discord.User):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(
                data['webhook_url'], adapter=AsyncWebhookAdapter(session))

            embed = discord.Embed(color=discord.Color.from_rgb(255, 255, 255))
            embed.add_field(name='on_relationship_add', value='{} ({})'.format(
                relationship.user, relationship.user.id))
            await webhook.send(content=self.bot.user.mention, embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            return

        if isinstance(error, commands.errors.MissingRequiredArgument):
            return await ctx.send(f':x: usage: **{ctx.command.usage}**', delete_after=2)

        try:
            await ctx.send(f':x: *{error}*', delete_after=2)
        except Exception:
            pass

    @commands.Cog.listener()
    async def on_command(self, ctx):
        try:
            await ctx.message.delete()
        except Exception:
            pass


def setup(bot):
    bot.add_cog(Event(bot))
