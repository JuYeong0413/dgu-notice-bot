import discord
from discord.ext import commands
import os

# External File
import load_secrets as secrets
import crawling
import cse_crawling


# notice links
general_url = 'https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000' # 일반공지
academic_url = 'https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3638&id=kr_010801000000' # 학사공지
scholarship_url = 'https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3662&id=kr_010804000000' # 장학공지
cse_url = 'https://cse.dongguk.edu/?page_id=799' # 컴퓨터공학과

# notice types
type_general = "일반"
type_academic = "학사"
type_scholarship = "장학"
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

    # Get notice
    general_message = crawling.run(general_url, type_general)
    academic_message = crawling.run(academic_url, type_academic)
    scholarship_message = crawling.run(scholarship_url, type_scholarship)
    cse_message = cse_crawling.run(cse_url, type_cse)

    # Send message to channel
    ch_general = client.get_channel(797475056271622239)
    for i in range(len(general_message)):
        await ch_general.send(general_message[i])
    ch_academic = client.get_channel(797476259777085440)
    for i in range(len(academic_message)):
        await ch_academic.send(academic_message[i])
    ch_scholarship = client.get_channel(797476280836161546)
    for i in range(len(scholarship_message)):
        await ch_scholarship.send(scholarship_message[i])
    ch_cse = client.get_channel(865617763220717568)
    for i in range(len(cse_message)):
        await ch_cse.send(cse_message[i])

    print(client.user.name, 'successfully sent notices.')
    await client.close()
    print(client.user.name, 'successfully logged out.')


@client.command(name="test")
async def react_test(ctx):
    # Get notice
    general_message = crawling.run(general_url, type_general)
    academic_message = crawling.run(academic_url, type_academic)
    scholarship_message = crawling.run(scholarship_url, type_scholarship)
    cse_message = cse_crawling.run(cse_url, type_cse)

    # Send message to test channel
    test_channel = client.get_channel(835518591830851584)
    for i in range(len(general_message)):
        await test_channel.send(general_message[i])
    for i in range(len(academic_message)):
        await test_channel.send(academic_message[i])
    for i in range(len(scholarship_message)):
        await test_channel.send(scholarship_message[i])
    for i in range(len(cse_message)):
        await test_channel.send(cse_message[i])
    
    print(client.user.name, 'successfully sent notices to test channel.')
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
