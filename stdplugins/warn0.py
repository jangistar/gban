# For @UniBorg

"""Countdown Commands

.timer

.fcd"""



from telethon import events

from datetime import datetime

from uniborg.util import admin_cmd

import importlib.util

import asyncio

import random

import importlib.util




@borg.on(events.NewMessage(outgoing=True, pattern='^\.(f?f)warn0'))

async def timer_blankx(e):

 txt=e.text[7:] + '\n\n`Warning....` '

 j=0

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k=0

  await asyncio.sleep(1)

 if e.pattern_match.group(1) == 'f':

  await e.edit("`Warning Resetted By Admin...\nYou Have  0/3  warnings...` ")

