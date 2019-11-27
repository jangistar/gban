""" displays the Truth
use cmd .ok"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.05
    animation_ttl = range(0, 90)
    input_str = event.pattern_match.group(1)
    if input_str == "ok":
        await event.edit(input_str)
        animation_chars = [
            "B",
            "O",
            "T",
            "H",
            "U",
            "B",
            "I",
            "S",
            "T",
            "H",
            "E",
            "B",
            "E",
            "S",
            "T",
            "BOTHUB IS THE BEST , 0K Sir 😇"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 78])
