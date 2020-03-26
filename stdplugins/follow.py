""" Userbot module for getting information about the social media. """

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from sample_config import Config
from uniborg.util import admin_cmd
import uniborg


# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================


@borg.on(admin_cmd(pattern="follow ?(.*)"))
async def follow(follow):
    """ For .follow command, check if the bot is running.  """
    await follow.edit(
                     f"`FOLLOW {DEFAULTUSER} ON` \n\n"
                     f"[InstaGram](https://www.instagram.com/mayur_karaniya) \n\n"
                     f"[FaceBook](https://www.facebook.com/mkaraniya) \n\n"
                     f"[YouTube](https://www.youtube.com/channel/UCeKQxQK7XZ3jGi3541uWATg?sub_confirmation=1) "
                     )    

