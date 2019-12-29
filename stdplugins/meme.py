"""
Memes Plugin for Userbot
usage = .meme someCharacter //default delay will be 3

Bonus : Flower Boquee Generater
usage:- .flower


By : - @Zero_cool7870

"""
from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.meme", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return   
    memeVar = event.text
    sleepValue = 3
    memeVar = memeVar[6:] 
           
    await event.edit("-------------"+memeVar)
    await event.edit("------------"+memeVar+"-")
    await event.edit("-----------"+memeVar+"--")
    await event.edit("----------"+memeVar+"---")
    await event.edit("---------"+memeVar+"----")    
    await event.edit("--------"+memeVar+"-----")
    await event.edit("-------"+memeVar+"------")
    await event.edit("------"+memeVar+"-------")
    await event.edit("-----"+memeVar+"--------")
    await event.edit("----"+memeVar+"---------")
    await event.edit("---"+memeVar+"----------")
    await event.edit("--"+memeVar+"-----------")
    await event.edit("-"+memeVar+"------------")
    await event.edit(memeVar+"-------------")
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)

	
@borg.on(events.NewMessage(pattern=r"\.flower", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return   
    flower =" 🌹"
    sleepValue = 5
           
    await event.edit(flower+"        ")
    await event.edit(flower+flower+"       ")
    await event.edit(flower+flower+flower+"      ")
    await event.edit(flower+flower+flower+flower+"     ")
    await event.edit(flower+flower+flower+flower+flower+"    ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+"   ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+"  ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+" ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+flower)
    await asyncio.sleep(sleepValue)
    
@borg.on(events.NewMessage(pattern=r"\.resp", outgoing=True))
async def meme(event):
	if event.fwd_from:
		return   
	paytext=event.text[6:]
	pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*5, paytext*1,paytext*1, paytext*4, paytext*1, paytext*1, paytext*1)
	await event.edit(pay)    
        
    
