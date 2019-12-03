from os import remove
from os import execl
import sys

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

# from uniborg import CMD_HELP, bot
# from uniborg.events import register


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

@borg.on(admin_cmd("king ?(.*)", outgoing=True))
async def king(e):
    await e.edit(
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒█▒▒█▒▒█▒"
        "\n▒█▒▒█▒▒█▒"
        "\n▒█▒▒█▒▒█▒"
        "\n▒▒██▒██▒▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒▒█████▒▒"
        "\n▒█▒▒▒▒▒█▒"
        "\n▒█▒▒▒▒▒█▒"
        "\n▒█▒▒▒▒▒█▒"
        "\n▒▒█████▒▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒▒▒█▒"
        "\n▒▒▒▒▒▒▒█▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒█▒"
        "\n▒▒▒▒▒▒▒█▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒█▒▒▒▒"
        "\n▒▒▒▒█▒▒▒▒"
        "\n▒▒▒▒█▒▒▒▒"
        "\n▒███████▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒▒██████▒"
        "\n▒█▒▒▒▒▒▒▒"
        "\n▒█▒▒▒▒▒▒▒"
        "\n▒█▒▒▒▒▒▒▒"
        "\n▒▒██████▒"
        "\n▒▒▒▒▒▒▒▒▒"
        "\n▒███████▒"
        "\n▒█▒▒█▒▒█▒"
        "\n▒█▒▒█▒▒█▒"
        "\n▒█▒▒█▒▒█▒"
        "\n▒▒██▒██▒▒"
        "\n▒▒▒▒▒▒▒▒▒")
        
