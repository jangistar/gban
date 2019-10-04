"""Command: .repo, .screenshotrick"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("repo"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Link To The Custom Forked Repo:** https://github.com/ravana69/PornHub/ "
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd("screenshottrick"))
async def _(event):
    if event.fwd_from:
        return
    mentions = ".eval NO_OF_SCSS = 5
for I in range(NO_OF_SCSS):
  await event.client(functions.messages.SendScreenshotNotificationRequest(peer=event.chat_id, reply_to_msg_id=42))
await event.delete()"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
