import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
import asyncio
import shutil

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

@command(pattern="^.autopic", outgoing=True)
async def autopic(event):
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    shutil.copy(downloaded_file_name, photo)
    while True:
        im = Image.open(photo)
        file_test = im.rotate(-5, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \n ⚡USERBOT TIMEZONE⚡ \n  Time: %H:%M:%S \n  Date: %d.%m.%y \n⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
        photo_complete = "userbot/photo_complete.png"
        shutil.copy(photo, photo_complete)
        img = Image.open(photo_complete)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((50, 250), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo_complete)
        file = await bot.upload_file(photo_complete)  # pylint:disable=E0602
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo_complete)
            await asyncio.sleep(60)
        except:
            return
