"""Get the info your system. Using .neofetch then .sysd"""
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.sysd", outgoing=True))
async def sysdetails(sysd):
    """ a. """
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            neo = "neofetch/neofetch --on --color_blocks on --bold on --cpu_temp=C \
                    --cpu_speed on --cpu_cores physical --kernel_shorthand on \
                    --gpu_brand on --refresh_rate on --gtk_shorthand on --colors=distro  --backend ascii \
                    --source=auto --Redhat source --stdout"
            fetch = await asyncrunapp(
                neo,
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) \
                + str(stderr.decode().strip())

            await sysd.edit("sysd Result: `" + result + "`")
        except FileNotFoundError:
            await sysd.edit("`Hey, on mkaraniya/BotHub install .neofetch first kthx`")

