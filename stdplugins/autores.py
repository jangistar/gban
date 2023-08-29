"""Auto-responder edited by `@Three_Cube_TeKnoways.`
YOUR <msg/request text> #request/request/one/two/help/everyone/success to see the magic."""

#regex ([a-zA-Z0-9 ]+)( #([r]|[R])equest)($|[\n])

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([r]|[R])equest)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`Your request has been received, It will be fulfilled ASAP.`\n`Please don't send a duplicate request within 3 weeks.`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )

            
#regex ([a-zA-Z0-9 ]+)( ([e]|[E])veryone)($|[\n])


@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([e]|[E])veryone)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`'Hey you'`.\n`Don't be formal just start🛫 your query🗣 by userself with typing` `**/notes**.`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=True
            )
            
#regex ([a-zA-Z0-9 ]+)( ([r]|[R])equest)($|[\n])


@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"((#([r]|[R])equest))"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`Your request has been received, It will be fulfilled ASAP`.\n`Please don't send a duplicate request within 3 weeks.`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )

#regex ([a-zA-Z0-9 ]+)( ([o]|[O])ne)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([o]|[O])ne)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`One, two, Buckle my shoe`;\n`Three, four, Knock at the door;`\n`Five, six, Pick up sticks;`\n`Seven, eight, Lay them straight:`\n`Nine, ten, A big fat hen;`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=True
            )


#regex ([a-zA-Z0-9 ]+)( ([t]|[T])wo)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([t]|[T])wo)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`One, two, Buckle my shoe`;\n`Three, four, Knock at the door;`\n`Five, six, Pick up sticks;`\n`Seven, eight, Lay them straight:`\n`Nine, ten, A big fat hen;`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=True
            )


#regex ([a-zA-Z0-9 ]+)( ([h]|[H])elp)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([h]|[H])elp)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`There is only one way you are helped`\n`& that is either you pay💰 for it or you wait⏱ for someone👨🏻‍⚖️ to respond to it`\n`which-ever-way you wish`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )


#regex ([a-zA-Z0-9 ]+)( ([s]|[S])uccess)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([s]|[S])uccess)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`Success & Failiar is the part of life`\n`So, don't get excited when you Succeed`\n`& when you Fail, don't go the other way too 😉.`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )

#regex ([a-zA-Z0-9 ]+)( ([r]|[R])equesting)($|[\n])


@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([r]|[R])equesting)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`please use /notes, for your own 📕knowledge`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )


#regex ([a-zA-Z0-9 ]+)( ([s]|[S])uccessful)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([s]|[S])uccessful)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`Success & Failiar is the part of life`\n`So, don't get excited when you Succeed`\n`& when you Fail, don't go the other way too 😉.`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )



#regex ([a-zA-Z0-9 ]+)( ([s]|[S])uccessfully)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([s]|[S])uccessfully)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "`Success & Failiar is the part of life`\n`So, don't get excited when you Succeed`\n`& when you Fail, don't go the other way too 😉.`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )

#regex ([a-zA-Z0-9 ]+)( ([s]|[S])orry)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([s]|[S])orry)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "**`don't be sorry bro it's ok now`**\n`But if it still hurts you`/n`you can always pay us money`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )
            
#regex ([a-zA-Z0-9 ]+)( ([h]|[H])i)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([h]|[H])i)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "**`We can't help you if you don't describe your problems.`**\n`We're not psychic.`\n`Please read (nohello.net)[nohello.net] to see why it makes no sense to send a "hi, I have a problem" message.`/n`(https://dl.dropboxusercontent.com:443/s/xmtnzyz5b5b2tx4/2_541175087705893845.webp)`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )
            
#regex ([a-zA-Z0-9 ]+)( ([h]|[H])ello)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([h]|[H])ello)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "**`We can't help you if you don't describe your problems.`**\n`We're not psychic.`\n`Please read (nohello.net)[nohello.net] to see why it makes no sense to send a "hi, I have a problem" message.`/n`(https://dl.dropboxusercontent.com:443/s/xmtnzyz5b5b2tx4/2_541175087705893845.webp)`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )
            
#regex ([a-zA-Z0-9 ]+)( ([h]|[H])owdy)($|[\n])



@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"(([h]|[H])owdy)"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "**`We can't help you if you don't describe your problems.`**\n`We're not psychic.`\n`Please read (nohello.net)[nohello.net] to see why it makes no sense to send a "hi, I have a problem" message.`/n`(https://dl.dropboxusercontent.com:443/s/xmtnzyz5b5b2tx4/2_541175087705893845.webp)`",
            reply_to=message_id
        )
        """await event.client.send_message(
            -346103366,
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )"""
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=-346103366,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )
            
