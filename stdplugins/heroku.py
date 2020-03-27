"""command: .heroku"""


from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd
import importlib.util
import asyncio
import random
import importlib.util
from datetime import datetime
from random import randint
from asyncio import sleep
from os import execl
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import asyncio
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which, rmtree
from telethon import version
from os import remove, execle, path, makedirs, getenv, environ
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
import distutils
from uniborg.util import admin_cmd
from collections import deque
import sys
import os
import io
import git
import heroku3
import json
from sample_config import Config

# ================= CONSTANT =================
HEROKU_API_KEY = Config.HEROKU_API_KEY
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
Heroku = heroku3.from_key(HEROKU_API_KEY)
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================

async def subprocess_run(cmd, heroku):
    subproc = await asyncrunapp(cmd, stdout=asyncPIPE, stderr=asyncPIPE)
    stdout, stderr = await subproc.communicate()
    exitCode = subproc.returncode
    if exitCode != 0:
        await heroku.edit(
            '**An error was detected while running subprocess**\n'
            f'```exitCode: {exitCode}\n'
            f'stdout: {stdout.decode().strip()}\n'
            f'stderr: {stderr.decode().strip()}```')
        return exitCode
    return stdout.decode().strip(), stderr.decode().strip(), exitCode

  
@borg.on(admin_cmd(pattern="heroku ?(.*)"))
async def _event(heroku):
    await heroku.edit("`Processing...`")
    await asyncio.sleep(3)
    conf = heroku.pattern_match.group(1)
    result = await subprocess_run(f'heroku ps -a {HEROKU_APP_NAME}', heroku)
    if result[2] != 0:
        return
    hours_remaining = result[0]
    await heroku.edit('`' + hours_remaining + '`')
    return
