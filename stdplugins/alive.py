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
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version

from userbot import ALIVE_NAME


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


# @register(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd("alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await on.edit("`"
                     "i am alive My Mastor \n\n"
                     " \n\n"
                     f"Telethon version: {version.__version__} \n"
                     f"Python: {python_version()} \n"
                     f"------------------------------------ \n"
                     f"User: {DEFAULTUSER} \n"
                     " \n\n"
                     f"Creator: Mayur Karaniya \n"
                     " \n\n"
                     f"Owner: 3Cube TeKnoways \n"
                     " \n\n"
                     f"Userbot: testuserbot "
                     "`")    
