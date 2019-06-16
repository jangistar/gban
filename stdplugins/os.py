"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "macos":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To MacOS...`",
            "`Initiating MacOs Login.`",
            "`Loading MacOS... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading MacOS... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading MacOS... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Loading MacOS... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading MacOS... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading MacOS... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading MacOS... 84%\n█████████████████████▒▒▒▒ `",
            "`Loading MacOS... 100%\n█████████████████████████ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: MacOS`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "windows":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Windows 10...`",
            "`Initiating Windows 10 Login.`",
            "`Loading Windows 10... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Loading Windows 10... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Windows 10... 84%\n█████████████████████▒▒▒▒ `",
            "`Loading Windows 10... 100%\n█████████████████████████ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Windows 10`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "linux":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Linux...`",
            "`Initiating Linux Login.`",
            "`Loading Linux... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Loading Linux... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Linux... 84%\n█████████████████████▒▒▒▒ `",
            "`Loading Linux... 100%\n█████████████████████████ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Linux`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "stock":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Symbian OS...`",
            "`Initiating Symbian OS Login.`",
            "`Loading Symbian OS... 0%\n█████████████████████████ `",
            "`Loading Symbian OS... 4%\n█████████████████████▒▒▒▒ `",
            "`Loading Symbian OS... 8%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Loading Symbian OS... 20%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Symbian OS... 36%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Symbian OS... 52%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Symbian OS... 84%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Loading Symbian OS... 100%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Symbian OS"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 3)

    input_str = event.pattern_match.group(1)

    if input_str == "os":

        await event.edit(input_str)

        animation_chars = [
        
            "`Scanning OS...`",
            "`Scanning OS......`",
            "`Current Loaded OS: Symbian OS\nTo Boot Other OS, Use The Following Trigger:\n✳️.macos\n✳️.windows\n✳️.linux\n✳️.stock `",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 3])
