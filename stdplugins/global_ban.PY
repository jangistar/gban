""".gban , .ungban"""

from asyncio import sleep
import requests
from os import remove
from telethon import events, errors, functions, types
from telethon.tl import functions, types
from platform import python_version, uname
from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (PeerChannel, ChannelParticipantsAdmins,
                               ChatAdminRights, ChatBannedRights,
                               MessageEntityMentionName, MessageMediaPhoto,
                               ChannelParticipantsBots)

from telethon.tl.functions.users import GetFullUserRequest

#from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
#from userbot.events import register

from telethon import events
import logging
import asyncio
from uniborg.util import admin_cmd
from telethon.tl import functions, types
from uniborg.util import admin_cmd
from platform import python_version, uname
from sample_config import Config
import io
import re


# ================= CONSTANT =================
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
# ================= CONSTANT =================

# =================== CONSTANT ===================
PP_TOO_SMOL = "`The image is too small`"
PP_ERROR = "`Failure while processing the image`"
NO_ADMIN = "`I am not an admin!`"
NO_PERM = "`I don't have sufficient permissions!`"
NO_SQL = "`Running on Non-SQL mode!`"

CHAT_PP_CHANGED = "`Chat Picture Changed`"
CHAT_PP_ERROR = "`Some issue with updating the pic,`" \
                "`maybe coz I'm not an admin,`" \
                "`or don't have enough rights.`"
INVALID_MEDIA = "`Invalid Extension`"


BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)


# ================================================

async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(' ', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj
  
@borg.on(events.NewMessage(incoming=True))
async def on_new_message(event):
#async def muter(moot):

    """ Used for deleting the messages of muted people """
    try:
        from sql_helpers.locks_sql import init_locks
        from sql_helpers.global_bans_sql import gban_user
    except AttributeError:
        return
    locked = init_locks(event.chat_id, reset=False)
    gbaned = gban_user(event.sender_id, name, reason=None)
    rights = ChatBannedRights(
        until_date=None,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True,
    )
    if locked:
        for i in locked:
            if str(i.sender) == str(event.sender_id):
                await event.delete()
                await event.client(
                    EditBannedRequest(event.chat_id, event.sender_id, rights))
    for i in gbaned:
        if i.sender == str(event.sender_id):
            await event.ban()


#@register(outgoing=True, pattern="^.ungmute(?: |$)(.*)")
#async def ungmoot(un_gmute):
@borg.on(events.NewMessage(pattern=r"\.ungban", outgoing=True))
async def _(event):
    """ For .ungban command, ungbans the target in the userbot """
    # Admin or creator check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await event.edit(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from sql_helpers.global_bans_sql import ungban_user
    except AttributeError:
        await event.edit(NO_SQL)
        return

    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return

    # If pass, inform and start ungmuting
    await event.edit('```Ungmuting...```')

    if ungban(user.id) is False:
        await event.edit("`Error! User probably not gbaned.`")
    else:
        # Inform about success
        await event.edit("```Ungbaned Successfully```")

        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, "#UNGBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)")


#@register(outgoing=True, pattern="^.gmute(?: |$)(.*)")
#async def gspider(gspdr):
@borg.on(events.NewMessage(pattern=r"\.gban", outgoing=True))
async def _(event):
    """ For .gban command, globally mutes the replied/tagged person """
    # Admin or creator check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await event.edit(NO_ADMIN)
        return

    # Check if the function running under SQL mode
    try:
        from sql_helpers.global_bans_sq import gban_user
    except AttributeError:
        await event.edit(NO_SQL)
        return

    user, reason = await get_user_from_event(event)
    if user:
        pass
    else:
        return

    # If pass, inform and start gmuting
    await event.edit("`Grabs a huge, sticky duct tape!`")
    if gban(user.id) is False:
        await event.edit(
            '`Error! User probably already gbaned.\nRe-rolls the tape.`')
    else:
        if reason:
            await event.edit(f"`Globally taped!`Reason: {reason}")
        else:
            await event.edit("`Globally taped!`")

        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, "#GBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)")
