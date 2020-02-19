"""spamwatch for uniborg users. Credits : @By_Azade"""

from asyncio import sleep
from os import remove
import asyncio
from telethon import events
from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (MessageTooLongError,
                                          UserIdInvalidError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins,
                               ChannelParticipantsBots, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto, PeerChat)

from sample_config import Config
from uniborg.util import admin_cmd
import spamwatch

ENABLE_LOG = True
LOGGING_CHATID = Config.PRIVATE_CHANNEL_BOT_API_ID
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

@borg.on(events.ChatAction())
async def spamwatch_(event):
    # user = await get_user_from_event(event)
    client = spamwatch.Client(Config.SPAMWATCH_API)
    # ban = client.get_ban(event.from_id)
    user = await event.get_user()
    if event.user_joined or event.user_added:
        try:
            ban = client.get_ban(event.action_message.from_id)
            if ban:
                await borg(EditBannedRequest(event.chat_id,event.action_message.from_id,BANNED_RIGHTS))
                await event.client.send_message(
                LOGGING_CHATID,
                "#SPAMWATCH\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)"
            )
            else:
                return
        except BadRequestError:
            return
        if ENABLE_LOG:
            await event.client.send_message(
                LOGGING_CHATID,
                "#SPAMWATCH_BAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)"
            )


# async def get_user_from_event(event):
#     if event.reply_to_msg_id:
#         previous_message = await event.get_reply_message()
#         user_obj = await event.client.get_entity(previous_message.from_id)
#     else:
#         user = event.pattern_match.group(1)
#         if user.isnumeric():
#             user = int(user)
#         if not user:
#             await event.edit("`Pass the user's username, id or reply!`")
#             return
#         if event.message.entities is not None:
#             probable_user_mention_entity = event.message.entities[0]

#             if isinstance(probable_user_mention_entity, MessageEntityMentionName):
#                 user_id = probable_user_mention_entity.user_id
#                 user_obj = await event.client.get_entity(user_id)
#                 return user_obj
#         try:
#             user_obj = await event.client.get_entity(user)
#         except (TypeError, ValueError) as err:
#             await event.edit(str(err))
#             return None
#     return user_obj

# async def get_user_from_id(user, event):
#     if isinstance(user, str):
#         user = int(user)
#     try:
#         user_obj = await event.client.get_entity(user)
#     except (TypeError, ValueError) as err:
#         await event.edit(str(err))
#         return None
#     return user_obj
