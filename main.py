import discord
from discord.ext import commands

TOKEN = open("token.txt", "r").readline()
client = commands.Bot(command_prefix="--")

# Global list to hold the names and intros
introList = []

# PUT CODE TO RUN BOT HERE

# We delete default help command
client.remove_command("help")


# answers with the ms latency
@client.command()
async def alive(ctx):
    await ctx.send(
        f"Yes I am deployed and working with a ping of: {round (client.latency * 1000)}ms "
    )


@client.command()
async def test(ctx):
    await ctx.send(f"This was returned: {client.voice_clients}ms ")


# END OF BOT CODE
print("CODE IS RUNNING")
client.run(TOKEN)
