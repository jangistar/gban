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
    pattern = r"([a-zA-Z0-9 ]+)( #([r]|[R])equest)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([e]|[E])veryone)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([r]|[R])equest)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([o]|[O])ne)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([t]|[T])wo)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([h]|[H])elp)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([s]|[S])uccess)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([r]|[R])equesting)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([s]|[S])uccessful)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([s]|[S])uccessfully)($|[\n])"
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

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( ([s]|[S])orry)($|[\n])"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "**`don't be sorry bro it's ok now`**",
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
            
