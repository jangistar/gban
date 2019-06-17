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

    animation_ttl = range(0, 13)

    input_str = event.pattern_match.group(1)

    if input_str == "baalaji":

        await event.edit(input_str)

        animation_chars = [
        
            "`Your bot is running\n\nTelethon version:` 1.9.0\n`Python:` 3.7.3\n`User:` @r4v4n4\n`Database Status: Databases functioning normally!`",
            "`Connecting To github.com...`",
            "`Deleting Baalaji Repo....`",
            "`Forking Uniborg... 0%\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ `",
            "`Forking Uniborg... 4%\n\n⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ `",
            "`Forking Uniborg... 8%\n\n⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ `",    
            "`Forking Uniborg... 20%\n\n⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ `",
            "`Forking Uniborg... 36%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ `",
            "`Forking Uniborg... 52%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️ `",
            "`Forking Uniborg... 84%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️ `",
            "`Forking Uniborg... 100%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\n\nTask Completed... `",
            "`Fork Deploying...`\n\n@UniBorg ( `Custom Built By` @r4v4n4 ) \n`Verified Account:` ✔️\n`Official Website:` https://ravanaisdrunk.site.live\n\n`Python` Loading...\n[GCC 7.3.0]\n`Telethon` Loading...\n\n`Custom Built Fork:` Loading...",
            "`Fork Deployed...`\n\n@UniBorg ( `Custom Built By` @r4v4n4 ) \n`Verified Account:` ✅\n`Official Website:` https://ravanaisdrunk.site.live\n\n`Python` 3.6.8 (default, Jan 29 2019, 19:35:16)\n[GCC 7.3.0]\n`Telethon` 1.8.0\n\n`Custom Built Fork:` https://github.com/ravana69/UniBorg"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 13])
