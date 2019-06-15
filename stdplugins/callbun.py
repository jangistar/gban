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

    animation_interval = 5

    animation_ttl = range(0, 10)

    input_str = event.pattern_match.group(1)

    if input_str == "/call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`User Authorised.`",
            "`Private VOIP Call Connected...`",
            "`Me Calling Pavel Durov Shukla....`",
            "`Me: Hello Sir, Please Ban This Guys Telegram Account.`",    
            "`Durov: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @r4v4n4",
            "`Durov: OMG!!! I Am FAN Of You Sir...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: See You Later Brah.`",
            "`Private VOIP Call Disconnected.`",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
