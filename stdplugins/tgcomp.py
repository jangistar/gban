#

# Copyright (c) TelegramCompanion | 2019

#



import urllib

import re

import emoji

import aiohttp

import bs4

from telethon import events

from uniborg import HELPER

from telethon.tl.functions.messages import GetStickerSetRequest

from telethon.tl.types import (DocumentAttributeFilename,

                               InputMediaUploadedDocument,

                               InputStickerSetShortName,

                               MessageMediaPhoto,

                               InputStickerSetID)

from telethon.tl.types import DocumentAttributeSticker

from uniborg.util import admin_cmd

from uniborg import *





@borg.on(admin_cmd("^.gstfy$"))

async def gangstafy_text(event):

    message = None

    split_text = event.text.split(None, 1)

    if event.reply_to_msg_id:

        rep_msg = await event.get_reply_message()

        message = rep_msg.text

    elif len(split_text) == 1:

        await client.update_message(event, "...")

        return



    elif not message:

        await client.update_message(event, "`Unsuported message`")

        return

    else:

        message = split_text[1]

    await client.update_message(event, await __gangsafy(message))



#===============FUNCTION HELPERS=================================#

async def __gangsafy(text):

    urls = ("http", "www.", "https")

    if text.startswith(urls):

        params = {"search": __remove_emojis(text)}

        return "http://www.gizoogle.net/tranzizzle.php?{}".format(urllib.parse.urlencode(params))

    params = {"translatetext": __remove_emojis(text)}

    target_url = "http://www.gizoogle.net/textilizer.php"

    async with aiohttp.ClientSession() as session:

        async with session.post(target_url, data=params) as response:

            soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', await response.text())

    soup = bs4.BeautifulSoup(soup_input, "lxml")

    giz = soup.find_all(text=True)

    giz_text = giz[39].strip("\r\n")

    return giz_text



def __remove_emojis(text):

    clean_text = text

    for char in text:

        if char in list(emoji.EMOJI_UNICODE.values()):

            clean_text = re.sub(char, "", clean_text)

    return clean_text



@borg.on(admin_cmd("^.packinfo$"))

async def get_pack_info(event):

    if not event.is_reply:

        await event.update_message(event, PACKINFO_HELP)

        return

    rep_msg = await event.get_reply_message()

    if not rep_msg.document:

        await event.update_message(event, "`Reply to a sticker to get the pack details`")

        return

    stickerset_attr = rep_msg.document.attributes[1]

    if not isinstance(stickerset_attr, DocumentAttributeSticker):

        await event.update_message(event, "`Not a valid sticker`")

        return

    get_stickerset = await event(GetStickerSetRequest(InputStickerSetID(id=stickerset_attr.stickerset.id, access_hash=stickerset_attr.stickerset.access_hash)))

    pack_emojis = []

    for document_sticker in get_stickerset.packs:

        if document_sticker.emoticon not in pack_emojis:

            pack_emojis.append(document_sticker.emoticon)

    OUTPUT = f"**Sticker Title:** `{get_stickerset.set.title}\n`" \

             f"**Sticker Short Name:** `{get_stickerset.set.short_name}`\n" \

             f"**Official:** `{get_stickerset.set.official}`\n" \

             f"**Archived:** `{get_stickerset.set.archived}`\n" \

             f"**Stickers In Pack:** `{len(get_stickerset.packs)}`\n" \

             f"**Emojis In Pack:** {' '.join(pack_emojis)}"

    await event.edit(OUTPUT)



HELPER.update(

    {"gstfy": "gangstafy the text"}

)

HELPER.update(

    {"packinfo": "send sticker packinfo"}

)
