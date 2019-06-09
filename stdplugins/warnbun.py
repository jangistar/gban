#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @madarchod

from telethon import events
import random
import asyncio

@borg.on(events.NewMessage(pattern=r"\.warn (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "1":
        emoticons = [
            "`You Have  1/3  warnings...\nWatch out!....\nReason for last warn: Porn Demand`"
        ]
    elif input_str in "2":
        emoticons = [
            "`You Have  2/3  warnings...\nWatch out!....\nReason for last warn: Porn Demand`"
        ]
    elif input_str in "3":
        emoticons = [
            "`You Have  3/3  warnings...\nBanned!!!....\nReason for ban: Porn Demand`"
        ]
    elif input_str in "0":
        emoticons = [
            "`Warning Resetted By Admin...\nYou Have  0/3  warnings`"
        ]
    elif input_str in "bun":
        emoticons = [
            "`Warning!! User Gbanned By Admin...\nReason: Potential Spammer. `"
    else:    
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀̿Ĺ̯▀̿ ̿)",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)
