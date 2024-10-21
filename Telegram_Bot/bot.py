import requests
import asyncio
import json
import warnings
from urllib3.exceptions import InsecureRequestWarning
from telegram import Bot, InputFile
from info import tg_token, tg_chat_id, tg_chat_id_2, url_api
from parsing_today import start_parsing_today
from parsing_tomorrow import start_parsing_tomorrow
from datetime import datetime

# Налаштування Telegram
TELEGRAM_BOT_TOKEN = tg_token

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# URL API для моніторингу
API_URL = url_api
CHECK_INTERVAL = 60  # Інтервал перевірки в секундах

# Файл для зберігання попереднього стану даних
STATE_FILE = 'previous_data.json'
DATABASE_FILE = 'database.json'  # Файл, який буде надіслано


async def fetch_data(url):
    current_time = datetime.now().time()
    start_time = "01:30"
    end_time = "02:30"
    time_start = datetime.strptime(start_time, '%H:%M').time()
    time_end = datetime.strptime(end_time, '%H:%M').time()
    if time_start <= current_time <= time_end:
        print('Планове відключення')
    else:
        try:
            warnings.simplefilter('ignore', InsecureRequestWarning)
            response = requests.get(url, verify=False)  # або із SSL-перевіркою
            if response.status_code == 200:
                response.raise_for_status()
                return response.json()
        except requests.RequestException as e:
            print(f"Помилка запиту до сайту.")
            message = (
                f"Помилка запиту до сайту."
            )
            await send_telegram_message(tg_chat_id, message)
            await send_telegram_message(tg_chat_id_2, message)
            raise asyncio.CancelledError  # Зупиняємо виконання


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
        try:
            current_data = await fetch_data(API_URL)
            previous_data = load_previous_data()

            if current_data:
                # Перевіряємо, чи є зміни
                try:
                    if current_data and current_data['data']['modified_on'] == previous_data['data']['dict_tom']['modified_on']:
                        print('Новий день')
                except:
                    if current_data['data']['modified_on'] == '':
                        print('Без оновлень')
                    if previous_data and previous_data['data']['modified_on'] != current_data['data']['modified_on']:
                        message = (
                            f"Дата зміни на сьогодні: {
                                current_data['data']['modified_on']}"
                        )
                        start_parsing_today()
                        print("Знайдено зміни на сьогодні!")
                        await send_telegram_message(tg_chat_id, message, DATABASE_FILE)
                        await send_telegram_message(tg_chat_id_2, message, DATABASE_FILE)

                    try:
                        if current_data and current_data['data']['modified_on'] == previous_data['data']['modified_on']:
                            print('Нова інформація дорівнює старій')
                    except:
                        if current_data['data']['modified_on'] != '':
                            message = (
                                f"Дата зміни на сьогодні: {
                                    current_data['data']['modified_on']}"
                            )
                            start_parsing_today()
                            print("Знайдено зміни на сьогодні!")
                            await send_telegram_message(tg_chat_id, message, DATABASE_FILE)
                            await send_telegram_message(tg_chat_id_2, message, DATABASE_FILE)

                # Оновлюємо попередні дані
                save_current_data(current_data)
            else:
                message = (
                    "Не вдалося отримати дані з API"
                )
                print("Не вдалося отримати дані з API")
                await send_telegram_message(tg_chat_id, message, DATABASE_FILE)
                await send_telegram_message(tg_chat_id_2, message, DATABASE_FILE)

            # Затримка між перевірками
            try:
                if current_data:
                    # Перевіряємо, чи є зміни на завтра
                    if previous_data and previous_data['data']['dict_tom']['modified_on'] != current_data['data']['dict_tom']['modified_on']:
                        message = (
                            f"Дата зміни на завтра: {
                                current_data['data']['dict_tom']['modified_on']}"
                        )
                        start_parsing_tomorrow()
                        print("Знайдено зміни на завтра!")
                        await send_telegram_message(tg_chat_id, message, DATABASE_FILE)
                        await send_telegram_message(tg_chat_id_2, message, DATABASE_FILE)
                    else:
                        print("Змін на завтра не знайдено")

                    # Оновлюємо попередні дані
                    save_current_data(current_data)
                else:
                    message = (
                        "Не вдалося отримати дані з API"
                    )
                    print("Не вдалося отримати дані з API")
                    await send_telegram_message(tg_chat_id, message, DATABASE_FILE)
                    await send_telegram_message(tg_chat_id_2, message, DATABASE_FILE)
            except:
                try:
                    if current_data and 'dict_tom' in current_data['data']:
                        message = (
                            f"Дата зміни на завтра: {
                                current_data['data']['dict_tom']['modified_on']}"
                        )
                        start_parsing_tomorrow()
                        print("Знайдено зміни на завтра!")
                        await send_telegram_message(tg_chat_id, message, DATABASE_FILE)
                        await send_telegram_message(tg_chat_id_2, message, DATABASE_FILE)
                except:
                    message = (
                        "Інформації на завтра немає"
                    )
                    print('Інформації на завтра немає')
                    await send_telegram_message(tg_chat_id, message, DATABASE_FILE)
                    await send_telegram_message(tg_chat_id_2, message, DATABASE_FILE)
        except asyncio.CancelledError:
            print("Моніторинг зупинено через невдале підключення.")
            break  # Завершуємо цикл, якщо було викликано CancelledError
        # Затримка між перевірками
        await asyncio.sleep(CHECK_INTERVAL)

# Запуск моніторингу
asyncio.run(monitor_api())
