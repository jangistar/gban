""".on cmd to see if your userbot is ALIVE or Dead
.3 command, to print 3Cubes Logo in Ascii."""

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
async def amireallyalive(on):
    """ For .on command, check if the bot is running.  """
    await on.edit(
                     " Hey `i am 𝐎𝓷 My 𝕄𝕒𝕤𝕥𝕖𝕣`\n"
                     "`𝘪 𝙘𝙖𝙣'𝙩 Ðïê`")
                     " \n"
                     f"------------------------------------ \n"
                     f"U̴̧̡̫̤̦̇͆͛̿͑̈́̂̊̚͝s̷̡͓͎͘e̷̹̙̝̽̾͂ŕ̴̡̛̺̖̝̬̣͖͕̐̅͌͂͌̕: {DEFAULTUSER} \n"
                     f"🅲🆁🅴🅰🆃🅾🆁: @🄼🄰🅈🅄🅁_🄺🄰🅁🄰🄽🄸🅈🄰 \n"
                     

    
