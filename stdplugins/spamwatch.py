"""spamwatch for uniborg users. Credits : @By_Azade
cmd is .spamwatch, this was impossible without https://t.me/SitiSchu!."""

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
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins,
                               ChannelParticipantsBots, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto, PeerChat,
                               MessageService, MessageActionChatAddUser)
from telethon.tl.functions.contacts import DeleteContactsRequest

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
@borg.on(events.NewMessage())
async def spam_watch_(event):
    client = spamwatch.Client(Config.SPAM_WATCH_API)
    users = await get_user_from_event(event)
    for user in users:
        ban = client.get_ban(user.id)
        if event.chat_id != event.from_id and ban:
            try:
                await event.client(
                    EditBannedRequest(
                        event.chat_id,
                        user,
                        BANNED_RIGHTS
                    )
                )
                if isinstance(event, events.NewMessage.Event):
                    await event.delete()
                else:
                    return
            except BadRequestError:
                return
        elif ban:
            await event.client(BlockRequest(user))
            await event.client(DeleteContactsRequest(id=[user]))
        else:
            return
        if ENABLE_LOG:
            await event.client.send_message(
                LOGGING_CHATID,
                "#SPAM_WATCH_BAN\n" + \
                f"USER: [{user.first_name}](tg://user?id={user.id})\n" + \
                (f"CHAT: {event.chat.title}(`{event.chat_id}`)" if event.chat_id != event.from_id else "")
            )


async def get_user_from_event(event):
    user_obj = [await event.client.get_input_entity(event.from_id)]
    if isinstance(event, MessageService):
        if isinstance(event.action, MessageActionChatAddUser):
            user_obj.extend([await event.client.get_input_peer(x) for x in event.action.users])
    return user_obj
