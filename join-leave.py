import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
token = ""

@client.event
async def on_member_join(member):
    channel = client.get_channel(채널ID)
    embed = discord.Embed(title="입장", description="{}님이 서버에 입장하였습니다. 서버에 오신것을 환영합니다!".format(member.mention), color=0x000000)
    await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(채널ID)
    embed = discord.Embed(title="퇴장", description="{}님이 서버를 퇴장하였습니다. ".format(member), color=0x000000)
    await channel.send(embed=embed)

client.run(token)