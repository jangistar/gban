import sys
from telethon import TelegramClient, events
from async_generator import aclosing
from telethon import *
from datetime import datetime, timedelta
import time
import logging
import random, re
import asyncio
import os
from gtts import gTTS
import time
import hastebin
import urbandict
import gsearch
import subprocess
from telethon import events, utils, TelegramClient
import requests
import sys, os, re, subprocess, time, logging, math
from datetime import datetime, timedelta
from datetime import datetime
from requests import get
import wikipedia
import inspect
import platform
import pybase64
import pyfiglet
from googletrans import Translator
from random import randint
from zalgo_text import zalgo
import sqlite3
global SPAM
SPAM=False
global ISAFK
ISAFK=False
global AFKREASON
AFKREASON="No Reason"
global USERS
USERS={}
global COUNT_MSG
global SPAM_ALLOWANCE
SPAM_ALLOWANCE=3
global MUTING_USERS
MUTING_USERS={}
COUNT_MSG=0
WIDE_MAP = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000

@borg.on(events.NewMessage(outgoing=True,pattern='.*'))
@borg.on(events.MessageEdited(outgoing=True))
async def common_outgoing_handler(e):
    find = e.text
    find = str(find[1:])
    if find=="delmsg" :
        i=1
        async for message in borg.iter_messages(e.chat_id,from_user='me'):
            if i>2:
                break
            i=i+1
            await message.delete()
    elif find == "shg":
        await e.edit("¯\_(ツ)_/¯")
    elif find == "get userbotfile":
        file=open(sys.argv[0], 'r')
        await borg.send_file(e.chat_id, sys.argv[0], reply_to=e.id, caption='`Here\'s me in a file`')
        file.close()
    elif find == "reportbug":
        await e.edit("Report bugs here: @hackedyouahain")
    elif find == "help":
        await e.edit('https://github.com/bottest123/forkborg/blob/master/README.md')
    elif find == "thanos":
        rights = ChannelBannedRights(
                             until_date=None,
                             view_messages=True,
                             send_messages=True,
                             send_media=True,
                             send_stickers=True,
                             send_gifs=True,
                             send_games=True,
                             send_inline=True,
                             embed_links=True
                             )
        if (await e.get_reply_message()).sender_id in BRAIN_CHECKER:
            await e.edit("`Ban Error! Couldn\'t ban this user`")
            return
        await e.edit("`Thanos snaps!`")
        time.sleep(5)
        await borg(EditBannedRequest(e.chat_id,(await e.get_reply_message()).sender_id,rights))
        await e.delete()
        await borg.send_file(e.chat_id,"https://media.giphy.com/media/xUOxfgwY8Tvj1DY5y0/source.gif")
    elif find == "addsudo":
        if e.sender_id==BRAIN_CHECKER[0]:
            db=sqlite3.connect("brains.check")
            cursor=db.cursor()
            id=(await e.get_reply_message()).sender_id
            cursor.execute('''INSERT INTO BRAIN1 VALUES(?)''',(id,))
            db.commit()
            await e.edit("```Added to Sudo Successfully```")
            db.close()
    elif find == "spider":
        rights = ChannelBannedRights(
                             until_date=None,
                             view_messages=None,
                             send_messages=True,
                             send_media=True,
                             send_stickers=True,
                             send_gifs=True,
                             send_games=True,
                             send_inline=True,
                             embed_links=True
                             )
        if (await e.get_reply_message()).sender_id in BRAIN_CHECKER:
            await e.edit("`Mute Error! Couldn\'t mute this user`")
            return
        await e.edit("`Spiderman nabs him!`")
        time.sleep(5)
        await borg(EditBannedRequest(e.chat_id,(await e.get_reply_message()).sender_id,rights))
        await e.delete()
        await borg.send_file(e.chat_id,"https://image.ibb.co/mNtVa9/ezgif_2_49b4f89285.gif")
    elif find == "wizard":
        rights = ChannelAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        invite_link=True,
        )
        await e.edit("`Wizard waves his wand!`")
        time.sleep(3)
        await borg(EditAdminRequest(e.chat_id,(await e.get_reply_message()).sender_id,rights))
        await e.edit("A perfect magic has happened!")
    elif find == "asmoff":
        global SPAM
        SPAM=False
        await e.edit("Spam Tracking turned off!")
    elif find == "rmfilters":
        await e.edit("```Will be kicking away all Marie filters.```")
        time.sleep(3)
        r = await e.get_reply_message()
        filters = r.text.split('-')[1:]
        for filter in filters:
            await e.reply('/stop %s' % (filter.strip()))
            await asyncio.sleep(0.3)
        await e.respond("```Successfully cleaned Marie filters yaay!```\n Gimme cookies @baalajimaestro")
    elif find == "rmnotes":
        await e.edit("```Will be kicking away all Marie filters.```")
        time.sleep(3)
        r = await e.get_reply_message()
        filters = r.text.split('-')[1:]
        for filter in filters:
            await e.reply('/clear %s' % (filter.strip()))
            await asyncio.sleep(0.3)
        await e.respond("```Successfully cleaned Marie notes yaay!```\n Gimme cookies @baalajimaestro")
    elif find=="rekt":
        await e.edit("Get Rekt man! ( ͡° ͜ʖ ͡°)")
    elif find=="speed":
            l=await e.reply('`Running speed test . . .`')
            k=subprocess.run(['speedtest-cli'], stdout=subprocess.PIPE)
            await l.edit('`' + k.stdout.decode()[:-1] + '`')
            await e.delete()
    elif find == "alive":
        await e.edit("`Master! I am alive😁`")
    elif find=="notafk":
        global ISAFK
        global COUNT_MSG
        global USERS
        global AFKREASON
        ISAFK=False
        await e.edit("I have returned from AFK mode.")
        await e.respond("`You had recieved "+str(COUNT_MSG)+" messages while you were away. Check log for more details. This auto-generated message shall be self destructed in 2 seconds.`")
        time.sleep(2)
        i=1
        async for message in borg.iter_messages(e.chat_id,from_user='me'):
            if i>1:
                break
            i=i+1
            await message.delete()
        await borg.send_message(-1001200493978,"You had recieved "+str(COUNT_MSG)+" messages from "+str(len(USERS))+" chats while you were away")
        for i in USERS:
            await borg.send_message(-1001200493978,str(i)+" sent you "+"`"+str(USERS[i])+" messages`")
        COUNT_MSG=0
        USERS={}
        AFKREASON="No reason"
    elif find=="runs":
        reactor=['Runs to Modi for Help','Runs to Donald Trumpet for help','Runs to Kaala','Runs to Thanos','Runs far, far away from earth','Running faster than usian bolt coz I\'mma Bot','Runs to Marie']
        index=randint(0,len(reactor)-1)
        reply_text=reactor[index]
        await e.edit(reply_text)
        await borg.send_message(-1001200493978,"You ran away from a cancerous chat")
    elif find=="react":
        reactor=['ʘ‿ʘ','ヾ(-_- )ゞ','(っ˘ڡ˘ς)','(´ж｀ς)','( ಠ ʖ̯ ಠ)','(° ͜ʖ͡°)╭∩╮','(ᵟຶ︵ ᵟຶ)','(งツ)ว','ʚ(•｀','(っ▀¯▀)つ','(◠﹏◠)','( ͡ಠ ʖ̯ ͡ಠ)','( ఠ ͟ʖ ఠ)','(∩｀-´)⊃━☆ﾟ.*･｡ﾟ','(⊃｡•́‿•̀｡)⊃','(._.)','{•̃_•̃}','(ᵔᴥᵔ)','♨_♨','⥀.⥀','ح˚௰˚づ ','(҂◡_◡)','ƪ(ړײ)‎ƪ​​','(っ•́｡•́)♪♬','◖ᵔᴥᵔ◗ ♪ ♫ ','(☞ﾟヮﾟ)☞','[¬º-°]¬','(Ծ‸ Ծ)','(•̀ᴗ•́)و ̑̑','ヾ(´〇`)ﾉ♪♪♪','(ง\'̀-\'́)ง','ლ(•́•́ლ)','ʕ •́؈•̀ ₎','♪♪ ヽ(ˇ∀ˇ )ゞ','щ（ﾟДﾟщ）','( ˇ෴ˇ )','눈_눈','(๑•́ ₃ •̀๑) ','( ˘ ³˘)♥ ','ԅ(≖‿≖ԅ)','♥‿♥','◔_◔','⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾','乁( ◔ ౪◔)「      ┑(￣Д ￣)┍','( ఠൠఠ )ﾉ','٩(๏_๏)۶','┌(ㆆ㉨ㆆ)ʃ','ఠ_ఠ','(づ｡◕‿‿◕｡)づ','(ノಠ ∩ಠ)ノ彡( \\o°o)\\','“ヽ(´▽｀)ノ”','༼ ༎ຶ ෴ ༎ຶ༽','｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡','(づ￣ ³￣)づ','(⊙.☉)7','ᕕ( ᐛ )ᕗ','t(-_-t)','(ಥ⌣ಥ)','ヽ༼ ಠ益ಠ ༽ﾉ','༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽','ミ●﹏☉ミ','(⊙_◎)','¿ⓧ_ⓧﮌ','ಠ_ಠ','(´･_･`)','ᕦ(ò_óˇ)ᕤ','⊙﹏⊙','(╯°□°）╯︵ ┻━┻','¯\_(⊙︿⊙)_/¯','٩◔̯◔۶','°‿‿°','ᕙ(⇀‸↼‶)ᕗ','⊂(◉‿◉)つ','V•ᴥ•V','q(❂‿❂)p','ಥ_ಥ','ฅ^•ﻌ•^ฅ','ಥ﹏ಥ','（ ^_^）o自自o（^_^ ）','ಠ‿ಠ','ヽ(´▽`)/','ᵒᴥᵒ#','( ͡° ͜ʖ ͡°)','┬─┬﻿ ノ( ゜-゜ノ)','ヽ(´ー｀)ノ','☜(⌒▽⌒)☞','ε=ε=ε=┌(;*´Д`)ﾉ','(╬ ಠ益ಠ)','┬─┬⃰͡ (ᵔᵕᵔ͜ )','┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻','¯\_(ツ)_/¯','ʕᵔᴥᵔʔ','(`･ω･´)','ʕ•ᴥ•ʔ','ლ(｀ー´ლ)','ʕʘ̅͜ʘ̅ʔ','（　ﾟДﾟ）','¯\(°_o)/¯','(｡◕‿◕｡)']
        index=randint(0,len(reactor))
        reply_text=reactor[index]
        await e.edit(reply_text)
    elif find == "fastpurge":
        chat = await e.get_input_chat()
        msgs = []
        count =0
        async with aclosing(borg.iter_messages(chat, min_id=e.reply_to_msg_id)) as h:
         async for m in h:
             msgs.append(m)
             count=count+1
             if len(msgs) == 100:
                 await borg.delete_messages(chat, msgs)
                 msgs = []
        if msgs:
         await borg.delete_messages(chat, msgs)
        await borg.send_message(e.chat_id,"`Fast Purge Complete!\n`Purged "+str(count)+" messages. **This auto-generated message shall be self destructed in 2 seconds.**")
        await borg.send_message(-1001200493978,"Purge of "+str(count)+" messages done successfully.")
        time.sleep(2)
        i=1
        async for message in borg.iter_messages(e.chat_id,from_user='me'):
             if i>1:
                 break
             i=i+1
             await message.delete()
    elif find == "restart":
        await e.edit("`Thank You master! I am taking a break!`")
        os.execl(sys.executable, sys.executable, *sys.argv)
        
@borg.on(events.NewMessage(pattern='.cp'))
@borg.on(events.MessageEdited(pattern='.cp'))
async def copypasta(e):
    textx=await e.get_reply_message()
    if textx:
         message = textx
         message = str(message.message)
    else:
        message = e.text
        message = str(message[3:])
    emojis = ["馃槀", "馃槀", "馃憣", "鉁�", "馃挒", "馃憤", "馃憣", "馃挴", "馃幎", "馃憖", "馃槀", "馃憮", "馃憦", "馃憪", "馃崟", "馃挜", "馃嵈", "馃挦", "馃挦", "馃崙", "馃崋", "馃槱", "馃槒", "馃憠馃憣", "馃憖", "馃憛", "馃槱", "馃毎"]
    reply_text = random.choice(emojis)
    b_char = random.choice(message).lower() # choose a random character in the message to be substituted with 馃叡锔�
    for c in message:
        if c == " ":
            reply_text += random.choice(emojis)
        elif c in emojis:
            reply_text += c
            reply_text += random.choice(emojis)
        elif c.lower() == b_char:
            reply_text += "馃叡锔�"
        else:
            if bool(random.getrandbits(1)):
                reply_text += c.upper()
            else:
                reply_text += c.lower()
    reply_text += random.choice(emojis)
    await e.edit(reply_text)
        
@borg.on(events.NewMessage(outgoing=True,pattern='.hash (.*)'))
@borg.on(events.MessageEdited(outgoing=True,pattern='.hash (.*)'))
async def hash(e):
	hashtxt_ = e.pattern_match.group(1)
	hashtxt=open('hashdis.txt','w+')
	hashtxt.write(hashtxt_)
	hashtxt.close()
	md5=subprocess.run(['md5sum', 'hashdis.txt'], stdout=subprocess.PIPE)
	md5=md5.stdout.decode()
	sha1=subprocess.run(['sha1sum', 'hashdis.txt'], stdout=subprocess.PIPE)
	sha1=sha1.stdout.decode()
	sha256=subprocess.run(['sha256sum', 'hashdis.txt'], stdout=subprocess.PIPE)
	sha256=sha256.stdout.decode()
	sha512=subprocess.run(['sha512sum', 'hashdis.txt'], stdout=subprocess.PIPE)
	subprocess.run(['rm', 'hashdis.txt'], stdout=subprocess.PIPE)
	sha512=sha512.stdout.decode()
	ans='Text: `' + hashtxt_ + '`\nMD5: `' + md5 + '`SHA1: `' + sha1 + '`SHA256: `' + sha256 + '`SHA512: `' + sha512[:-1] + '`'
	if len(ans) > 4096:
		f=open('hashes.txt', 'w+')
		f.write(ans)
		f.close()
		await borg.send_file(e.chat_id, 'hashes.txt', reply_to=e.id, caption="`It's too big, in a text file and hastebin instead. `" + hastebin.post(ans[1:-1]))
		subprocess.run(['rm', 'hashes.txt'], stdout=subprocess.PIPE)
	else:
		await e.reply(ans)
		
@borg.on(events.NewMessage(outgoing=True,pattern='.base64 (en|de) (.*)'))
@borg.on(events.MessageEdited(outgoing=True,pattern='.base64 (en|de) (.*)'))
async def endecrypt(e):
	if e.pattern_match.group(1) == 'en':
		lething=str(pybase64.b64encode(bytes(e.pattern_match.group(2), 'utf-8')))[2:]
		await e.reply('Encoded: `' + lething[:-1] + '`')
	else:
		lething=str(pybase64.b64decode(bytes(e.pattern_match.group(2), 'utf-8'), validate=True))[2:]
		await e.reply('Decoded: `' + lething[:-1] + '`')
@borg.on(events.NewMessage(outgoing=True, pattern='.random'))
@borg.on(events.MessageEdited(outgoing=True, pattern='.random'))
async def randomise(e):
    r=(e.text).split()
    index=randint(1,len(r)-1)
    await e.edit("**Query: **\n`"+e.text+'`\n**Output: **\n`'+r[index]+'`')
@borg.on(events.NewMessage(outgoing=True, pattern='.log'))
@borg.on(events.MessageEdited(outgoing=True, pattern='.log'))
async def log(e):
    textx=await e.get_reply_message()
    if textx:
         message = textx
         message = str(message.message)
    else:
        message = e.text
        message = str(message[4:])
    await borg.send_message(-1001200493978,message)
    await e.edit("`Logged Successfully`")
    
@borg.on(events.NewMessage(incoming=True,pattern='.killme'))
async def killmelol(e):
    name = await borg.get_entity(e.from_id)
    name0 = str(name.first_name)
    await e.reply('**K I L L  **[' + name0 + '](tg://user?id=' + str(e.from_id) + ')**\n\nP L E A S E\n\nE N D  T H E I R  S U F F E R I N G**')

@borg.on(events.NewMessage(outgoing=True, pattern='.vapor'))
@borg.on(events.MessageEdited(outgoing=True, pattern='.vapor'))
async def vapor(e):
    textx=await e.get_reply_message()
    message = e.text
    if textx:
         message = textx
         message = str(message.message)
    else:
        message = str(message[7:])
    if message:
        data = message
    else:
        data = ''
    reply_text = str(data).translate(WIDE_MAP)
    await e.edit(reply_text)
    
@borg.on(events.NewMessage(outgoing=True, pattern=':/'))
@borg.on(events.MessageEdited(outgoing=True, pattern=':/'))
async def kek(e):
    uio=['/','\\']
    for i in range (1,15):
        time.sleep(0.3)
        await e.edit(':'+uio[i%2])
@borg.on(events.NewMessage(outgoing=True, pattern='-_-'))
@borg.on(events.MessageEdited(outgoing=True, pattern='-_-'))
async def lol(e):
    await e.delete()
    t = '-_-'
    r = await e.reply(t)
    for j in range(10):
        t = t[:-1] + '_-'
        await r.edit(t)
        
@borg.on(events.NewMessage(outgoing=True, pattern='.term'))
@borg.on(events.MessageEdited(outgoing=True, pattern='.term'))
async def terminal_runner(e):
    message=e.text
    command = str(message)
    list_x=command.split(' ')
    result=subprocess.run(list_x[1:], stdout=subprocess.PIPE)
    result=str(result.stdout.decode())
    await e.edit("**Query: **\n`"+str(command[6:])+'`\n**Output: **\n`'+result+'`')

@borg.on(events.NewMessage(outgoing=True, pattern='.spam'))
@borg.on(events.MessageEdited(outgoing=True, pattern='.spam'))
async def spammer(e):
    message= e.text
    counter=int(message[6:8])
    spam_message=str(e.text[8:])
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    await e.delete()


@borg.on(events.NewMessage(pattern=r'.google (.*)'))
@borg.on(events.MessageEdited(pattern=r'.google (.*)'))
async def gsearch(e):
        match = e.pattern_match.group(1)
        result_=subprocess.run(['gsearch', match], stdout=subprocess.PIPE)
        result=str(result_.stdout.decode())
        await borg.send_message(await borg.get_input_entity(e.chat_id), message='**Search Query:**\n`' + match + '`\n\n**Result:**\n' + result, reply_to=e.id, link_preview=False)


@borg.on(events.NewMessage(outgoing=True, pattern='.loltts'))
@borg.on(events.MessageEdited(outgoing=True, pattern='.loltts'))
async def meme_tts(e):
    textx=await e.get_reply_message()
    replye = e.text
    if textx:
         replye = await e.get_reply_message()
         replye = str(replye.message)
    else:
        replye = str(replye[8:])
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    tts = gTTS(replye, "ja")
    tts.save("k.mp3")
    with open("k.mp3", "rb") as f:
        linelist = list(f)
        linecount = len(linelist)
    if linecount == 1:                          #tts on personal chats is broken
        tts = gTTS(replyes,"ja")
        tts.save("k.mp3")
    with open("k.mp3", "r") as speech:
        await borg.send_file(e.chat_id, 'k.mp3', voice_note=True)
        os.remove("k.mp3")
        await e.delete()
if len(sys.argv) < 2:
    borg.run_until_disconnected()
   
    
