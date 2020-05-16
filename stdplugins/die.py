""".die cmd to see if your userbot is ALIVE or Dead."""

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd
import uniborg
from os import remove
from platform import python_version, uname
from shutil import which
from telethon import version

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE

from shutil import which
from os import remove
from telethon import version

from platform import python_version, uname
from sample_config import Config


# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================


@borg.on(admin_cmd("die"))
async def amireallyalive(die):
    """ For .die command, check if the bot is running.  """
    await die.edit(
                     " Hey `i am ᗩᒪᓰᐺᘿ My 𝕄𝕒𝕤𝕥𝕖𝕣`\n"
                     f"`𝘪 𝙘𝙖𝙣'𝙩 Ðïê`\n"
                     f"------------------------------------ \n"
                     f"User: {DEFAULTUSER} \n"
                     f"🅲🆁🅴🅰🆃🅾🆁: @🄼🄰🅈🅄🅁_🄺🄰🅁🄰🄽🄸🅈🄰 ")    
                     

    
