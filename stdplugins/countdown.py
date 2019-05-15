# For @UniBorg

"""Countdown Command

.timer"""



from telethon import events

from datetime import datetime

from uniborg.util import admin_cmd

import importlib.util

import asyncio

import random

import importlib.util





@borg.on(events.NewMessage(outgoing=True, pattern='^\.(f?t)imer '))

async def timer_blankx(e):

 txt=e.text[7:] + '\nDeleting in '

 j=9000

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k-1

  await asyncio.sleep(10)

 if e.pattern_match.group(1) == 't':

  await e.delete()

 else:

  await e.edit(txt + 'NaN')
