#Discord Modules
import discord
from discord.ext.commands import Bot

#Common Modules
import random
import pprint
import ast

#Self-made Module
import PointSystem
import BasicCommand
import Music


#Bot/Discord/Owner
#Change Accordingly
owner_id = 123456 
client_id = 123456 
client_secret = ""
bot_token = ""

#Bot Initiations
KsBot = Bot(command_prefix ='//')

#Display Bot Info and Discord Version
@KsBot.event
async def on_ready():
    print('Discord Version : ' + discord.__version__)
    print('Bot User Name : ' + KsBot.user.name)
    print('Bot ID : ' + KsBot.user.id)
    print('----------------------')

#Display The Total Number of Users Registered with the Bot
registered_members_file = open("RegisteredMembers.txt")
number_of_registered_members = len(ast.literal_eval(registered_members_file.read())) #storing the content of RegisteredMembers.txt as a dictionary
print("Number of registered user in this server: " + str(number_of_registered_members))
registered_members_file.close()

#All the commands
@KsBot.event
async def on_message(message):
    
#Register Command Called From PointSystem Module
#Register user with the bot for point system
    if message.content.startswith("//register"):
        await PointSystem.register(KsBot,message.author,message.author.id)
    
#Balance Command Called From PointSystem Module
#Show User Their Point Balance
    if message.content.startswith("//balance"):
        await PointSystem.display_points(KsBot,message.author,message.author.id,message.channel)

#Betting On Head Or Tails
    if message.content.startswith("//choose-h"):
        registered_members = await PointSystem.get_members_info()
        if message.author.id not in registered_members:
            await KsBot.send_message(message.channel,"Error: you are not registered")
        bet = int(message.content[11:])
        await PointSystem.head_or_tail(KsBot,message.author.id,message.channel,"head",bet)
    elif message.content.startswith("//choose-t"):
        registered_members = await PointSystem.get_members_info()
        if message.author.id not in registered_members:
            await KsBot.send_message(message.channel,"Error: you are not registered")
        bet = int(message.content[11:])
        await PointSystem.head_or_tail(KsBot,message.author.id,message.channel,"tail",bet)
        

#Ping Command Called From BasicCommand Module
    if message.content.startswith("//ping"):
        await BasicCommand.ping(KsBot,message.channel)

#Magic 8 Ball Command Called From BasicCommand Module
    if message.content.startswith("//m8ball"):
        await BasicCommand.m8ball(KsBot,message.channel,message.content)

#Summon Command Called From Music Module
    if message.content.startswith("//summon"):
        await Music.summon(KsBot,message.author,message.channel)
    await KsBot.process_commands(message)
    
#Run Bot
KsBot.run(bot_token)
