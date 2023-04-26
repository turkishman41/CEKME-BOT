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
API_HASH = "e5f7a25123dca9d734516cde8ae4c374"
BOT_TOKEN = "5947534274:AAEmY-91HrtD2sYSiinRIyB6rY1BxOU5bXk"
SESSION = "BAADr_ipQPv4DDxNKzZoXYGTH9ooG71ILy03fQnPV9D1XZmxjTgxrwy3er_BObfxJpSSV6eAm-iXjt2797WE89DeDCrpPdogWAkeycmm6I2qQf35T-K7V_2p_rjEv3yqR_emP9HzKgSxbkUoi7ViwEp-dUHIYLJDDuHCuO864vnJK6UOilsVYqFE_g0H1XrXMYLO9Ov1ufiQV8eJxEmCdmn5oL-XMh2wAbVlcBnWvOdS5MGNa4xggAAL4e0aGweDU-DIZdFy-uVP5eqN6ywFl7v7EHXL0j4ebVjeHaUprA2zz0HlRULKVmqUfLBJj8sAz582q-GoE3m-LAyG69SLQ2CKAAAAAV2IWkgA"
FORCESUB = "DTO_Bots"
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
