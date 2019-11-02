"""COMMAND : .eye"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "eye":

        await event.edit(input_str)

        animation_chars = [

            "✋🏻\n  🇮🇳  =====> By faith Enoch was translated so that he did not see death, ",
            "✋🏻\n  🇮🇳  =====> and was not found because God had translated him; ",    
            "✋🏻\n  🇮🇳  =====> for before his translation he had this testimony, ",
            "✋🏻\n  🇮🇳  =====> that he pleased God. ",
            "✋🏻\n  🇮🇳  =====> But without faith it is impossible to please Him. ",    
            "✋🏻\n  🇮🇳  =====> It is the will of God that ",
            "✋🏻\n  🇮🇳  =====> we learn to walk in a manner pleasing to the Lord: ",
            "✋🏻\n  🇮🇳  =====> that you may have a walk worthy of the Lord, ",    
            "✋🏻\n  🇮🇳  =====> fully pleasing Him",
            "✋🏻\n  🇮🇳  =====> Hi All, How Are You Guys,, Praise The Lord..."
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
