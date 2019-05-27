#

# Copyright (c) Gegham zakaryan | 2019

#

import language_check



from telethon import events

from uniborg.util import admin_cmd

from uniborg import *



@borg.on(admin_cmd("^.fix( (.*))?"))

async def grammar_check(to_fix):

    if not to_fix.text[0].isalpha() and to_fix.text[0] not in ("/", "#", "@", "!"):

        reply = False

        textx = await to_fix.get_reply_message()

        if textx:

            message = str(textx.message)

            reply = True

        elif to_fix.pattern_match.group(2):

            message = to_fix.pattern_match.group(2)

        else:

            await to_fix.edit(

                "```Give a text to fix!\nReplying to your message will fix "

                "and edit it, while giving an inline text will output the "

                "fixed version of it.```"

            )



        tool = language_check.LanguageTool('en-GB')

        matches = tool.check(message)

        result = language_check.correct(message, matches)



        if reply:

            me = await event.get_me()



            if textx.from_id == me.id:

                await textx.edit(result)

                await to_fix.delete()

            else:

                await to_fix.edit("Did you mean? \n\n`" + result)

        else:

            await to_fix.edit(result)
