"""Emoji

Available Commands:

.fgdrive"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 13)

    input_str = event.pattern_match.group(1)

    if input_str == "fgdrive":

        await event.edit(input_str)

        animation_chars = [
        
            "Downloading To Heroku Started...\n\n░░░░░░░░░░",
            "Downloading...\n\n█░░░░░░░░░",
            "Downloading...\n\n███░░░░░░░",
            "Downloading...\n\n█████░░░░░",
            "Downloading...\n\n█████████░",    
            "Download Completed.\n\n██████████",
            "Uploading To G-Drive Started...\n\n░░░░░░░░░░",
            "Uploading To G-Drive...\n\n█░░░░░░░░░",
            "Uploading To G-Drive...\n\n█████░░░░░",
            "Uploading To G-Drive...\n\n█████████░",
            "Uploading To G-Drive Completed.\n\n██████████",
            "Generating G-Drive link........",
            "[G-Drive Link](https://drive.google.com/a/oxford.edu.in/uc?id=1hn_VuI6WdVlg6oZb3t1ch0dZ-qA&export=download)
 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 13])
