import discord
from discord.ext import commands

# External File
import load_secrets as secrets
import crawling_general as general
import crawling_academic as academic
import crawling_scholarship as scholarship

prefix = "!"
client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print(client.user.name, 'has connected to Discord!')
    await client.change_presence(status=discord.Status.online, activity=None)
    print('Ready')


@client.command(name="test")
async def react_test(ctx):
    """
    This command runs when user calls 'test' after the prefix.
    :param ctx: discord.context
    :return: None
    """

    # Get general notice
    # general_message = general.run()
    # academic_message = academic.run()
    scholarship_message = scholarship.run()

    # Send message to channel
    # await ctx.channel.send(general_message)
    # await ctx.channel.send(academic_message)
    await ctx.channel.send(scholarship_message)
    
    await client.close()
    print(client.user.name, 'successfully logged out.')

    return None

client.run(secrets.get_token())
