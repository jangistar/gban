"""Emoji

Available Commands:

.fleave"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "fleave":

        await event.edit(input_str)

        animation_chars = [
        
            "⬛⬛⬛
⬛⬛⬛
⬛⬛⬛",
            "⬛⬛⬛
⬛🔄⬛
⬛⬛⬛",
            "⬛⬆️⬛
⬛🔄⬛
⬛⬛⬛",
            "⬛⬆️↗️
⬛🔄⬛
⬛⬛⬛",
            "⬛⬆️↗️
⬛🔄➡️
⬛⬛⬛",    
            "⬛⬆️↗️
⬛🔄➡️
⬛⬛↘️",
            "⬛⬆️↗️
⬛🔄➡️
⬛⬇️↘️",
            "⬛⬆️↗️
⬛🔄➡️
↙️⬇️↘️",
            "⬛⬆️↗️
⬅️🔄➡️
↙️⬇️↘️",
            "↖️⬆️↗️
⬅️🔄➡️
↙️⬇️↘️",
            "**Chat Message Exported To** `./ravana/chatbackup/new.txt`",
            "__Legend is leaving this chat.....!__ @admin __Goodbye aren't forever..__"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
