# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
"""
This module generates the changelog for the userbot based on Upstream revision
cmd is .try
"""

from os import remove
from os import execl
import sys

import heroku3
import git
from git import Repo
from git.exc import GitCommandError
from git.exc import InvalidGitRepositoryError
from git.exc import NoSuchPathError

import asyncio
import random
import re
import time

from collections import deque

import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon import events

from uniborg.util import admin_cmd
# from uniborg import HEROKU_MEMEZ
# from uniborg import HEROKU_APIKEY
# from uniborg import HEROKU_APPNAME

from contextlib import suppress
import os
import sys
import asyncio

# from uniborg import CMD_HELP, bot, HEROKU_MEMEZ, HEROKU_APIKEY, HEROKU_APPNAME
# from userbot.events import register


async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


async def is_off_br(br):
    off_br = ['master']
    for k in off_br:
        if k == br:
            return 1
    return

@borg.on(admin_cmd("try ?(.*)", outgoing=True, allow_sudo=True))
async def upstream(ups):
    "For .update command, check if the bot is up to date, update if specified"
    await ups.edit("`Checking for updates, please wait....`")
    conf = ups.pattern_match.group(1).lower()
    off_repo = 'https://github.com/mkaraniya/BotHub.git'

    try:
        txt = "`Oops.. Updater cannot continue due to some problems occured`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.edit(f'{txt}\n`directory {error} is not found`')
        return
    except GitCommandError as error:
        await ups.edit(f'{txt}\n`Early failure! {error}`')
        return
    except InvalidGitRepositoryError:
        repo = Repo.init()
        await ups.edit(
            "`Warning: Force-Syncing to the latest stable code from repo.`\
            \nI may lose my downloaded files during this update."
        )
        origin = repo.create_remote('upstream', off_repo)
        origin.fetch()
        repo.create_head('master', origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if not await is_off_br(ac_br):
        await ups.edit(
            f'**[UPDATER]:**` Looks like you are using your own custom branch ({ac_br}). \
            in that case, Updater is unable to identify which branch is to be merged. \
            please checkout to any official branch`')
        return

    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if not changelog:
        await ups.edit(f'\n`Your BOT is` **up-to-date** `with` **{ac_br}**\n')
        return

    if conf != "now":
        changelog_str = f'**New UPDATE available for [{ac_br}]:\n\nCHANGELOG:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await ups.edit("`Changelog is too big, sending it as a file.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await ups.client.send_file(
                ups.chat_id,
                "output.txt",
                reply_to=ups.id,
            )
            remove("output.txt")
        else:
            await ups.edit(changelog_str)
        await ups.respond(
            "`do \".update now\" to update\nDon't if using Heroku`")
        return

    await ups.edit('`New update found, updating...`')
    ups_rem.fetch(ac_br)
    await ups.edit('`Successfully Updated!\n'
                   'Bot is restarting... Wait for a second!`')
    await install_requirements()
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    exit()

if Config.HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(Config.HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if Config.HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == Config.HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit("Invalid APP Name. Please set the name of your bot in heroku in the var HEROKU_APP_NAME.")
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://",
                    "https://api:" + Config.HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(deploy_start(tgbot, message, HEROKU_GIT_REF_SPEC, remote))

            else:
                await message.edit("Please create the var HEROKU_APP_NAME as the key and the name of your bot in heroku as your value.")
                return
        else:
            await message.edit(NO_HEROKU_APP_CFGD)
    else:
        await message.edit("No heroku api key found in HEROKU_API_KEY var")
        

def generate_change_log(git_repo, diff_marker):
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in git_repo.iter_commits(diff_marker):
        out_put_str += f"•[{repo_change.committed_datetime.strftime(d_form)}]: {repo_change.summary} <{repo_change.author}>\n"
    return out_put_str
    
async def deploy_start(tgbot, message, refspec, remote):
    await message.edit(RESTARTING_APP)
    await message.edit("restarted! do `.ping` to check if I am pinging?")
    await remote.push(refspec=refspec)
    await tgbot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    
