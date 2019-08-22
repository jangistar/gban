"""
A Torrent Client Plugin Based On Aria2 for Userbot

cmds: Magnet link : .mag magnetLink
      Torrent file from local: .tor file_path
      Show Downloads: .show
      Remove All Downloads: .remtor
      Resume All Downloads: .resumetor
      Pause All Downloads:  .pausetor

By:- @Zero_cool7870

Credits: https://github.com/jaskaranSM/UniBorg/blob/b42cd70144143ce079e5fb3aed49c9aa1412481b/stdplugins/aria.py
"""

import aria2p
from telethon import events
import asyncio
import io
import os
from uniborg.util import admin_cmd

ARIA_2_PORT = 6800
cmd = f"aria2c --enable-rpc --rpc-listen-all=false --rpc-listen-port {ARIA_2_PORT}  --max-connection-per-server=10 --rpc-max-request-size=1024M --seed-time=0.01 --min-split-size=10M --follow-torrent=mem --split=10 --daemon=true"

aria2_is_running = os.system(cmd)

aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        port=ARIA_2_PORT,
        secret=""
    )
)


@borg.on(events.NewMessage(pattern=r"\.mag", outgoing=True))
async def magnet_download(event):
	if event.fwd_from:
		return   
	var = event.text
	var = var[8:]
	
	magnet_uri = var
	magnet_uri = magnet_uri.replace("`","")
	print(magnet_uri)

	#Add Magnet URI Into Queue
	try:
		download = aria2.add_magnet(magnet_uri)
		gid = download.gid
		complete = None
		while complete != True:
			file = aria2.get_download(gid)
			complete = file.is_complete
			try:
				if not file.error_message:
					msg = "Downloading Metadata: `"+str(file.name) +"`\nSpeed: "+ str(file.download_speed_string())+"\nProgress: "+str(file.progress_string())+"\nTotal Size: "+str(file.total_length_string())+"\nStatus: "+str(file.status)+"\nETA:  "+str(file.eta_string())+"\n\n"
					await event.edit(msg)
					await asyncio.sleep(10)
				else:
					msg = file.error_message
					await event.edit("`"+msg+"`")
					return 	
			except Exception as e:
				#print(str(e))
				pass
		await asyncio.sleep(3)
		new_gid = await check_metadata(gid)
		complete = None
		while complete != True:
			file = aria2.get_download(new_gid[0])
			complete = file.is_complete
			try:
				if not file.error_message:
					msg = "Downloading File: `"+str(file.name) +"`\nSpeed: "+ str(file.download_speed_string())+"\nProgress: "+str(file.progress_string())+"\nTotal Size: "+str(file.total_length_string())+"\nStatus: "+str(file.status)+"\nETA:  "+str(file.eta_string())+"\n\n"
					await event.edit(msg)
					await asyncio.sleep(15)
				else:
					msg = file.error_message
					await event.edit("`"+msg+"`")
					return 	
			except Exception as e:
				#print(str(e))
				pass

	except Exception as e:
		if "EditMessageRequest" in str(e):
			pass
		elif " not found" in str(e):
			await event.edit("Download Cancelled:\n`"+file.name+"`")
			return
		else:	
			print(str(e))
			await event.edit("Error:\n`"+str(e)+"`")	
			return
	await event.edit("File Downloaded Successfully:\n`"+file.name+"`")
	
async def check_metadata(gid):
	file = aria2.get_download(gid)
	new_gid = file.followed_by_ids
	print("Changing GID "+gid+" to "+new_gid[0])
	return new_gid	

@borg.on(events.NewMessage(pattern=r"\.tor", outgoing=True))
async def torrent_download(event):
	if event.fwd_from:
		return

	var = event.text[5:]
	
	torrent_file_path = var	
	torrent_file_path = torrent_file_path.replace("`","")
	print(torrent_file_path)

	#Add Torrent Into Queue
	try:
		download = aria2.add_torrent(torrent_file_path, uris=None, options=None, position=None)
	except:
		await event.edit("`Torrent File Not Found...`")
		return

	gid = download.gid
	complete = None
	while complete != True:
		try:
			file = aria2.get_download(gid)
			complete = file.is_complete
			if not file.error_message:
				msg = "Downloading File: `"+str(file.name) +"`\nSpeed: "+ str(file.download_speed_string())+"\nProgress: "+str(file.progress_string())+"\nTotal Size: "+str(file.total_length_string())+"\nStatus: "+str(file.status)+"\nETA:  "+str(file.eta_string())+"\n\n"
				await event.edit(msg)
				await asyncio.sleep(15)
			else:
					msg = file.error_message
					await event.edit("`"+msg+"`")
					return	
		except Exception as e:
			if "EditMessageRequest" in str(e):
				pass
			elif "not found" in str(e):
				await event.edit("Download Cancelled:\n`"+file.name+"`")
				print("Download Aborted: "+gid)
				return	
			else:	
				print(str(e))
				await event.edit("Error:\n`"+str(e)+"`")	
				return	

	await event.edit("File Downloaded Successfully:\n`"+download.name+"`")

@borg.on(events.NewMessage(pattern=r"\.get", outgoing=True))
async def magnet_download(event):
	if event.fwd_from:
		return
	var = event.text[5:]
	print(var)	
	uris = [var]

	#Add URL Into Queue 
	try:	
		download = aria2.add_uris(uris, options=None, position=None)
	except Exception as e:
		await event.edit("`Error:\n`"+str(e))
		return

	gid = download.gid
	complete = None
	while complete != True:
		file = aria2.get_download(gid)
		complete = file.is_complete
		try:
			msg = "⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\n\n\n`ℛAVANA Telegram Downloader`\n\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛⬛️⬛️⬛️⬛️⬛️\n\n\nDownloading File: "+str(file.name) +"\n\nSpeed: "+ str(file.download_speed_string())+"\n\n"+"Progress: "+str(file.progress_string())+"\n\nStatus: "+str(file.status)+"\n\nETA:  "+str(file.eta_string())+"\n\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛⬛️⬛️⬛️\n"	
			await event.edit(msg)
			await asyncio.sleep(10)
		except Exception as e:
			#print(str(e))
			pass	
			
	await event.edit("🔔File Downloaded Successfully:\n\n`"+file.name+"`")

@borg.on(admin_cmd("remtor"))
async def remove_all(event):
    if event.fwd_from:
        return
    removed = aria2.remove_all()
    if removed == False:  # If API returns False Try to Remove Through System Call.
        os.system("aria2p remove-all")
    await event.edit("`Removed All Downloads.`")


@borg.on(admin_cmd("pausetor"))
async def pause_all(event):
    if event.fwd_from:
        return
    # Pause ALL Currently Running Downloads.
    paused = aria2.pause_all(force=True)
    await event.edit("Output: " + str(paused))


@borg.on(admin_cmd("resumetor"))
async def resume_all(event):
    if event.fwd_from:
        return
    resumed = aria2.resume_all()
    await event.edit("Output: " + str(resumed))


@borg.on(admin_cmd("show"))
async def show_all(event):
    if event.fwd_from:
        return
    # Show All Downloads
    downloads = aria2.get_downloads()
    msg = ""
    for download in downloads:
        msg = msg + "File: " + str(download.name) + "\nSpeed: " + str(download.download_speed_string()) + "\n" + \
            "Progress: " + str(download.progress_string()) + \
            "\nETA:  " + str(download.eta_string()) + "\n\n"
    if len(msg) <= Config.MAX_MESSAGE_SIZE_LIMIT:
        await event.edit("`Current Downloads: `\n" + msg)
    else:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = "ariastatus.txt"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="`Output is huge. Sending as a file...`"
            )
            await event.delete()
