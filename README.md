# cloud-bot
A bot written in Discord.py, using Cogs and slash commands.

### Quick Links
- Discord.py "quickstart" - https://discordpy.readthedocs.io/en/latest/quickstart.html
- Discord.py API ref - https://discordpy.readthedocs.io/en/stable/api.html


### Structure
All bot files are in /src

The Main.py file loads "cogs" from the src/cogs directory.
Cogs can be thought of as "individual commands", and provide a nice easy way of keeping code clean.

### Environment
The bot uses a .env file to grab things like the discord token. The .env file should be in the same directory as the __main__.py
The required environment variables are:
```bash
# Discord related things
PREFIX=> # The bot's prefix for non-slash commands. 
TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE # The discord token from https://discord.com/developers/applications

# Logging related things
LOG_LEVEL=20 # The bot's logging level (https://www.geeksforgeeks.org/logging-in-python/)
STREAM_LOGS=True # Allows us to stream logs to STDOUT. Good for visibility.
```

### Running the bot
##### Without Docker
1. Make sure the above .env file exists, or your environment contains the variables listed above.
2. `python /src/__main__.py`

##### With Docker
```TODO```