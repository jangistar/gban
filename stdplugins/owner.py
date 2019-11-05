"""Available Commands:  .owner"""

from telethon import events

import asyncio




@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "owner":

        await event.edit(input_str)

        animation_chars = [
        
            "M\nA\nY\nU\nR",
            "T\nH\nE",
            "K\nI\nN\nG",
            "👑\nMAYUR THE KING 👑"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])
