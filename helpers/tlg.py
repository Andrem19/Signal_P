import os
from decouple import config
from telegram import Bot
import shared_variables as sv
import managers_func as mf
import time
from threading import Lock
old_timestamp = 0

async def send_inform_message(message, image_path: str, send_pic: bool):
    try:
        api_token = config("SIGNAL_BOT")
        chat_id = config("CHAT_ID")
        
        bot = Bot(token=api_token)

        response = None
        if send_pic:
            with open(image_path, 'rb') as photo:
                response = await bot.send_photo(chat_id=chat_id, photo=photo, caption=message)
        else:
            response = await bot.send_message(chat_id=chat_id, text=message)

        if response:
            print("Inform message sent successfully!")
        else:
            print("Failed to send inform message.")
    except Exception as e:
        print("An error occurred:", str(e))

