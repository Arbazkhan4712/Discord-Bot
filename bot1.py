
import discord
import time
import asyncio


messages = joined = 0

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("ak") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="NO STOP THAT")


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await channel.send(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    global messages
    messages += 1

    id = client.get_guild(    )# add your channel id
    channels = ["commands"]
    valid_users = ["   "]#add the user id 
    bad_words = ["bad", "stop", "45"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)

    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        embed.add_field(name="how are you?", value="Gives an replay")
        embed.add_field(name="Portfolio", value="Gives an replay")
        embed.add_field(name="Youtube channel", value="Gives an replay")
        embed.add_field(name="What's App", value="Gives an replay")
        embed.add_field(name="Twitter", value="Gives an replay")
        embed.add_field(name="Linkedin", value="Gives an replay")
        embed.add_field(name="Instagram", value="Gives an replay")
        embed.add_field(name="Github", value="Gives an replay")
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("hello") != -1:
            await message.channel.send("Hi") 
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
        elif message.content == ("how are you?"):
            await message.channel.send("I'm doing great!") 
        elif message.content == ("how old are you?"):
            await message.channel.send("I'm 18 years old") 
        elif message.content == ("how old are you?"):
            await message.channel.send("I'm 18 years old")
        elif message.content == ("Portfolio"):
            await message.channel.send('https://arbazkhan4712.github.io/')
        elif message.content == ("Youtube channel"):
            await message.channel.send('https://www.youtube.com/channel/UCGYWLvjmBouSwjJIzeNDuzw')
        elif message.content == ("What's App"):
            await message.channel.send('https://wa.me/+918788855641')
        elif message.content == ("Twitter"):
            await message.channel.send('https://twitter.com/Arbazkh87773546')
        elif message.content == ("Linkedin"):
            await message.channel.send('https://www.linkedin.com/in/arbaz-khan-a73b71187')
        elif message.content == ("Instagram"):
            await message.channel.send('https://www.instagram.com/getsetcoding47/')
        elif message.content == ("Github"):
            await message.channel.send('https://github.com/Arbazkhan4712')
        
        



client.loop.create_task(update_stats())
client.run(token)  
        