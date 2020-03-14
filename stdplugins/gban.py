# Credits to Anubis
# This is a troll indeed ffs *facepalm*

"""cmd is .gban reply user., but biggest problem is you can't ungban that person,, rest enjoy for now 
Credits to Anubis"""

import asyncio
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("gban"))
async def gban(event):
    if event.fwd_from:
        return
    gbanVar = event.text
    gbanVar = gbanVar[6:]
    mentions = "`Warning!! User is Globally 𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n`"
    no_reason = "__Reason: forgot to add reason. __"
    await event.edit("**Kicking this person out ❗️⚜️☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 236390091:
            await reply_message.reply("`Wait a sec., This is my Master!`\n**How dare you threaten to ban my Master !**\n\n__Your account has been hacked! Pay 999$ to my Master__ [3Cube](tg://user?id=236390091) __to release your account__😏")
        else:
            jnl=("`Warning!! `"
                  "[{}](tg://user?id={})"
                  "` Globally 𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n\n`"
                  "**User's Name: ** __{}__\n"
                  "**ID : ** `{}`\n"
                ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**🤮's username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**🤮's username** : @{}\n".format(usname)
            if len(gbanVar) > 0:
                gbanm = "`{}`".format(gbanVar)
                gbanr = "**Reason: **"+gbanm
                jnl += gbanr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "`Warning!! User is Globally 𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\nReason: forgot to add reason. `"
        await event.reply(mention)
    await event.delete()
