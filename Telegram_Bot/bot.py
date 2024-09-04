import requests
import asyncio
import json
from telegram import Bot
from tg_token import token

# Налаштування Telegram
TELEGRAM_BOT_TOKEN = token
TELEGRAM_CHAT_ID = '355542941'

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# URL API для моніторингу
API_URL = 'https://www.soe.com.ua/includes/vidklyuchennya_srv_CURL.php?cmd=get_user_disconnections_image_api&cherga=1'
CHECK_INTERVAL = 60  # Інтервал перевірки в секундах

# Файл для зберігання попереднього стану даних
STATE_FILE = 'previous_data.json'


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


async def send_telegram_message(chat_id, message):
    try:
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
                    f"Дата модифікації: {current_data['data']['modified_on']}"
                )
                print("Знайдено зміни на сайті!")
                await send_telegram_message(TELEGRAM_CHAT_ID, message)
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
