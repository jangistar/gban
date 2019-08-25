"""
AI based Replier Module for Userbot. //lazy af
cmd: .rep (to any text message)
usage-tips: Training Data is still not sufficient. so maybe bot wouldnt be that intelligent. But it is good for having some fun.
			English Language Only.
By: @Zero_cool7870
"""
from telethon import events
import asyncio
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
import os


bot= ChatBot('Bot')     #Prepare Bot
trainer = ChatterBotCorpusTrainer(bot)
bot_trained = False
corpus_path = '/app/english/'
if not bot_trained:							
	for file in os.listdir(corpus_path):
	    trainer.train(corpus_path + file)  #Train Bot
	bot_trained = True   
	print("Bot Trained")  

@borg.on(events.NewMessage(pattern=r"\.rep", outgoing=True))
async def chat_bot(event):
	if event.fwd_from:
		return  
	if bot_trained:    
		text = await event.get_reply_message()
		msg = str(text.message)
		reply = bot.get_response(msg)
		print(reply)
		await event.edit("**🤖Artificial Intelligence 🤖:\n"+str(reply)+"**")
	else:
		await event.edit("Hold On I am still Training Myself...")     
