import os

from time import sleep

from uniborg import HELPER, REDIS

from telethon import events

from selenium import webdriver

from urllib.parse import quote_plus

from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options

from uniborg.util import admin_cmd



# ===== Rescue Force ======

if REDIS.get('carbon'):

      pass

else:

      REDIS.set('carbon', 'auto')



@borg.on(admin_cmd("^.setlang"))

async def setlang(prog):

    if not prog.text[0].isalpha() and prog.text[0] not in ("/", "#", "@", "!"):

        LANG = prog.text.split()[1]

        REDIS.set('carbon', LANG)

        await prog.edit(f"language set to {LANG}")



@borg.on(admin_cmd("^.carbon"))

async def carbon_api(e):

 if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

   """ A Wrapper for carbon.now.sh """

   await e.edit("Processing...")

   CARBON = 'https://carbon.now.sh/?l={lang}&code={code}'

   LANG = REDIS.get('carbon')

   textx = await e.get_reply_message()

   pcode = e.text

   if pcode[8:]:

         pcode = str(pcode[8:])

   elif textx:

         pcode = str(textx.message) # Importing message to module

   code = quote_plus(pcode) # Converting to urlencoded 

   url = CARBON.format(code=code, lang=LANG)

   chrome_options = Options()

   chrome_options.add_argument("--headless")

   chrome_options.add_argument("--window-size=1920x1080")

   chrome_options.add_argument("--disable-dev-shm-usage")

   chrome_options.add_argument("--no-sandbox")

   chrome_options.add_argument('--disable-gpu')

   prefs = {'download.default_directory' : '/'}

   chrome_options.add_experimental_option('prefs', prefs)

   await e.edit("Processing 30%")



   driver = webdriver.Chrome(options=chrome_options)

   driver.get(url)

   download_path = '/home/'

   driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}

   command_result = driver.execute("send_command", params)



   driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()

   sleep(3)  # this might take a bit.

   await e.edit("Processing 50%")

   driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()

   sleep(3) #Waiting for downloading

   

   await e.edit("Processing 90%")

   file = '/home/carbon.png'

   await e.edit("Done!!")

   await event.send_file(

         e.chat_id,

         file,

        reply_to=e.message.reply_to_msg_id,

           )

 

   os.remove('/home/carbon.png')

   # Removing carbon.png after uploading

   await e.delete() # Deleting msg 



HELPER.update({

      "carbon":".carbon <text> \n Beautify your code"

})

HELPER.update({

    'setlang':".setlang <Lang> \ \nUsage: It will set language for you carbon module "

})
