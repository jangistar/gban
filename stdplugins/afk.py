# Credits to https://t.me/anubisxx for this plugin


"""AFK Plugin for @UniBorg
Syntax: .afkb REASON"""
import asyncio
from asyncio import sleep
import datetime
import shutil 
import random, re
from random import choice, randint
import time
from time import gmtime, strftime
from datetime import timedelta
from datetime import datetime
from telethon import events
from telethon.tl import functions, types
from uniborg.util import progress, is_read, humanbytes, time_formatter, admin_cmd
from sample_config import Config
from platform import python_version, uname

# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================

# ========================= CONSTANTS ============================
AFKSTR = [
    "`I'm busy right now. Please talk in a bag and when I come back you can just give me the bag!`",
    "I'm away right now. If you need anything, leave a message after the beep:\n`beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep`!",
    "`You missed me, next time aim better.`",
    "`I'll be back in a few minutes and if I'm not...,\nwait longer.`",
    "`I'm not here right now, so I'm probably somewhere else.`",
    "`Roses are red,\nViolets are blue,\nLeave me a message,\nAnd I'll get back to you.`",
    "`Sometimes the best things in life are worth waiting for…\nI'll be right back.`",
    "`I'll be right back,\nbut if I'm not right back,\nI'll be back later.`",
    "`If you haven't figured it out already,\nI'm not here.`",
    "`Hello, welcome to my away message, how may I ignore you today?`",
    "`I'm away over 7 seas and 7 countries,\n7 waters and 7 continents,\n7 mountains and 7 hills,\n7 plains and 7 mounds,\n7 pools and 7 lakes,\n7 springs and 7 meadows,\n7 cities and 7 neighborhoods,\n7 blocks and 7 houses...\n\nWhere not even your messages can reach me!`",
    "`I'm away from the keyboard at the moment, but if you'll scream loud enough at your screen, I might just hear you.`",
    "`I went that way\n---->`",
    "`I went this way\n<----`",
    "`Please leave a message and make me feel even more important than I already am.`",
    "`I am not here so stop writing to me,\nor else you will find yourself with a screen full of your own messages.`",
    "`If I were here,\nI'd tell you where I am.\n\nBut I'm not,\nso ask me when I return...`",
    "`I am away!\nI don't know when I'll be back!\nHopefully a few minutes from now!`",
    "`I'm not available right now so please leave your name, number, and address and I will stalk you later.`",
    "`Sorry, I'm not here right now.\nFeel free to talk to my userbot as long as you like.\nI'll get back to you later.`",
    "`I bet you were expecting an away message!`",
    "`Life is so short, there are so many things to do...\nI'm away doing one of them..`",
    "`I am not here right now...\nbut if I was...\n\nwouldn't that be awesome?`",
]
# ============================================

global USER_AFKB  # pylint:disable=E0602
global afkb_time  # pylint:disable=E0602
global last_afkb_message  # pylint:disable=E0602
global afkb_start
global afkb_end
USER_AFKB = {}
afkb_time = None
last_afkb_message = {}
afkb_start = {}

AFKSK = str(choice(AFKSTR))

@borg.on(events.NewMessage(pattern=r"\.afkb ?(.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    global USER_AFKB  # pylint:disable=E0602
    global afkb_time  # pylint:disable=E0602
    global last_afkb_message  # pylint:disable=E0602
    global afkb_start
    global afkb_end
    global reason
    USER_AFKB = {}
    afkb_time = None
    last_afkb_message = {}
    afkb_end = {}
    start_1 = datetime.now()
    afkb_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    if not USER_AFKB:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(
                types.InputPrivacyKeyStatusTimestamp()
            )
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afkb_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFKB = f"yes: {reason}"  # pylint:disable=E0602
        if reason:
            await borg.send_message(event.chat_id, f"**My King 👑 {DEFAULTUSER} 👑 is Going afk!** __because ~ {reason}__")
        else:
            await borg.send_message(event.chat_id, f"**My King 👑 {DEFAULTUSER} 👑 is Going afk!**")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                f"Set AFK mode to True, and Reason is {reason}"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afkb(event):
    global USER_AFKB  # pylint:disable=E0602
    global afkb_time  # pylint:disable=E0602
    global last_afkb_message  # pylint:disable=E0602
    global afkb_start
    global afkb_end
    back_alive = datetime.now()
    afkb_end = back_alive.replace(microsecond=0)
    total_afkb_time = str(afkb_end - afkb_start)
    current_message = event.message.message
    if ".afkb" not in current_message and "yes" in USER_AFKB:  # pylint:disable=E0602
        shite = await borg.send_message(event.chat_id, "__My Master is Back!__\n**He is No Longer afk.**\n `Was afk for:``" + total_afkb_time + "`")
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "Set AFK mode to False"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` " + \
                "for the proper functioning of afk functionality " + \
                "ask in related group for more info.\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True
            )
        await asyncio.sleep(5)
        await shite.delete()
        USER_AFKB = {}  # pylint:disable=E0602
        afkb_time = None  # pylint:disable=E0602


@borg.on(events.NewMessage(  # pylint:disable=E0602
    incoming=True,
    func=lambda e: bool(e.mentioned or e.is_private)
))
async def on_afkb(event):
    if event.fwd_from:
        return
    global USER_AFKB  # pylint:disable=E0602
    global afkb_time  # pylint:disable=E0602
    global last_afkb_message  # pylint:disable=E0602
    global afkb_start
    global afkb_end
    back_alivee = datetime.now()
    afkb_end = back_alivee.replace(microsecond=0)
    total_afkb_time = str(afkb_end - afkb_start)
    afkb_since = "**a while ago**"
    current_message_text = event.message.message.lower()
    if "afkb" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFKB and not (await event.get_sender()).bot:  # pylint:disable=E0602
        if afkb_time:  # pylint:disable=E0602
            now = datetime.datetime.now()
            datime_since_afkb = now - afkb_time  # pylint:disable=E0602
            time = float(datime_since_afkb.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afkb_since = "**Yesterday**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afkb_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afkb_since = wday.strftime('%A')
            elif hours > 1:
                afkb_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
            elif minutes > 0:
                afkb_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
            else:
                afkb_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = f"My Master {DEFAULTUSER} Is **afk since** {total_afkb_time}" + \
            f"\n__and HE may be back soon__\n**Because my King is** {reason}" \
            if reason \
            else f"My King 👑 {DEFAULTUSER} 👑 is **afk Since** {total_afkb_time}. \nand My King has left a word for you only: \n{AFKSK}\n`.` "
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afkb_message:  # pylint:disable=E0602
            await last_afkb_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afkb_message[event.chat_id] = msg  # pylint:disable=E0602
