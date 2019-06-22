"""

Memes Plugin for Userbot

usage = .meme someCharacter //default delay will be 3

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

    await event.edit("-------------------------------------------------"+memeVar)
    await event.edit("------------------------------------------------"+memeVar+"-")
    await event.edit("-----------------------------------------------"+memeVar+"--")
    await event.edit("----------------------------------------------"+memeVar+"---")
    await event.edit("---------------------------------------------"+memeVar+"----")
    await event.edit("--------------------------------------------"+memeVar+"-----")
    await event.edit("-------------------------------------------"+memeVar+"------")
    await event.edit("------------------------------------------"+memeVar+"-------")
    await event.edit("-----------------------------------------"+memeVar+"--------")
    await event.edit("----------------------------------------"+memeVar+"---------")
    await event.edit("---------------------------------------"+memeVar+"----------")
    await event.edit("--------------------------------------"+memeVar+"-----------")
    await event.edit("-------------------------------------"+memeVar+"------------")
    await event.edit("------------------------------------"+memeVar+"-------------")
    await event.edit("-----------------------------------"+memeVar+"--------------")
    await event.edit("----------------------------------"+memeVar+"---------------")
    await event.edit("---------------------------------"+memeVar+"----------------")
    await event.edit("--------------------------------"+memeVar+"-----------------")
    await event.edit("-------------------------------"+memeVar+"------------------")
    await event.edit("------------------------------"+memeVar+"-------------------")
    await event.edit("-----------------------------"+memeVar+"--------------------")
    await event.edit("----------------------------"+memeVar+"---------------------")
    await event.edit("---------------------------"+memeVar+"----------------------")
    await event.edit("--------------------------"+memeVar+"-----------------------")
    await event.edit("-------------------------"+memeVar+"------------------------")
    await event.edit("------------------------"+memeVar+"-------------------------")
    await event.edit("-----------------------"+memeVar+"--------------------------")
    await event.edit("----------------------"+memeVar+"---------------------------")
    await event.edit("---------------------"+memeVar+"----------------------------")     
    await event.edit("--------------------"+memeVar+"-----------------------------")
    await event.edit("-------------------"+memeVar+"------------------------------")
    await event.edit("------------------"+memeVar+"-------------------------------")
    await event.edit("-----------------"+memeVar+"--------------------------------")
    await event.edit("----------------"+memeVar+"---------------------------------")
    await event.edit("---------------"+memeVar+"----------------------------------")
    await event.edit("--------------"+memeVar+"-----------------------------------")
    await event.edit("-------------"+memeVar+"------------------------------------")
    await event.edit("------------"+memeVar+"-------------------------------------")
    await event.edit("-----------"+memeVar+"--------------------------------------")
    await event.edit("----------"+memeVar+"---------------------------------------")
    await event.edit("---------"+memeVar+"----------------------------------------")
    await event.edit("--------"+memeVar+"-----------------------------------------")
    await event.edit("-------"+memeVar+"------------------------------------------")
    await event.edit("------"+memeVar+"-------------------------------------------")
    await event.edit("-----"+memeVar+"--------------------------------------------")
    await event.edit("----"+memeVar+"---------------------------------------------")
    await event.edit("---"+memeVar+"----------------------------------------------")
    await event.edit("--"+memeVar+"-----------------------------------------------")
    await event.edit("-"+memeVar+"------------------------------------------------")
    await event.edit(memeVar+"----------------------------------------------------")
    await event.edit(memeVar)

    await asyncio.sleep(sleepValue)



"""

Bonus : Flower Boquee Generater

usage:- .flower



"""

@borg.on(events.NewMessage(pattern=r"\.chu", outgoing=True))

async def meme(event):

    if event.fwd_from:

        return   

    flower =" Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa ki unko ab bada loudha chahye ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain Aur agar tb b tjhe apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga!"

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
