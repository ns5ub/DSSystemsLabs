# Option 3: Discord Bot
Deliverable: Create and publish an interactive Discord bot in a test server (provided for you by the instructor). Unlike a Twitter bot that simply parses and replies to messages sent to it, Discord bots can have much more functionality. For instance, they can have a wide variety of commands that users can invoke in channels as well as in direct messages with the bot.
Like a Twitter bot, a Discord bot must be backed by a Python-backed application that runs actively with an open connection to the Discord activity API and is invoked by bot commands and messages. You must write and publish this app, and it should connect to at least one external data source such as an external API or a database for some of its possible interactions.
Your bot does not have to be "serious" – for instance it could play a game or quiz, but the seriousness will be found in how your application handles data, performs remote retrieval and processing of requests and replies.

Benchmarks:
1. Your bot should recognize a "help" message and reply with user instructions.
2. Your bot should provide at least three commands or functions.
3. Your bot should reply promptly with an intelligent response or an informative error
message.
4. Your bot should integrate with at least one external data source that you can document
and describe. This could be a database system or API.
5. Submit all code in a standalone GitHub repository in your account.

o Successful build of the bot and API solution using Lightsail or EC2 or Repl.it (recommended)– 10 points

o Functionality that meets all benchmarks – 10 points

o Creativity / Innovation / Quality – 2 points

o Documentation – Describes how to use the bot and the elements that make it operational 3 point

### Resources

Originally set up with the following tutorials: 

Base: https://realpython.com/how-to-make-a-discord-bot-python/

Repl.it: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

DOCS: https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html 

## Setup
Hosted on a Repl.it: https://replit.com/@NikitaSaxena1/DSSystemsLabs#FinalProject_DiscordBot/bot.py 

Running Code above starts the bot! Unfortunately, it has a high start time due to dependencies for the entire github repo. The discord token is stored as a secret on replit - the submission includes a join link for the replit to allow access to that when running the bot.

The bot is already attached to this server:
https://discord.gg/5ncgmn4bae

Or you can add it to a server by clickin this link: https://discord.com/api/oauth2/authorize?client_id=972244704227909743&permissions=534723951680&scope=bot

## 1 Help: bot.py

Using the bot functionality by discord, help messages are generated automatically. These messages include information as to how to use the functionality.

```
d.help
```

## 3 - 4 Functionality: bot.py

### Roll dice with d.r

```
d.r AdB+C
```

Try `d.r 2d20+4`

Rolls some generic amount of dice and adds a flat value to them. `d.help r` gives more information. A, B, C must all be integers.

### Query Feature

```
d.spell spell name
d.spell "spell name"
```

Try `d.spell acid arrow`

Connects to the DnD API and gives a description of the spell with other useful information.

The DnD 5e API is accessible here: https://www.dnd5eapi.co/ It allows users to query any of the features, spells, and monsters included in the System Reference Document for the tabletop game Dungeons and Dragons.

### Prediction

```
d.prediction
```

Get a magic 8-ball style prediction on how the next session will go, except this time, it's Dungeosn and Dragons themed!

