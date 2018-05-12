#WORK IN PROGRESS
#Music Functionality for KsBot

#Summoning Bot to voice channel
async def summon(bot,sender,channel_to_notify):
    KsBot = bot
    voice_channel_to_join = sender.voice_channel
    #For preventing errors
    #the voice channel is not a valid option
    if voice_channel_to_join == None:
        await KsBot.send_message(channel_to_notify,"Invalid Channel")
    KsBotVoice = await KsBot.join_voice_channel(voice_channel_to_join)
            
    
