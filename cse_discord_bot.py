import discord
from discord.ext import commands
import os

# External File
import load_secrets as secrets
import cse_crawling


cse_url = 'https://cse.dongguk.edu/?page_id=799' # 컴퓨터공학과
type_cse = "컴퓨터공학과 "

# Get discord token
token = os.environ.get('discord_token')

prefix = "!"
client = commands.Bot(command_prefix=prefix)
# client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name, 'has connected to Discord!')
    await client.change_presence(status=discord.Status.online, activity=None)
    print('Ready')

    cse_message = cse_crawling.run(cse_url, type_cse)

    ch_cse = client.get_channel(865617763220717568)
    for i in range(len(cse_message)):
        await ch_cse.send(cse_message[i])

    print(client.user.name, 'successfully sent cse notices.')
    await client.close()
    print(client.user.name, 'successfully logged out.')


@client.command(name="cse-test")
async def react_test(ctx):
    # Get notice
    cse_message = cse_crawling.run(cse_url, type_cse)

    # Send message to test channel
    test_channel = client.get_channel(835518591830851584)
    for i in range(len(cse_message)):
        await test_channel.send(cse_message[i])
    
    print(client.user.name, 'successfully sent cse notices to test channel.')
    await client.close()
    print(client.user.name, 'successfully logged out.')


@client.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title=":rotating_light:", description="오류가 발생했습니다.", color=0xFF0000)
    embed.add_field(name="로그", value=f"```{error}```")
    ch = client.get_channel(835550287305244702)
    await ch.send(embed=embed)
    await ch.send("<@&{}>".format(str(797475663547203604)))

    await client.close()
    print(client.user.name, 'successfully logged out.')


# client.run(secrets.get_token()) # For local test
client.run(token)
