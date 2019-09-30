"""

Let me Google / YouTube that for you! 

Syntax:

 .ggl <search query>

 .ytb <search query>

By @Deonnn 



"""







from telethon import events



import os



import requests



import json



from uniborg.util import admin_cmd











@borg.on(admin_cmd(pattern="ggl (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=http://google.com/search?q={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **Google** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")





@borg.on(admin_cmd(pattern="ytb (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.youtube.com/results?search_query={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Let me **YouTube** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Something went wrong. Please try again later.")
