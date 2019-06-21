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

    animation_interval = 1.5

    animation_ttl = range(0, 13)

    input_str = event.pattern_match.group(1)

    if input_str == "music":

        await event.edit(input_str)

        animation_chars = [
            "⬤⬤⬤ 81%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",    
            "⬤⬤◯ 80%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80%\n\n⠀⠀⠀⠀⠀[RAVANA Music Player](t.me/r4v4n4)\n\n⠀⠀⠀⠀**Now Playing:Kamasutra BGM**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 13])

