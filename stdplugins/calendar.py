"""Malayalam Calendar plugin for @UniBorg
SYNTAX: .calendar DD-MM-YYYY"""
from telethon import events
import asyncio
from datetime import datetime
import requests
import json
from uniborg.util import admin_cmd


@borg.on(admin_cmd("calendar (.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split("-")
    if len(input_sgra) == 3:
        dd = input_sgra[0]
        mm = input_sgra[1]
        yyyy = input_sgra[2]
        url = "https://vedicrishi-horoscope-matching-v1.p.rapidapi.com/basic_panchang/"

payload = "{  \"day\": \"25\",  \"month\": \"12\",  \"year\": \"1988\",  \"hour\":\"10\",  \"min\":\"20\",  \"lat\": \"25.123\",  \"lon\": \"82.34\",  \"tzone\": \"5.5\"}"
headers = {
    'x-rapidapi-host': "vedicrishi-horoscope-matching-v1.p.rapidapi.com",
    'x-rapidapi-key': "ff1dd53d6cmsh64a023e59884445p12403cjsn4c7c40092564",
    'content-type': "application/json",
    'accept': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
