import discord
import os
import random
import dotenv
import requests

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

  # ', '.join(rolls)
  # join function was stalling bot? manually doing it...
  rolls_string = str(rolls[0])
  for i in range(1, len(rolls)):
    print(i)
    rolls_string = rolls_string + ", " + str(rolls[i])
  roll_message = '> **Result:** {} \n*Dice Sum: {}* \n\t*Rolls: {}*'.format(total, roll_sum, rolls_string)
  await ctx.send('*Rolling {} {}-Sided Dice and Adding {}. The average roll is {}...* \n{}'.format(num_dice, dice_type, flat_add, dice_average, roll_message))




@bot.command(name='spell', help='Search for a spell using the DnD api')
async def search_spell(ctx, *args):
  
  x = '{}'.format(' '.join(args))
  url = f'https://www.dnd5eapi.co'
  name_query = f"/api/spells/?name={x}"

  spell_query_output = requests.request("GET", url +name_query).json()
  print(spell_query_output)
#  if(spell_query_output["count"]>1):
#    await ctx.send("There are many spells that match this request. Maybe try a more specfic search?")
#    return
  if(spell_query_output["count"]<=0):
       await ctx.send("No spells were found to match this request. Try another search")
  #print(url + spell_query_output["results"][0]["url"])
  spell = requests.request("GET", url + spell_query_output["results"][0]["url"]).json()
  spell = spell
  print(spell)
  embed = discord.Embed(
    title = spell["name"],
    description = spell["desc"][0], 
    color = 0xFF0000
  )
  embed.add_field(name="Range", value=spell["range"], inline = True)
  embed.add_field(name = "Components", value = spell["components"])
  embed.add_field(name="Duration", value = spell["duration"], inline=True)
  embed.add_field(name="Concentration", value = spell["concentration"], inline=True)
  await ctx.send(embed=embed)
  return



@bot.command(name='prediction', help='Get a prediction of how the next session will go')
async def pred(ctx):
  responses = [
    '```High rollers tonight!```',
    '```too many nat 1s```',
    '```tpk is prevalent```',
    '```the DM will cry```',
    '```i don\'t know how you made it through, but you did```',
    '```murder hobo rampage```',
    '```have backup characters prepared```',
    '```clean game```',
    '```the final boss lurks around```',
    '```shopping episode!!!```',
    '```get distracted by a chair```'   
  ]
  await ctx.send(random.choice(responses))
  return
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('You are missing an arguement')


bot.run(TOKEN)
