
""" Command: .pingme will show you your loop back ping..
edited by @Mayur_Karaniya"""

from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="pingme ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    start = datetime.now()
    mone = await event.reply("My 🇵 🇮 🇳 🇬  Is : Calculating...")
    end = datetime.now()
    ms = (end - start).microseconds * 0.00001
    await mone.edit("My 🇵 🇮 🇳 🇬  Is : {} ms".format(ms))
 
