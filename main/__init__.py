#Join me at telegram @dev_gagan

from pyrogram import Client
from pyromod import listen
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("5525620445", default=None, cast=int)
API_HASH = config("de14eccfa6fa8d7c2eee9656cc2bdc69", default=None)
BOT_TOKEN = config("7762470551:AAFbtj2V7aBnhy-q3vM6qqQ9DIAdeF6mLLI", default=None)
SESSION = config("BQDttYcAv_Lgda1aJnZ1tFnfZZ8i_170e3gqpRKvpiNrl_6Cfkttt7sTS-q8v05ec4TozfyNiqEmGMPJLUxaPwhZxuvsQHHT0uYVfRhyp96JppHc33JgYozW_2SI53QVwNtX4cSssdGj1m3n3F1HjgBXTYllpd7MO2sidtTbuHPYeG_i4igg8IUyyUsAZyHWUvmApwSgAfEDW1nwJUJXZC-7-_qdgF8s58YXF2HxElCihJQF2hgCSO_sxqsVqxNq3glkNk5M3VSzB_OA0h4S6hGud52C7elLvUNVOwzvslR5aGJnHvCdVp0o-0IMYYy0KdI_rRi53bjtxvy9fnV411i1yaFTuAAAAAFJWkbdAA", default=None)
FORCESUB = config("Atul100329", default=None)
AUTH = config("5525620445", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
