import requests
import asyncio
import json
from telegram import Bot, InputFile
from info import tg_token, tg_chat_id, url_api
from parsing import start_parsing

# Налаштування Telegram
TELEGRAM_BOT_TOKEN = tg_token
TELEGRAM_CHAT_ID = tg_chat_id

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# URL API для моніторингу
API_URL = url_api
CHECK_INTERVAL = 60  # Інтервал перевірки в секундах

# Файл для зберігання попереднього стану даних
STATE_FILE = 'previous_data.json'
DATABASE_FILE = 'database.json'  # Файл, який буде надіслано


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Помилка запиту до {url}: {e}")
        return None


def load_previous_data():
    try:
        with open(STATE_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def save_current_data(data):
    with open(STATE_FILE, 'w') as file:
        json.dump(data, file)


async def send_telegram_message(chat_id, message, document_path=None):
    try:
        if document_path:
            with open(document_path, 'rb') as doc:
                await bot.send_document(chat_id=chat_id, document=InputFile(doc), caption=message)
        else:
            await bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Помилка відправки повідомлення в Telegram: {e}")


async def monitor_api():
    while True:
        current_data = fetch_data(API_URL)
        previous_data = load_previous_data()

        if current_data:
            # Перевіряємо, чи є зміни
            if previous_data and previous_data['data']['modified_on'] != current_data['data']['modified_on']:
                message = (
                    f"Дата зміни: {current_data['data']['modified_on']}"
                )
                start_parsing()
                print("Знайдено зміни на сайті!")
                await send_telegram_message(TELEGRAM_CHAT_ID, message, DATABASE_FILE)
            else:
                print("Змін не знайдено")

            # Оновлюємо попередні дані
            save_current_data(current_data)
        else:
            print("Не вдалося отримати дані з API")

        # Затримка між перевірками
        await asyncio.sleep(CHECK_INTERVAL)

# Запуск моніторингу
asyncio.run(monitor_api())
