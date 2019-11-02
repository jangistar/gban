"""use cmd .mayur
aaahaaa you can edit this 😉"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "mayur":

        await event.edit(input_str)

        animation_chars = [

            "👑Mayur👑👑👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑",

            "◼️👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑",

            "◼️◼️👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑",

            "◼️◼️◼️️👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑",

            "◼️◼️◼️◼️👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑",

            "‎◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Mayur👑👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑Mayur👑👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Mayur👑👑Mayur👑◼️◼️\n◼️👑Mayur👑👑Mayur👑👑Mayur👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Mayur👑👑Mayur👑◼️◼️\n◼️👑Mayur👑👑Mayur👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Mayur👑👑Mayur👑◼️◼️\n◼️👑Mayur👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Mayur👑👑Mayur👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑Mayur👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            "👑 MAYUR 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
