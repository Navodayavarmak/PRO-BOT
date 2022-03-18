import os
import discord
import datetime
import asyncio
import pyjokes
from better_profanity import profanity



messages = joined = 0
checker=0

joke = pyjokes.get_joke("en", "all")
client = discord.Client()
token = "OTQ2NDI5NDY4NzkxMTczMTgx.YhelIQ.Ardht6ytzVQpdNlx6osVtknfaOQ"


def bad_sink(message):
    global checker
    censored = profanity.censor(message)
    if message==censored :
        checker=0
    else :
         checker=1


def ran_joke():
    joke = pyjokes.get_joke("en", "all")
    return joke



async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(
                    f"TIME : {datetime.datetime.now()}, MESSAGES : {messages} ,MEMBERS : {joined}\n"
                )

            messages = 0
            joined = 0

            await asyncio.sleep(600)

        except Exception as e:
            print(e)
            await asyncio.sleep(600)


@client.event
async def on_ready():
    with open("stats.txt", "a") as f:
        f.write(
            f"We have logged in as {client.user} on {datetime.datetime.now()} \n"
        )
        print("BOT IS ONLINE...")


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("navodaya") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="change ur nick")

@client.event
async def on_member_join(member):

    global joined
    joined += 1

    for channel in member.guild.channels:
        if str(channel) == "general":
            await client.send_message(f"Welcome to the server {member.mention}")


@client.event
async def on_message(message):

    global messages
    messages += 1
    id = client.get_guild(946424314423558164)
    channels1 = ["testing"]
    commands = ["!joke", "$help", "!details","!coin","!users","$commands"]
    greetings = ["hi", "HI", "Hi", "HII", "Hii", "hii", "GM", "Good","good", "Good morning","Hello"]
    admin_commands = ["!delete all","!delete 20"]
    valid_users = ["Navodaya#5068"]
        





    bad_sink(message.content)
    if checker==0 :
        pass
    else :
        print (f"The message was deleted(bad word) {message.content} from {message.author}")
        await message.channel.purge(limit =1)
        
        




     


    #if str(message.channel) in channels1 and str(message.content) in commands:
    if  str(message.content) in commands:

        if str(message.content) == "!users":
            await message.channel.send(f"TOTAL NO OF USERS : {id.member_count}")
                                       
        elif str(message.content) == "!joke":
            await message.channel.send(ran_joke())

        elif str(message.content) == "!coin":
            await message.channel.send('Hello.'or 'helo')

        elif str(message.content) == "!details" :
          await message.channel.send("HELLO! IM FOREVER BOT 1.O,AS MY NAME SAYS I USED TO RUN FOREVER AND I WAS CREATED ON 22.02.2022")

        elif message.content == "$help":
            embed = discord.Embed(title="HEY HOW CAN I HELP YOU?",description="I CAN HELP BY THESE COMMANDS")
                                  
            embed.add_field(name="!users", value="GIVES TOTAL OF USERS")
            embed.add_field(name="!joke", value="GIVES A JOKE")
            embed.add_field(name="!commands", value="GIVES LIST OF COMMANDS")           
            embed.add_field(name="!details", value="BASIC INFO ABOUT ME")
  
            await message.channel.send(content=None, embed=embed)

        elif message.content == "$commands":
            embed = discord.Embed(title="Commands you can use",description="If you are unable to perform any Commands check your Permissions")
                                  
            embed.add_field(name="!users", value="GIVES TOTAL OF USERS")
            embed.add_field(name="!joke", value="GIVES A JOKE")
            embed.add_field(name="!delete all", value="Delete all message range of 100 [ADMINS]")
            embed.add_field(name="!delete 20", value="Delete 20 messages [ADMINS]")
            embed.add_field(name="!details", value="BASIC INFO ABOUT ME")
            
            await message.channel.send(content=None, embed=embed)

    
    content = message.content.lower()

    if message.author == client.user:
        return

    if any(greeting in content for greeting in greetings):
        return await message.channel.send('Hello,Good to see you :-)')

    if  str(message.author) in valid_users:
    
        if str(message.content) in admin_commands and str(message.content) == "!delete all":
                
            with open("history.txt", "a") as f:
                f.write(f"All message was deleted by {message.author} on {datetime.datetime.now()} \n")                                    
                await message.channel.purge(limit=100)

        elif str(message.content) in admin_commands and str(message.content) == "!delete 20":
                
            with open("history.txt", "a") as f:
                f.write(f"20 message was deleted by {message.author} on {datetime.datetime.now()} \n")                                
                await message.channel.purge(limit=20)

    


client.loop.create_task(update_stats())
client.run(token)




















