[👑](https://telegram.dog/Three_Cube_TeKnoways_bot)

[@SpEcHlDe](https://telegram.dog/ShrimadhaVahdamirhS)

    Only two of the environment variables are mandatory.
    This is because of telethon.errors.rpc_error_list.ApiIdPublishedFloodError
        APP_ID: You can get this value from https://my.telegram.org
        API_HASH: You can get this value from https://my.telegram.org
    The userbot will work without setting the non-mandatory environment variables.
    Please report any issues to the support group: https://t.me/Bot_Hub_Official_Group.


design

The modular design of the project enhances your Telegram experience through plugins which you can enable or disable on demand.

Each plugin gets the borg, logger, Config, tgbot and storage magical variables to ease their use. Thus creating a plugin as easy as adding a new file under the plugin directory to do the job:

# stdplugins/myplugin.py
from telethon import events
from uniborg.util import admin_cmd

@borg.on(admin_cmd("hi"))
async def handler(event):
    await event.reply("hey")

learning

Check out the already-mentioned plugins directory, or some third-party plugins to learn how to write your own, and consider reading Telethon's documentation.

Note this is the fork of UNIBORG so most of the credits should be given to UNIBORG DEVELOPERS and TO Those who originally used their Brains to create very useful plugins to name them are two in my knowlegde Spechide and Jaskaran.
and yes our admin team also worked hard to make few things work on this so not forgeting BOTHUB TEAM.
