""".gban , .ungban"""

from asyncio import sleep
from os import remove
from telethon import events
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

@borg.on(admin_cmd(pattern="ungban ?(.*)", allow_sudo=True))
async def ungban(un_gbon):
    """ For .ungban command, Globaly ungbans the target in the userbot """
    # Admin or creator check
    chat = await un_gbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await un_gbon.edit(NO_ADMIN)
        return

    # If everything goes well...
    await un_gbon.edit("`Ungbanning...`")

    user = await get_user_from_event(un_gbon)
    user = user[0]
    if user:
        pass
    else:
        return

    try:
        await un_gbon.client(
            EditBannedRequest(un_gbon.chat_id, user.id, UNBAN_RIGHTS))
        await un_gbon.edit("```Ungbanned Successfully```")

        if BOTLOG:
            await un_gbon.client.send_message(
                BOTLOG_CHATID, "#UNGBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {un_gbon.chat.title}(`{un_gbon.chat_id}`)")
    except UserIdInvalidError:
        await un_gbon.edit("`Uh oh my ungban logic broke!`")


#@register(outgoing=True, pattern="^.gmute(?: |$)(.*)")
@borg.on(admin_cmd(pattern="gban ?(.*)", allow_sudo=True))
async def gban(gbon):
    """ For .gban command, globally bans the replied/tagged person """
    # Admin or creator check
    chat = await gbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
# Well
    if not admin and not creator:
        await gbon.edit(NO_ADMIN)
        return

    user = await get_user_from_event(gbon)
    user = user[0]
    if user:
        pass
    else:
        return

    result = await borg(functions.channels.GetAdminedPublicChannelsRequest())
    
    # Announce that we're going to whack the pest
    await gbon.edit("`Whacking the pest!`")

    try:
        await gbon.client(EditBannedRequest(results.chats.id, user.id,
                                           BANNED_RIGHTS))
    except BadRequestError:
        await gbon.edit(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await gbon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await gbon.edit(
            "`I dont have message nuking rights! But still he was gbanned!`")
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    await gbon.edit(f"`{str(user.id)}` was gbanned !!")
