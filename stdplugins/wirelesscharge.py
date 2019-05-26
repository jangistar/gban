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




@borg.on(events.NewMessage(outgoing=True, pattern='^\.(f?f)wire'))

async def timer_blankx(e):

 txt=e.text[7:] + '\n\n`Wireless Telegram Phone Charging (beta) Started...\nBattery Percentage:` '

 j=10

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k+10

  await asyncio.sleep(10)

 if e.pattern_match.group(1) == 'f':

  await e.edit("`Wireless Charging (beta) Completed...\nBattery Percentage: 100%\nDevice Detected: Nokia 1100 (Space Grey Varient)` ")


