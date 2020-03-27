
""" Command: .pingme will show you your loop back ping..
edited by @Mayur_Karaniya"""

from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd
from sample_config import Config

# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================




@borg.on(admin_cmd(pattern="pingme ?(.*)", allow_sudo=False))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    start = datetime.now()
    mone = await event.reply(f"{DEFAULTUSER}'s P I N G Is : Calculating...")
    end = datetime.now()
    ms = (end - start).microseconds * 0.00001
    await mone.edit(f"{DEFAULTUSER}'s P I N G Is : {} ms".format(ms)")
return
                    
