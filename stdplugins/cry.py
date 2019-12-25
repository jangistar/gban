"""Use cmd `.cry` to cry
Remastered by @AyushChatterjee"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1
    

    animation_ttl = range(0, 105)

    input_str = event.pattern_match.group(1)

    if input_str == "cry":

        await event.edit(input_str)

        animation_chars = [
            ";__;",
            ";___;",
            ";____;",
            ";_____;",
            ";______;",
            ";_______;",
            ";________;",
            ";_________;",
            ";__________;",
            ";___________;",
            ";____________;",
            ";_____________;",
            ";______________;",
            ";_______________;",
            ";________________;",
            ";_________________;",
            ";__________________;",
            ";___________________;",
            ";____________________;",
            ";_____________________;",
            ";____________________;",
            ";___________________;",
            ";__________________;",
            ";_________________;",
            ";________________;",
            ";_______________;",
            ";______________;",
            ";_____________;",
            ";____________;",
            ";___________;",
            ";__________;",
            ";_________;",
            ";________;",
            ";_______;",
            ";______;",
            ";_____;",
            ";____;",
            ";___;",
            ";__;",
            "`You made me CRY`",
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 45])
