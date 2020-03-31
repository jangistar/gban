# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#-----------------
# from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
# from userbot.events import register
#------------

"""spam:
    .cspam <text>
Usage: Spam the text letter by letter.
.spam <count> <text>
Usage: Floods text in the chat !!
.wspam <text>
Usage: Spam the text word by word.
.picspam <count> <link to image/gif>
Usage: As if text spam was not enough !!
.delayspam <delay> <count> <text>
Usage: .bigspam but with custom delay.
NOTE : Spam at your own risk !!"
-
Copyright (C) 2019 The Raphielscape Company LLC.
"""

import asyncio
from asyncio import wait, sleep

from sample_config import Config
from uniborg.util import admin_cmd
import uniborg
import os

#----------------Basic Constants-------------------
BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
BOTLOG = Config.BOTLOG
#----------------Basic Constants-------------------


@borg.on(admin_cmd(pattern="cspam ?(.*)"))
async def tmeme(e):
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#CSPAM\n"
            "TSpam was executed successfully")


@borg.on(admin_cmd(pattern="wspam ?(.*)"))
async def tmeme(e):
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#WSPAM\n"
            "WSpam was executed successfully")


@borg.on(admin_cmd(pattern="spam ?(.*)"))
async def spammer(e):
    counter = int(e.pattern_match.group(1).split(' ', 1)[0])
    spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
    await e.delete()
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    if BOTLOG:
        await e.client.send_message(BOTLOG_CHATID, "#SPAM\n"
                                    "Spam was executed successfully")


@borg.on(admin_cmd(pattern="picspam ?(.*)"))
async def tiny_pic_spam(e):
    message = e.text
    text = message.split()
    counter = int(text[1])
    link = str(text[2])
    await e.delete()
    for i in range(1, counter):
        await e.client.send_file(e.chat_id, link)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#PICSPAM\n"
            "PicSpam was executed successfully")


@borg.on(admin_cmd(pattern="delayspam ?(.*)"))
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#DelaySPAM\n"
            "DelaySpam was executed successfully")

