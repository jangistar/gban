# Copyright (C) 2019 The Raphielscape Company LLC.

#

# Licensed under the Raphielscape Public License, Version 1.b (the "License");

# you may not use this file except in compliance with the License.

#

# The entire source code is OSSRPL except 'adminlist' which is MPL

# License: MPL and OSSRPL



""" Userbot module allowing you to get the admin list in a chat. """



from telethon.errors import ChatAdminRequiredError

from telethon.tl.types import ChannelParticipantsAdmins

from uniborg import HELPER

from uniborg.util import admin_cmd

from uniborg import *



@borg.on(admin_cmd("^.userslist ?(.*)"))

async def get_users(show):

    """ For .userslist command, list all of the users of the chat. """

    if not show.text[0].isalpha() and show.text[0] not in ("/", "#", "@", "!"):

        if not show.is_group:

            await show.edit("Are you sure this is a group?")

            return

        info = await show.client.get_entity(show.chat_id)

        title = info.title if info.title else "this chat"

        mentions = 'Users in {}: \n'.format(title)

        try:

            if not show.pattern_match.group(1):

                async for user in show.client.iter_participants(show.chat_id):

                    if not user.deleted:

                        mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"

                    else:

                        mentions += f"\nDeleted Account `{user.id}`"

            else:

                searchq = show.pattern_match.group(1)

                async for user in show.client.iter_participants(show.chat_id, search=f'{searchq}'):

                    if not user.deleted:

                        mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"

                    else:

                        mentions += f"\nDeleted Account `{user.id}`"

        except ChatAdminRequiredError as err:

            mentions += " " + str(err) + "\n"

        await show.edit(mentions)



HELPER.update({

    "userslist": ".userslist or .userslist <name>\ \nUsage: Retrieves all users in the chat."

})
