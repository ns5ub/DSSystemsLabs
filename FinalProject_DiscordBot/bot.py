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

@bot.command(name='r', help='Simulates rolling dice in the format AdB+C. \n For example 3d6+4 rolls 3 6 sided dice and adds 4')
async def roll(ctx, dice_string: str, *args):
  try: 
    num_dice = dice_string.split('d')[0]
    dice_type = dice_string.split('d')[1]
  except Exception as e:
    print(e)
    await ctx.send("Format has to be in AdB.")
    return

  flat_add = 0
  
  if '+' in dice_type:
    flat_add = dice_type.split('+')[1]
    dice_type = dice_type.split('+')[0]

  if len(args) > 0 and args[0] == '+':
    flat_add = args[1]

  try:
    num_dice = int(num_dice)
    dice_type = int(dice_type)
    flat_add = int(flat_add)
  except Exception as e:
    print(e)
    await ctx.send("Can't roll or add not a number!")
    return

  #return num_dice, dice_type, flat_add
  dice_average = (num_dice * ((1+dice_type)/2)) + flat_add
  rolls = [random.randint(1,dice_type) for r in range(num_dice)]
  roll_sum = sum(rolls)
  total = roll_sum + flat_add
  print(rolls)
  print(type(rolls))
  print(rolls[0])
  print(type(rolls[0]))

  # ', '.join(rolls)
  # join function was stalling bot? manually doing it...
  rolls_string = str(rolls[0])
  for i in range(1, len(rolls)):
    print(i)
    rolls_string = rolls_string + ", " + str(rolls[i])
  roll_message = '> **Result:** {} \n*Dice Sum: {}* \n\t*Rolls: {}*'.format(total, roll_sum, rolls_string)
  await ctx.send('*Rolling {} {}-Sided Dice and Adding {}. The average roll is {}...* \n{}'.format(num_dice, dice_type, flat_add, dice_average, roll_message))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('You are missing an arguement')

bot.run(TOKEN)
