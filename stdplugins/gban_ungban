"""Globally Ban users from all the Group Administrations where you are SUDO.
.gban REASON
.ungban REASON"""

from telethon import events
import asyncio
from uniborg.util import admin_cmd
from sample_config import Config

@borg.on(admin_cmd(pattern="gban ?(.*)", allow_sudo=True))
async def _(event):
    if Config.G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            Config.G_BAN_LOGGER_GROUP,
            ".ban 🤮 [{}](tg://user?id={}) `{}`".format(r_from_id, reason)
        )
    await asyncio.sleep(5)
    await event.delete()


@borg.on(admin_cmd(pattern="ungban ?(.*)", allow_sudo=True))
async def _(event):
    if Config.G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            Config.G_BAN_LOGGER_GROUP,
            ".unban 🤠 [{}](tg://user?id={}) `{}`".format(r_from_id, reason)
        )
    await asyncio.sleep(5)
    await event.delete()
