import requests
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN=os.getenv('TELEGRAM_TOKEN', '')
CHAT_ID=os.getenv('CHAT_ID', '')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def check_if_ok(url: str) -> tuple[str, bool]:
    response = requests.get(url)

    if response.status_code == 200:
        return url, True
    return url, False

def verify_and_send_message(urls: list[str]):
    for url in urls:
        if not check_if_ok(url):
            bot.send_message(CHAT_ID, url)

def main(func, params):
    import time

    while True:
        func(params)
        time.sleep(60)

