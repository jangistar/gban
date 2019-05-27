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




@borg.on(events.NewMessage(outgoing=True, pattern='^\.(f?h)eroku'))

async def timer_blankx(e):

 txt=e.text[7:] + '\n\n`Reatarting Heroku Dyno...` '

 j=0

 k=j

 for j in range(j):

  await e.edit(txt)

  k=k+10

  await asyncio.sleep(1)

 if e.pattern_match.group(1) == 'f':

  await e.edit("`Heroku Dyno Restarted`")

