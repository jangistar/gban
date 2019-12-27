
#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""it's to generate the replied users all profile pics that are not deleted
cmd is .PPS"""


import sys
import os
import datetime
import time
from telethon import events
from telethon.tl import functions, types
import asyncio
from telethon import utils
from uniborg.util import admin_cmd
import html
from html import *
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.tl.functions.account import *
from telethon.tl.functions.channels import *
from telethon.tl.functions.photos import *
from telethon.tl.types import *
from telethon import *


@borg.on(admin_cmd(pattern="PPS ?(.*)", allow_sudo=True))
async def _(event):
        """Gets the profile photos of replied users, channels or chats"""
        id = event.get_args_raw(event.message)
        user = await event.get_reply_message()
        chat = message.input_chat
        if user:
            photos = await event.get_profile_photos(user.sender)
        else:
            photos = await event.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.send_file(message.chat_id, photos)
            except a:
                photo = await event.download_profile_photo(chat)
                await event.send_file(message.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("<code>ID number you entered is invalid</code>")
                    return
            except:
                 await event.edit("<code>ID number you entered is invalid</code>")
                 return
            if int(id) <= (len(photos)):
                send_photos = await event.download_media(photos[id - 1])
                await event.send_file(message.chat_id, send_photos)
            else:
                await event.edit("<code>No photo found with that id</code>")
                return
    
