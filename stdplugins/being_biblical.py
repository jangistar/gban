"""Say something from the Holy Bible... Syntax: .BBL by @Mayur_Karaniya
|
Quotes credits: Being Biblical Channel : @BeingBiblical"""

from telethon import events

import asyncio

import os

import sys

import random



@borg.on(events.NewMessage(pattern=r"\.BBL", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("LAKHU CHU 1 MINUTE !...")

    await asyncio.sleep(1)

    x=(random.randrange(1,5))
    
    if x==1:
        
        await event.edit("`\"By faith Abraham, when he was called to go out into a place which he should after receive for an inheritance, obeyed; and he went out, not knowing whither he went.  <Hebrews 11:8>.\"`")
        
    if x==2:
        
        await event.edit("`\"By faith Noah, being warned of God of things not seen as yet, moved with fear, prepared an ark to the saving of his house; by the which he condemned the world, and became heir of the righteousness which is by faith.  <Hebrews 11:7>.\"`")
        
    if x==3:
        
        await event.edit("`\"These words spake Jesus, and lifted up his eyes to heaven, and said, Father, the hour is come; glorify thy Son, that thy Son also may glorify thee:  <John 17:1>.\"`")
        
    if x==4:
        
        await event.edit("`\"As thou hast given him power over all flesh, that he should give eternal life to as many as thou hast given him.  <John 17:2>.\"`")
        
