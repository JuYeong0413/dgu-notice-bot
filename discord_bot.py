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

    # Get notice
    general_message = general.run()
    academic_message = academic.run()
    scholarship_message = scholarship.run()

    # Send message to channel
    ch_general = client.get_channel(797475056271622239)
    await ch_general.send(general_message)
    ch_academic = client.get_channel(797476259777085440)
    await ch_academic.send(academic_message)
    ch_scholarship = client.get_channel(797476280836161546)
    await ch_scholarship.send(scholarship_message)
    
    await client.close()
    print(client.user.name, 'successfully logged out.')

    return None

client.run(secrets.get_token())
