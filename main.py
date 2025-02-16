from settings import bot_token
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'Login dengan nama {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Ini adalah echo-bot yang dibuat dengan pustaka discord.py!')

@client.command()
async def parrot(ctx, *args): # args adalah tuple
    if not args:
        await ctx.send('Kirim suatu pesan untuk saya parrot!')
    else:
        sentence = ' '.join(args)
        await ctx.send(sentence)

client.run(bot_token)