# This Source Code Form is subject to the terms of the Mozilla Public

# License, v. 2.0. If a copy of the MPL was not distributed with this

# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from .uniborg import *



import os



from sys import version_info

from logging import basicConfig, getLogger, INFO, DEBUG

from distutils.util import strtobool as sb



from dotenv import load_dotenv

from requests import get

from telethon import TelegramClient

from telethon.sessions import StringSession

from pymongo import MongoClient

import redis







# Logger setup:

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))





if CONSOLE_LOGGER_VERBOSE:

    basicConfig(

        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",

        level=DEBUG,

    )

else:

    basicConfig(

        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",

        level=INFO

    )

LOGS = getLogger(__name__)



if version_info[0] < 3 or version_info[1] < 6:

    LOGS.error(

        "You MUST have a python version of at least 3.6."

        " Multiple features depend on this. Bot quitting."

    )

    quit(1)



LOGGER_GROUP = "-264527165"



LOGGER = sb(os.environ.get(

    "LOGGER", "False"

))



CONSOLE_LOGGER_VERBOSE = sb(

    os.environ.get("CONSOLE_LOGGER_VERBOSE", "False")

    )



bot = TelegramClient("uniborg", API_ID, API_HASH)





# Init Mongo

MONGODB  = os.environ.get("MONGODB", None)



MONGO = MongoClient('mongo', 27017).bot







# Init Redis

REDIS_HOST = os.environ.get("REDIS_HOST", None)

REDIS_PORT = os.environ.get("REDIS_PORT", None)

REDIS_PW = os.environ.get("REDIS_PW", None)



REDIS = redis.StrictRedis(host= 'redis', port= 6379, decode_responses=True)



#Mad Variables(Putting For Fun)



HELPER = {}
