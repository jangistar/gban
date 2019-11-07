"""Reply to a user to .premote them in the current chat
and to just prank do .prankpremote"""
from telethon import events
import asyncio,re
from datetime import datetime
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from uniborg.util import admin_cmd


@borg.on(admin_cmd("premote ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    to_premote_id = None
    rights = ChatAdminRights(
        change_info=False,
        post_messages=True,
        edit_messages=True,
        delete_messages=True,
        ban_users=True,
        invite_users=True,
        pin_messages=True,
        add_admins=False,
    )
    rank = await event.user
    if not rank:
        # Just in case.
        rank = "admin"
    else:
        return
    input_str = event.pattern_match.group(1)
    reply_msg_id = event.message.id
    if reply_msg_id:
        r_mesg = await event.get_reply_message()
        to_premote_id = r_mesg.sender_id
    elif input_str:
        to_premote_id = input_str
    try:
        await borg(EditAdminRequest(event.chat_id, to_premote_id, rights, rank))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("Successfully premoted")


@borg.on(admin_cmd("prankpremote ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    to_premote_id = None
    rights = ChatAdminRights(
        post_messages=True
    )
    rank = await event.user
    if not rank:
        # Just in case.
        rank = "admin"
    else:
        return
    input_str = event.pattern_match.group(1)
    reply_msg_id = event.message.id
    if reply_msg_id:
        r_mesg = await event.get_reply_message()
        to_premote_id = r_mesg.sender_id
    elif input_str:
        to_premote_id = input_str
    try:
        await borg(EditAdminRequest(event.chat_id, to_premote_id, rights, rank))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("Successfully premoted")
