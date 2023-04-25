#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 1317481
API_HASH = e5f7a25123dca9d734516cde8ae4c374
BOT_TOKEN = 6078119965:AAE7y43vsCpme4aavFZQVxGGOyI71cMEBr8
SESSION = BAAK_517ygaHkE3t5-6a8x317sQA-N8p1VqRNh94hX-qh36QInWun_OiF1BHMPROrM6yxA3zTLq-i9LlZSXxYpq7FctMykf1nF7Pr6bsOmRAzPD2kFipOpihptxuiC8HIMxyTw35kgx1laaZA_Z_yX60_dW35HZpASZMePWMp2dbZOqrSu4GWn0EobcTH0ncciSMhYr4-RnIxsl8nD7QXzGEC51YkJFZFJ9XGSycM2B6kcI2CvA2Mpm34X6nCXUG4oE9Xb83emPJL1knETGHw9TRalUSryddI6-9NQTVjhRhCkHD7fmxziToMbf3l9VdMRYpyyrsj2f55VTmLEPK1WJ3AAAAAWNHLCsA
FORCESUB = DTO_bots
AUTH = 965221088

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
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
    print(e)
    sys.exit(1)
