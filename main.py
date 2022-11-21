import discord
import json
import os

from discord.ext import commands

file = open('./conf.json', 'r')
data = json.load(file)

# class client_reconn:
#     def __init__(self):
#         print('hello!')

client = commands.Bot(
    command_prefix=data['command_prefix'],
    self_bot=True
)

for file in os.listdir('cogs'):
    if file.endswith('.py'):
        name = file[:-3]
        client.load_extension(f'cogs.{name}')

client.run(data['bot_tokens'][0], bot=False)