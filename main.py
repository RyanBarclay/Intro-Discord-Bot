import discord
from discord.ext import commands

TOKEN = open(“token.txt”,”r”).readline()
client = commands.Bot(command_prefix = ‘--’)

# PUT CODE TO RUN BOT HERE

@client.command()
#We delete default help command
client.remove_command('help')


#answers with the ms latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')

# END OF BOT CODE
print("CODE IS RUNNING")
client.run(TOKEN)
