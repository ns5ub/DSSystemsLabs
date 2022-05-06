import discord
import os
import random

from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
bot = commands.Bot(command_prefix='d.')

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='r', help='Simulates rolling dice in the format AdB+C to roll A B-sided dice, and add C to the total.')
async def roll(ctx, dice_string: str):
  await ctx.send('dice called')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('You are missing an arguement')

bot.run(TOKEN)
