# Copyright (C) 2020 BotHub.
#
# You can find misc modules, which dont fit in anything xD

"""
.bguide command, returns BotHub's basic setup-guide.
.readme command, returns Bothub's Readme Url from git.
.community command, just returns OG Uniborg's group link.
.support command, just returns the group link.
.myrepo command, just returns the user's personal repo URL. 
.creator command, returns the name of the creator of this BotHub bot.
.user command, returns the name of the person who is using it.
"""

from telethon import events
from github import Github
import aiohttp
import asyncio
import os
import time
from datetime import datetime
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
from sample_config import Config
from uniborg.util import admin_cmd, humanbytes, progress, time_formatter

import asyncio
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from uniborg.util import progress, is_read, humanbytes, time_formatter, admin_cmd
from platform import python_version, uname
from sample_config import Config

# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================




@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 1)

    input_str = event.pattern_match.group(1)

    if input_str == "bguide":

        await event.edit(input_str)

        animation_chars = [

            "[BotHub's Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-11-06)",
            
            "[BotHub's README.md file](https://github.com/mkaraniya/BotHub/blob/master/README.md)"
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 3])




@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.8

    animation_ttl = range(0, 1)

    input_str = event.pattern_match.group(1)

    if input_str == "readme":

        await event.edit(input_str)

        animation_chars = [

                       
            "[BotHub's README.md file](https://github.com/mkaraniya/BotHub/blob/master/README.md)",
            
            "[Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-11-06)"
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 3])


from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 1)

    input_str = event.pattern_match.group(1)

    if input_str == "FUnny":

        await event.edit(input_str)

        animation_chars = [

            ".eai",

            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 2])


from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 1)

    input_str = event.pattern_match.group(1)

    if input_str == "FUnny":

        await event.edit(input_str)

        animation_chars = [

           

            ".apm"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 2])










#@register(outgoing=True, pattern="^.community$")
@borg.on(admin_cmd(pattern="community ?(.*)", allow_sudo=False))
async def bot_community(community):
    await community.edit(
        "Join SpEcHlDe's Uniborg userbot community: https://t.me/SpEcHlDe"
        "\nDo note that BotHub is an unoficial fork of their "
        "Uniborg project and it may get limited or no support for bugs from them.")


#@register(outgoing=True, pattern="^.support$")
@borg.on(admin_cmd(pattern="support ?(.*)", allow_sudo=False))
async def bot_support(wannahelp):
    await wannahelp.edit(
        "Join the BotHub Channel: https://t.me/Bot_Hub_Official_Group : @Bot_Hub_Official_Group \
        \nJoin the BotHub Chat: https://t.me/Bot_Hub_Official : @Bot_Hub_Official")


#@register(outgoing=True, pattern="^.creator$")
@borg.on(admin_cmd(pattern="creator ?(.*)", allow_sudo=False))
async def creator(e):
    await e.edit("[TeKnoways](https://t.me/Three_Cube_TeKnoways)")
    
#@register(outgoing=True, pattern="^.user$")
@borg.on(admin_cmd(pattern="user ?(.*)", allow_sudo=False))
async def user(e):
    await e.edit(
        f"{DEFAULTUSER}")




