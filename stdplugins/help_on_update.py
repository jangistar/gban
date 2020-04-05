"""  syntax:
    .useit
    Usage: Provide links to update repo guides while you keep your changes on the floor.
 """
from math import ceil
import asyncio
import json
import random
import re
from telethon import events, custom
from uniborg.util import admin_cmd, humanbytes

from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
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



@borg.on(events.NewMessage(pattern=r"\.useit", outgoing=True))
async def usit(e):
    await e.edit(
        f"Here's something for {DEFAULTUSER} to use it for help_on_update on **BotHub**:\n"
        "\n[Windows Method](https://telegra.ph/How-to-keep-BotHub-repo-updated-while-keeping-your-changes-through-windows-cmd-method-04-01)"
        "\n[Termux Method](https://telegra.ph/How-to-keep-BotHub-repo-updated-while-keeping-your-changes-through-windows-cmd-method-04-01-2)"
        "\n[Kali Linux Method](https://telegra.ph/How-to-keep-BotHub-repo-updated-while-keeping-your-changes-through-windows-cmd-method-04-01-2)"
        "\n[Ubuntu Linux Method](https://telegra.ph/How-to-keep-BotHub-repo-updated-while-keeping-your-changes-through-Ubuntu-Terminal-method-04-01)"
        "\n[Special - Note](https://telegra.ph/Special-Note-11-02)")
    
@borg.on(events.NewMessage(pattern=r"\.puseit", outgoing=True))
async def pusit(f):
     result = builder.article(
    await f.edit(
        text="""Here's something for {DEFAULTUSER} to use it for help_on_update on **BotHub**""",
            buttons=[
                    [custom.Button.url("👤Contact Creator👤", "https://telegram.dog/Three_Cube_TeKnoways"), custom.Button.url(
                        "🎞My YouTube Channel🎞", "https://www.youtube.com/channel/UCeKQxQK7XZ3jGi3541uWATg?sub_confirmation=1")],
                    [custom.Button.url("🎛Source Code🎛", "https://github.com/mkaraniya/BotHub"), custom.Button.url(
                        "❕❗Deploy Me❗❕", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fmkaraniya%2FBotHub%2F&template=https%3A%2F%2Fgithub.com%2Fmkaraniya%2FBotHub%2F")],
                    [custom.Button.url("🔰Update Fork🔰", "tg://need_update_for_some_feature"), custom.Button.url(
                        "✳️Fork Boost✳️", "tg://some_unsupported_feature"), custom.Button.url(
                        "♻️Refresh Heroku♻️", "tg://some_unsupported_feature")]
               
                ],
                link_preview=True
            )
