""" this plugin is just for testing update but thou.. cmd is .hub,
and the output should be BOTHUB is main HUB. """

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "hub":

        await event.edit(input_str)

        animation_chars = [

            "_",

            "__",

            "___",

            "____",
            
            "_____",
            
            "______",
            
            "_______", 
           
            "BOTHUB is main HUB",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])

