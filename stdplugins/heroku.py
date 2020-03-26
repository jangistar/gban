"""command: .heroku"""


from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd
import importlib.util
import asyncio
import random
import importlib.util
from datetime import datetime
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import git
import heroku3
import json

# ================= CONSTANT =================
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================

  
@borg.on(admin_cmd(pattern="heroku ?(.*)"))
async def heroku_manager(heroku):
    await heroku.edit("`Processing...`")
    await asyncio.sleep(3)
    conf = heroku.pattern_match.group(1)
    result = await subprocess_run(f'heroku ps -a {Config.HEROKU_APP_NAME}', heroku)
    if result[2] != 0:
        return
    hours_remaining = result[0]
    await heroku.edit('`' + hours_remaining + '`')
    return
