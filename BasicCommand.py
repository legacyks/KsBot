#importing modules
import random

#Ping Command To Check If Bot is Working
async def ping(bot,channel):
    KsBot = bot
    await KsBot.send_message(channel,"pong")

#Magic 8 Ball Command
async def m8ball(bot,channel,message):
    KsBot = bot
    rng_number = random.randint(0,2) 
    answer_list = ['yes','no','maybe']
    if message[8:] != "":
        await KsBot.send_message(channel,answer_list[rng_number])
        print(message[8:])
    else:
        await KsBot.send_message(channel,"say smth u cuck")

