"""COMMAND : .funny"""


from telethon import events
import random, re
from uniborg.util import admin_cmd

FUNNYREACTS = [
    ".eai",
    ".apm",
]



@borg.on(admin_cmd("funny ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(FUNNYREACTS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = FUNNYREACTS[bro]
    await event.edit(reply_text)
    
    
