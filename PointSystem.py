#Custom Module for Point System

#Importing Modules
import pprint
import ast
import random 

async def get_members_info():
    registered_members_file = open("RegisteredMembers.txt")
    registered_members = ast.literal_eval(registered_members_file.read()) #storing the content of RegisteredMembers.txt as a dictionary
    return registered_members
    registered_members_file.close()

async def register(bot,sender,sender_id):
    KsBot = bot
    #Gets all registered members ID and points from file
    registered_members = await get_members_info()
    print("Registering ID " + sender_id + " ...")
    if sender_id in registered_members:
        await KsBot.send_message(sender,"Registration Fail:Already a memmber")
        print("Registration Failed: Already a member")
    elif sender_id not in registered_members:
        print("User " + str(sender) + " is not registered")
        registered_members[sender_id] = 1000
        registered_members_file = open("RegisteredMembers.txt",'w')
        registered_members_file.write(pprint.pformat(registered_members))
        registered_members_file.close()
        await KsBot.send_message(sender,"Registration OK!")
        print("Registeration Successful")

async def display_points(bot,sender,sender_id,channel):
    KsBot = bot
    #Gets all registered members ID and points from file
    registered_members = await get_members_info()

    #Display Points
    if sender_id in registered_members:
        await KsBot.send_message(channel,"Your Current Balance: {point} KSD".format(point = registered_members[sender_id]))
    elif sender_id not in registered_members:
        await KsBot.send_message(channel,"Error: you are not registered")

#Head Or Tail Randomiser and Result Announcer
async def head_or_tail(bot,sender_id,channel,choice,bet):
    KsBot = bot
    coin_status_possibility = ["head","tail"]
    coin_status = coin_status_possibility[random.randint(0,1)]
    change = bet
    if coin_status == choice:
        registered_members = await update_points(sender_id,change)
        await KsBot.send_message(channel,"Result:{result} \nYou Win! \nYour New Balance: {point} KSD".format(point = registered_members[sender_id], result = coin_status))
    elif coin_status != choice:
        registered_members = await update_points(sender_id,-change)
        await KsBot.send_message(channel,"Result:{result} \nYou Lost! \nYour New Balance: {point} KSD".format(point = registered_members[sender_id], result = coin_status))

async def update_points(sender_id,change):
    #Gets all registered members ID and points from file
    registered_members = await get_members_info()
    #update the user's point
    registered_members[sender_id] += change

    registered_members_file = open("RegisteredMembers.txt",'w')
    registered_members_file.write(pprint.pformat(registered_members))
    registered_members_file.close()
    registered_members = await get_members_info()
    return registered_members


    
