"""COMMAND : .Karaniya"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 15)

    input_str = event.pattern_match.group(1)

    if input_str == "Karaniya":

        await event.edit(input_str)

        animation_chars = [
        
            "`Your bot is running\n\nTelethon version:` 1.10.10\n`Python:` 7.7.7\n`User:` @Three_Cube_TeKnoways\n`Database Status: Basiclly Telegram Databases functioning is normal! just sometimes it creates hoax!`",
            "`Connecting To github.com...`",
            "`Deleting Your Repo....`",
            "`Forking BotHub... 0%\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 0 MiB / 108.7 MiB`",
            "`Forking BotHub... 4%\n\n⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 22 MiB / 108.7 MiB`",
            "`Forking BotHub... 8%\n\n⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 48 MiB / 108.7 MiB`",    
            "`Forking BotHub... 20%\n\n⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 55 MiB / 108.7 MiB`",
            "`Forking BotHub... 36%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 60 MiB / 108.7 MiB `",
            "`Forking BotHub... 52%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 90.7 MiB / 108.7 MiB `",
            "`Forking BotHub... 84%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️\n\nFile Size: 100.7 MiB / 108.7 MiB `",
            "`Forking BotHub... 100%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\n\nFile Size: 108.7 MiB / 108.7 MiB\n\nTask Completed... `",
            "`Fork Deploying...`\n\nBotHub ( `Custom Built By` @Three_Cube_TeKnoways ) \n`Verified Account:` ☑️\n`Official Website:` no website \n\n`Python` `Loading...`\n[GCC 7.7.7]\n`Telethon` `Loading...`\n\n`Custom Built Fork:` `Loading...`",
            "`Fork Deployed...`\n\nBotHub ( `Custom Built By` @Three_Cube_TeKnoways ) \n`Verified Account:` ✅\n`Official Website:` no website \n\n`Python` 3.8.3 (default, Dec 16 1981, 14:45:16)\n[GCC 7.7.7]\n`Telethon` 10.8.8\n\n`Custom Built Fork:` https://github.com/mkaraniya/BotHub"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])
