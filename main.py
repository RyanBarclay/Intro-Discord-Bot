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


@client.event()
async def on_voice_state_update(member, before, after):
    if after != before:
        await ctx.send(f"{member} is stupid")


# END OF BOT CODE
print("CODE IS RUNNING")
client.run(TOKEN)
