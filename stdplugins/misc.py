
"""cmd : .bguide , .readme, .funny """

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 1)

    input_str = event.pattern_match.group(1)

    if input_str == "bguide":

        await event.edit(input_str)

        animation_chars = [

            "[BotHub's Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-11-06)",
            
            "[BotHub's README.md file](https://github.com/mkaraniya/BotHub/blob/master/README.md)"
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 3])




"""cmd : .readme """

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 1)

    input_str = event.pattern_match.group(1)

    if input_str == "readme":

        await event.edit(input_str)

        animation_chars = [

                       
            "[BotHub's README.md file](https://github.com/mkaraniya/BotHub/blob/master/README.md)",
            
            "[Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-11-06)"
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 3])


from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 2)

    input_str = event.pattern_match.group(1)

    if input_str == "funny":

        await event.edit(input_str)

        animation_chars = [

                       
            ".apm",
            
            ".eai"
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 2])






















