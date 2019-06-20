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

    animation_interval = 1

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "music":

        await event.edit(input_str)

        animation_chars = [
            "@r4v4n4 Music Player\n⠀⠀⠀⠀Now Playing:Taki Taki\n00:00 ▱▱▱▱▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ▶️ ⏩️ ⏭️",
            "Now Playing:Taki Taki\n00:01 ▰▱▱▱▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏸️ ⏩️ ⏭️",
            "Now Playing:Taki Taki\n00:02 ▰▰▱▱▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏸️ ⏩️ ⏭️",
            "Now Playing:Taki Taki\n00:03 ▰▰▰▱▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏸️ ⏩️ ⏭️",
            "Now Playing:Taki Taki\n00:04 ▰▰▰▰▱▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏸️ ⏩️ ⏭️",
            "Now Playing:Taki Taki\n00:05 ▰▰▰▰▰▱▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏸️ ⏩️ ⏭️",    
            "Now Playing:Taki Taki\n00:06 ▰▰▰▰▰▰▱▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏸️ ⏩️ ⏭️",
            "Now Playing:Taki Taki\n00:07 ▰▰▰▰▰▰▰▱▱▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏸️ ⏩️ ⏭️",
            "Now Playing:Taki Taki\n00:08 ▰▰▰▰▰▰▰▰▱▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏸️ ⏩️ ⏭️",
            "Now Playing:Taki Taki\n00:09 ▰▰▰▰▰▰▰▰▰▱ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏸️ ⏩️ ⏭️",
            "Now Playing:Taki Taki\n00:10 ▰▰▰▰▰▰▰▰▰▰ 00:10\n\n⠀⠀⠀⠀⠀⏮️ ⏪️ ⏺️ ⏩️ ⏭️"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
